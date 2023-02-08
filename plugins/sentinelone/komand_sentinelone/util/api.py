from json import dumps, loads
from re import match
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean_list, clean_dict
from typing import List, Any, Dict
import requests

default_array = [
    "computerMemberOf",
    "lastUserMemberOf",
    "locations",
    "networkInterfaces",
    "inet",
    "inet6",
    "userActionsNeeded",
]


def clean(obj):
    """
    Returns a new but cleaned JSON object.

    * Recursively iterates through the collection
    * None type values are removed
    * Empty string values are removed

    This function is designed so we only return useful data
    """

    cleaned = clean_list(obj) if isinstance(obj, list) else clean_dict(obj)

    # The only *real* difference here is how we have to iterate through these different collection types
    if isinstance(cleaned, list):
        for key, value in enumerate(cleaned):
            if isinstance(value, list) or isinstance(value, dict):  # pylint: disable=consider-merging-isinstance
                cleaned[key] = clean(value)
            if value is None or value == "None":
                cleaned[key] = []
    elif isinstance(cleaned, dict):
        for key, value in cleaned.items():
            if isinstance(value, dict) or isinstance(value, list):  # pylint:disable=consider-merging-isinstance
                cleaned[key] = clean(value)
            if key in default_array and (value is None or value == "None"):
                cleaned[key] = []

    return cleaned


class SentineloneAPI:
    def __init__(self, url, make_token_header):
        self.url = url
        self.token_header = make_token_header

    @staticmethod
    def set_agents_array(search: str, agent_details: str, agents: List[str]) -> List[str]:
        """
        Checks Search and assigns agents appropriate values
        :param search: String that will be searched for
        :type: str

        :param agent_details: Details of agent
        :type: str

        :param agents: List of agents
        :type: List[str]

        :returns agents: List of agents
        :rtype: List[str]
        """
        # Normalize casing if specified
        if search == "computerName":
            agents = [agent_details.lower(), agent_details.upper()]
        if search == "uuid":
            agents = [agent_details.lower()]
        return agents

    def get_agents_data(self, agent: str, api_version: str, search: str, results: List[Dict[str, Any]]) -> None:
        """
        Gets agents Data
        :param agent: Agent to get details for
        :type: str

        :param api_version: Version of API
        :type: str

        :param search: String that will be searched for
        :type: str

        :param results: Array containing agent results
        :type: List[Dict[str, Any]]
        """

        endpoint = f"{self.url}web/api/v{api_version}/agents?{search}={agent}"
        output = requests.get(endpoint, headers=self.token_header)
        if output.status_code == 200 and output.json().get("pagination", {}).get("totalItems", 0) >= 1:
            agents_data = output.json().get("data", [])
            if agents_data and agents_data[0] not in results:
                results.append(agents_data[0])

    def search_agents(
        self,
        agent_details: str,
        agent_active: bool = True,
        case_sensitive: bool = True,
        operational_state: str = None,
        results_length: int = 0,
        api_version: str = "2.0",
    ) -> List[Dict[str, Any]]:
        """
        Searches for agents
        :param agent_details: Details of agent
        :type: str

        :param agent_active: If the Agent is Active
        :type: bool

        :param case_sensitive: If the search is case_sensitive
        :type: bool

        :param operational_state: If in Operational states
        :type: bool

        :param results_length: Length of result
        :type: int

        :param api_version: API Version
        :type: str

        :return: self.clean_results(results)
        :rtype: List[Dict[str, Any]]
        """
        results = []
        if agent_details:
            for search in self.__get_searches(agent_details):
                agents = [agent_details]

                # Normalize casing if specified
                if not case_sensitive:
                    agents = self.set_agents_array(search, agent_details, agents)

                for agent in agents:
                    self.get_agents_data(agent, api_version, search, results)

                if results_length:
                    if len(results) >= results_length:
                        return self.clean_results(results)

        else:
            output = requests.get(
                f"{self.url}web/api/v{api_version}/agents?isActive={agent_active}", headers=self.token_header
            )
            results.extend(output.json()["data"])

        if operational_state and operational_state != "Any":
            for agent in results:
                if agent.get("operationalState") != operational_state:
                    results.pop(results.index(agent))

        return self.clean_results(results)

    def get_agent_uuid(self, agent: str) -> str:
        """
        Get Agent UUID
        :param agent: The Agent
        :type: str

        :return agent_uuid: The agent UUID
        :rtype: str
        """
        agents = self.search_agents(agent)
        if self.__check_agents_found(agents):
            raise PluginException(
                cause=f"No agents found for: {agent}.", assistance="Please check provided information and try again."
            )
        else:
            agent_uuid = agents[0].get("uuid")
        return agent_uuid

    @staticmethod
    def __get_searches(agent_details: str) -> List[str]:
        """
        Get Search Type
        :param agent_details:
        :type: str

        :return: String containing Search Type
        :rtype: List[str]
        """
        if len(agent_details) == 18 and agent_details.isdigit():
            return ["ids"]
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", agent_details):
            return ["networkInterfaceInet__contains", "externalIp__contains"]
        if match(r"((?:(\d{1,2}|[a-fA-F]{1,2}){2})(?::|-*)){6}", agent_details):
            return ["networkInterfacePhysical__contains", "uuid"]
        else:
            return ["computerName"]

    @staticmethod
    def clean_results(results: List) -> List[Dict[str, Any]]:
        """
        Cleans Results
        :param results: List of results
        :type: List

        :return: clean(loads(dumps(results).replace("null", '"None"')))
        :rtype: List[Dict[str, Any]]
        """
        return clean(loads(dumps(results).replace("null", '"None"')))

    @staticmethod
    def __check_agents_found(agents: List[Dict[str, Any]]) -> bool:
        """
        Checks if Agents are found
        :param agents: List of Agents
        :type: List[str]

        :return: True or False
        :type: bool
        """
        if len(agents) > 1:
            raise PluginException(
                cause="Multiple agents found.",
                assistance="Please provide a unique agent identifier so the action can be performed on the intended agent.",
            )
        if len(agents) == 0:
            return True
        return False
