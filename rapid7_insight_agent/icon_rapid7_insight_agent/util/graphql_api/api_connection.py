from icon_rapid7_insight_agent.util.graphql_api.region_map import region_map
from icon_rapid7_insight_agent.util.graphql_api.api_exception import APIException
from typing import Any
import icon_rapid7_insight_agent.util.graphql_api.agent_typer as agent_typer
import requests
import logging


class ApiConnection:
    """
    ApiConnection(api_key, region_string, logger)

    A class to connect to the Insight Agent GraphQL. This class provides convenience methods to perform actions
    on Insight Agents.
    """
    def __init__(self,
                 api_key: str,
                 region_string: str,
                 logger: logging.Logger
                 ) -> None:

        self.api_key = api_key
        self.logger = logger
        self.endpoint = self._setup_endpoint(region_string)

        self.session = requests.Session()
        self.session.headers = self._get_headers()

        self.org_key = self._get_org_key()
        self.logger.info(f"Received org key: ********-****-****-****-*******{self.org_key[-5:]}")

    def get_agent(self,
                  agent_input: str
                  ) -> dict:
        """
        Find an agent based on a Mac Address, IP, or Hostname

        :param agent_input: string
        :return:
        """

        agent_type = agent_typer.get_agent_type(agent_input)
        agent = self._get_agent(agent_input, agent_type)
        return agent

    def quarantine(self,
                   advertisement_period: int,
                   agent_id: str
                   ) -> bool:
        """
        quarantine action on a given agent ID

        :param advertisement_period: int (Amount of time in seconds to try to take the quarantine action)
        :param agent_id: string

        :return: boolean
        """
        quarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String! $advPeriod:Long! ) { quarantineAssets( orgId:$orgID assetIds: [$agentID] input: {advertisementPeriod: $advPeriod} ) { results { assetId failed } } }",
            "variables": {
                "orgID": self.org_key,
                "agentID": agent_id,
                "advPeriod": advertisement_period
            }
        }

        results_object = self._post_payload(quarantine_payload)
        failed = results_object.get("data").get("quarantineAssets").get("results")[0].get("failed")
        return not failed

    def unquarantine(self,
                     agent_id: str
                     ) -> bool:
        """
        unquarantine action on a given agent ID
        :param agent_id: string

        :return: boolean
        """
        unquarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }",
            "variables": {
                "orgID": self.org_key,
                "agentID": agent_id
            }
        }

        results_object = self._post_payload(unquarantine_payload)
        failed = results_object.get("data").get("unquarantineAssets").get("results")[0].get("failed")
        return not failed

    def get_agent_status(self,
                         agent_id: str
                         ) -> dict:
        """
        This will get agent status information from a specified agent

        :param agent_id: string
        :return: dict
        """
        payload = {
            "query": "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ agent { id quarantineState{ currentState } agentStatus } } }",
            "variables": {
              "orgID": self.org_key,
              "agentID": agent_id
            }
        }

        results_object = self._post_payload(payload)

        agent = results_object.get("data").get("assets")[0].get("agent")
        quarantine_state = agent.get("quarantineState").get("currentState")
        agent_status = agent.get("agentStatus")

        is_online = True if agent_status == "ONLINE" else False
        is_quarantine_requested = True if quarantine_state == "QUARANTINE_IN_PROGRESS" else False
        is_unquarantine_requested = True if quarantine_state == "UNQUARANTINE_IN_PROGRESS" else False
        is_is_quarantined = True if (quarantine_state == "QUARANTINED" or quarantine_state == "UNQUARANTINE_IN_PROGRESS") else False

        return {
            "is_currently_quarantined": is_is_quarantined,
            "is_asset_online": is_online,
            "is_quarantine_requested": is_quarantine_requested,
            "is_unquarantine_requested": is_unquarantine_requested
        }

    def connection_test(self) -> bool:
        # Return the first org to verify the connection works
        graph_ql_payload = {
            "query": "{ organizations(first: 1) { edges { node { id } } totalCount } }"
        }

        # If no exceptions are thrown, we have a valid connection
        self._post_payload(graph_ql_payload)
        return True

    #################
    # Private Methods
    #################

    def _get_org_key(self) -> str:
        """
        Get the org key from GraphQL

        :return: String
        """

        payload = {
            "query": "{ organizations(first: 1) { edges { node { id name } } } }"
        }
        result_object = self._post_payload(payload)
        self.logger.info("Organization ID query complete.")
        return result_object.get("data").get("organizations").get("edges")[0].get("node").get("id")

    def _get_headers(self) -> dict:
        """
        This build and returns headers for the request session

        :return: dict
        """
        return {
            "X-Api-key": self.api_key,
            "Accept-Version": "kratos",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br"
        }

    def _post_payload(self,
                      payload: dict
                      ) -> dict:
        """
        This will post a given payload to the API using the connection session

        :param payload: dict
        :return: dict
        """
        result = self.session.post(self.endpoint, json=payload)

        try:
            result.raise_for_status()
        except Exception:
            raise APIException(cause="Error connecting to the Insight Agent API.",
                               assistance="Please check your Organization ID and API key.\n",
                               data=result.text)

        results_object = result.json()

        if results_object.get("errors"):
            raise APIException(cause="The Insight Agent API returned errors",
                               assistance=results_object.get("errors"))

        return results_object

    def _setup_endpoint(self,
                        region_string: str
                        ) -> str:
        """
        Creates the URL endpoint for the API based on the region

        :param region_string: string
        :return: string
        """
        region_code = region_map.get(region_string)

        if region_code:
            endpoint = f"https://{region_code}.api.insight.rapid7.com/graphql"
        else:
            # It's an enum, hopefully this never happens.
            raise APIException(cause="Region not found.",
                               assistance="Region code was not found for selected region. Available regions are: United States, "
                                          "Europe, Canada, Australia, Japan")

        return endpoint

    def _get_agent(self,
                   agent_input: str,
                   agent_type: str
                   ) -> dict:
        """
        Gets an agent from a Mac, IP, or Hostname.

        :return: dict
        """
        agents = []
        payload = {
            "query": "query($orgId: String!) {organization(id: $orgId) { assets(first: 10000) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } } ",
            "variables": {
                "orgId": self.org_key
            }
        }

        self.logger.info(f"Getting all agents...")
        results_object = self._post_payload(payload)

        has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get("hasNextPage")
        agents.extend(self._get_agents_from_result_object(results_object))
        self.logger.info(f"Initial agents received.")

        agent = self._find_agent_in_agents(agents, agent_input, agent_type)
        if agent:
            return agent

        # See if we have more pages of data, if so get next page and append until we reach the end
        self.logger.info(f"Extra pages of agents: {has_next_page}")
        while has_next_page:
            self.logger.info(f"Getting next page of agents.")
            has_next_page, results_object, next_agents = self._get_next_page_of_agents(results_object)
            agent = self._find_agent_in_agents(next_agents, agent_input, agent_type)
            if agent:
                return agent

        raise APIException(cause=f"Could not find agent matching {agent_input} of type {agent_type}.",
                           assistance=f"Check the agent input value and try again.",
                           data="NA")

    def _get_next_page_of_agents(self,
                                 results_object: dict
                                 ) -> (bool, dict, list):
        """
        In the case of multiple pages of returned agents, this will go through each page and append
        those agents to the agents list

        :param results_object: dict
        :return: tuple (boolean, dict (results), list (agents))
        """
        self.logger.info(f"Getting next page of agents.")
        next_cursor = results_object.get("data").get("organization").get("assets").get("pageInfo").get("endCursor")
        payload = {
            "query": "query( $orgId:String! $nextCursor:String! ) { organization(id: $orgId) { assets( first: 10000 after: $nextCursor ) { pageInfo { hasNextPage endCursor } edges { node { host { id vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } id agent { id } } } } } }",
            "variables": {
                "orgId": self.org_key,
                "nextCursor": next_cursor
            }
        }
        results_object = self._post_payload(payload)

        has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get(
            "hasNextPage")

        next_agents = self._get_agents_from_result_object(results_object)

        return has_next_page, results_object, next_agents

    def _find_agent_in_agents(self,
                              agents: list,
                              agent_input: str,
                              agent_type: str
                              ) -> Any:
        """
        Given a list of agent objects, find the agent that matches our input.

        If no agent is found this will return None

        :param agents: list (agents)
        :param agent_input: String (Input value to look for)
        :param agent_type: String (What type of input to look for, MAC, IP_ADDRESS, or HOSTNAME)

        :return: dict (agent object), None
        """
        self.logger.info(f"Searching for: {agent_input}")
        self.logger.info(f"Search type: {agent_type}")
        for agent in agents:
            if agent_type == agent_typer.IP_ADDRESS:
                if agent_input == agent.get("primaryAddress").get("ip"):
                    return agent
            elif agent_type == agent_typer.HOSTNAME:
                # In this case, we have an alpha/numeric value. This could be the ID or the Hostname. Need to check both
                if agent_input == agent.get("id"):
                    return agent
                for host_name in agent.get("hostNames"):
                    if agent_input == host_name.get("name"):
                        return agent
            elif agent_type == agent_typer.MAC_ADDRESS:
                # Mac addresses can come in with : or - as a separator, remove all of it and compare
                stripped_input_mac = agent_input.replace("-", "").replace(":", "")
                stripped_target_mac = agent.get("primaryAddress").get("mac").replace("-", "").replace(":", "")
                if stripped_input_mac == stripped_target_mac:
                    return agent
            else:
                raise APIException(cause="Could not determine agent type.",
                                   assistance=f"Agent {agent_input} was not a MAC address, IP address, or hostname.")

        return None  # No agent found

    def _get_agents_from_result_object(self,
                                       results_object: dict
                                       ) -> list:
        """
        This will extract an agent object from the object that's returned from the API

        :param results_object: dict (API result payload)
        :return: list (agent objects)
        """
        agent_list = []

        try:
            edges = results_object.get("data").get("organization").get("assets").get("edges")
            for edge in edges:
                agent = edge.get("node").get("host")
                agent_list.append(agent)
        except KeyError:
            raise APIException(cause="Insight Agent API returned data in an unexpected format.\n",
                               data=str(results_object))

        return agent_list
