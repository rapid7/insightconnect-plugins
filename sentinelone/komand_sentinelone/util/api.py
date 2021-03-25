from json import dumps, loads
from re import match
from insightconnect_plugin_runtime.exceptions import PluginException

import requests


class SentineloneAPI:
    def __init__(self, url, make_token_header):
        self.url = url
        self.token_header = make_token_header

    def search_agents(
        self,
        agent_details: str,
        agent_active: bool = True,
        case_sensitive: bool = True,
        operational_state: str = None,
        results_length: int = 0,
        api_version: str = "2.0",
    ) -> list:
        results = []
        if agent_details:
            for search in self.__get_searches(agent_details):
                agents = [agent_details]

                # Normalize casing if specified
                if not case_sensitive:
                    if search == "computerName":
                        agents = [agent_details.lower(), agent_details.upper()]
                    if search == "uuid":
                        agents = [agent_details.lower()]

                for agent in agents:
                    endpoint = f"{self.url}web/api/v{api_version}/agents?{search}={agent}"
                    output = requests.get(endpoint, headers=self.token_header)

                    if output.status_code == 200 and output.json()["pagination"]["totalItems"] >= 1:
                        results.append(output.json()["data"][0])

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

    def get_agent_uuid(self, agent):
        agents = self.search_agents(agent)
        if self.__check_agents_found(agents):
            raise PluginException(
                cause=f"No agents found for: {agent}.", assistance="Please check provided information and try again."
            )
        else:
            agent_uuid = agents[0].get("uuid")
        return agent_uuid

    @staticmethod
    def __get_searches(agent_details: str) -> list:
        if len(agent_details) == 18 and agent_details.isdigit():
            return ["ids"]
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", agent_details):
            return ["networkInterfaceInet__contains", "externalIp__contains"]
        if match(r"((?:(\d{1,2}|[a-fA-F]{1,2}){2})(?::|-*)){6}", agent_details):
            return ["networkInterfacePhysical__contains", "uuid"]
        else:
            return ["computerName"]

    @staticmethod
    def clean_results(results):
        return loads(dumps(results).replace("null", '"None"'))

    @staticmethod
    def __check_agents_found(agents: list) -> bool:
        if len(agents) > 1:
            raise PluginException(
                cause="Multiple agents found.",
                assistance="Please provide a unique agent identifier so the action can be performed on the intended agent.",
            )
        if len(agents) == 0:
            return True
        return False
