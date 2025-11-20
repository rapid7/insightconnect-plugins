import logging
from typing import Optional, List, Tuple, Dict, Any

import requests
from datetime import datetime, timedelta

from icon_rapid7_insight_agent.util.graphql_api import agent_typer
from icon_rapid7_insight_agent.util.graphql_api.region_map import region_map
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from insightconnect_plugin_runtime.helper import clean

TIMEOUT_MINUTES = 3


class ApiConnection:
    """
    ApiConnection(api_key, region_string, logger)

    A class to connect to the Insight Agent GraphQL. This class provides convenience methods to perform actions
    on Insight Agents.
    """

    def __init__(self, api_key: str, region_string: str, logger: logging.Logger) -> None:

        self.api_key = api_key
        self.region = region_string
        self.logger = logger
        self._setup(region_string)

    def get_agent(self, agent_input: str, next_cursor: str) -> dict:
        """
        Find an agent based on a MAC address, IP address, or hostname

        :param agent_input: MAC address, IP address, or hostname
        :return:
        """

        agent_type = agent_typer.get_agent_type(agent_input)
        return self._get_agent(agent_input, agent_type, next_cursor)

    def quarantine(self, advertisement_period: int, agent_id: str) -> bool:
        """
        Quarantine an agent given an agent ID

        :param advertisement_period: Amount of time, in seconds, to try to take the quarantine action
        :param agent_id: Agent ID to quarantine

        :return: Boolean indicating whether or not the quarantine succeeded
        """
        quarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String! $advPeriod:Long! ) { quarantineAssets( orgId:$orgID assetIds: [$agentID] input: {advertisementPeriod: $advPeriod} ) { results { assetId failed } } }",
            "variables": {
                "orgID": self.org_key,
                "agentID": agent_id,
                "advPeriod": advertisement_period,
            },
        }

        results_object = self._post_payload(quarantine_payload)
        failed = results_object.get("data", {}).get("quarantineAssets", {}).get("results", [])[0].get("failed")
        return not failed

    def unquarantine(self, agent_id: str) -> bool:
        """
        Unquarantine an agent given an agent ID
        :param agent_id: Agent ID to unquarantine

        :return: boolean
        """

        # Check if agent with ID exists
        payload = {
            "query": "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ agent { id quarantineState{ currentState } agentStatus } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id},
        }
        results_object = self._post_payload(payload)
        agent = results_object.get("data", {}).get("assets", [])[0].get("agent")
        if not agent:
            return False

        # if exists then unquarantine it
        unquarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id},
        }

        results_object = self._post_payload(unquarantine_payload)
        failed = results_object.get("data").get("unquarantineAssets").get("results")[0].get("failed")
        return not failed

    def quarantine_list(
        self, agent_hostnames: List[str], advertisement_period: int, quarantine: bool = True
    ) -> Tuple[List[str], List[dict]]:
        """
        Quarantine or un-quarantine an agent given a list of agent hostnames

        :param agent_hostnames: List of agent hostnames to quarantine or un-quarantine
        :param advertisement_period: Amount of time, in seconds, to try to take the quarantine/un-quarantine action
        :param quarantine: Boolean value, True to quarantine, False to un-quarantine

        :return: Two lists containing hostnames for successful or unsuccessful quarantines/un-quarantines
        """
        # Raise exception if the provided list is empty
        self._check_empty(agent_hostnames)
        # Find agents from hostname
        found_agents = self._get_agents(agent_hostnames)
        # Create empty lists for successful & unsuccessful
        successful_operations = []
        not_found = list(set(agent_hostnames).difference(dict(found_agents)))
        unsuccessful_operations = [{"hostname": agent, "error": "Hostname could not be found"} for agent in not_found]
        # For each agent ID in the list, perform quarantine
        for hostname, agent in found_agents:
            agent_id = agent.get("id")
            result = self.quarantine(advertisement_period, agent_id) if quarantine else self.unquarantine(agent_id)
            if result:
                successful_operations.append(hostname)
            else:
                unsuccessful_operations.append(
                    {"hostname": hostname, "error": f"Agent ID {agent_id} " "could not be (un-)quarantined"}
                )
        return successful_operations, unsuccessful_operations

    def get_agent_status(self, agent_id: str) -> dict:
        """
        Get status information from a specified agent

        :param agent_id: Agent ID to get status information for
        :return: dict
        """
        payload = {
            "query": "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ agent { id quarantineState{ currentState } agentStatus } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id},
        }

        results_object = self._post_payload(payload)
        try:
            agent = results_object.get("data").get("assets")[0].get("agent")
            quarantine_state = agent.get("quarantineState").get("currentState")
            agent_status = agent.get("agentStatus")
        except (Exception, IndexError):
            raise PluginException(
                cause="Received an unexpected response from the server.",
                assistance="Verify your plugin connection inputs are correct especially region. If the issue persists, please contact support.",
                data=str(results_object),
            )

        is_online = bool(agent_status == "ONLINE")
        is_quarantine_requested = bool(quarantine_state == "QUARANTINE_IN_PROGRESS")
        is_unquarantine_requested = bool(quarantine_state == "UNQUARANTINE_IN_PROGRESS")
        is_is_quarantined = bool(quarantine_state in ("QUARANTINED", "UNQUARANTINE_IN_PROGRESS"))

        return {
            "is_currently_quarantined": is_is_quarantined,
            "is_asset_online": is_online,
            "is_quarantine_requested": is_quarantine_requested,
            "is_unquarantine_requested": is_unquarantine_requested,
        }

    def connection_test(self) -> bool:
        # Return the first org to verify the connection works
        graph_ql_payload = {"query": "{ organizations(first: 1) { edges {node { id name } } totalCount } }"}

        # If no exceptions are thrown, we have a valid connection
        result = self._post_payload(graph_ql_payload)
        orgs = result.get("data", {}).get("organizations", {}).get("edges", [])
        if len(orgs) == 0:
            raise ConnectionTestException(data="No organizations found")
        if orgs[0].get("node", {}).get("name") is None:
            raise ConnectionTestException(
                data=f"Org ID: ********-****-****-****-*******{self.org_key[-5:]} found but "
                f"does not belong to region {self.region}"
            )
        return True

    #################
    # Private Methods
    #################

    def _setup(self, region_string: str) -> None:
        """
        Setup the API connection

        :param region_string: The human readable name of the region. e.x. "United States"
        :return: None
        """
        self.endpoint = self._setup_endpoint(region_string)

        self.org_key = self._get_org_key()
        self.logger.info(f"Received org key: ********-****-****-****-*******{self.org_key[-5:]}")

    def _get_org_key(self) -> str:
        """
        Get the org key from GraphQL

        :return: String
        """

        payload = {"query": "{ organizations(first: 1) { edges { node { id name } } } }"}
        result_object = self._post_payload(payload)
        self.logger.info("Organization ID query complete.")
        return result_object.get("data").get("organizations").get("edges")[0].get("node").get("id")

    def _get_headers(self) -> dict:
        """
        Build and return headers for the API

        :return: dict
        """
        return {
            "X-Api-key": self.api_key,
            "Accept-Version": "kratos",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
        }

    def _post_payload(self, payload: dict) -> dict:
        """
        This will post a given payload to the API using the connection session

        :param payload: dict
        :return: dict
        """
        _request = requests.Request(method="POST", headers=self._get_headers(), url=self.endpoint, json=payload)
        try:
            with requests.Session() as session:
                prepared_request = session.prepare_request(request=_request)
                result = session.send(prepared_request)
        except Exception as e:
            raise PluginException(
                cause="Error connecting to the Insight Agent API.",
                assistance="Please check your Region and API key.\n",
                data=str(e),
            )

        results_object = result.json()

        if results_object.get("errors"):
            raise PluginException(
                cause="The Insight Agent API returned errors",
                assistance=results_object.get("errors"),
            )

        return results_object

    def _setup_endpoint(self, region_string: str) -> str:
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
            raise PluginException(
                cause="Region not found.",
                assistance="Region code was not found for selected region. Available regions are: United States, "
                "Europe, Canada, Australia, Japan",
            )

        return endpoint

    def get_agents_by_ip(self, ip_address: str, next_cursor: str = None) -> List[Dict[str, Any]]:
        start_time = datetime.now()
        agents = []
        has_next_page = True
        if not next_cursor:
            payload = {
                "query": "query( $orgId:String! ) { organization(id: $orgId) { assets( first: 10000 ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } } } } }",
                "variables": {"orgId": self.org_key},
            }

            self.logger.info(f"Getting first page of agents by IP: {ip_address}...")
            results_object = self._post_payload(payload)
            agents.extend(self._get_agents_from_result_object(results_object))
            self.logger.info("Initial agents received.")
            has_next_page = (
                results_object.get("data", {})
                .get("organization", {})
                .get("assets", {})
                .get("pageInfo", {})
                .get("hasNextPage")
            )
            next_cursor = (
                results_object.get("data", {})
                .get("organization", {})
                .get("assets", {})
                .get("pageInfo", {})
                .get("endCursor")
            )
        while has_next_page:
            current_time = datetime.now()
            if (current_time - start_time) > timedelta(minutes=TIMEOUT_MINUTES):
                self.logger.info("List of agents is too long, action will time out.")
                self.logger.info("More pages are available, please use the next cursor value to requery.")
                self.logger.info("Returning results...")
                return self._filter_agents(agents, ip_address), next_cursor
            # See if we have more pages of data, if so get next page and append until we reach the end
            self.logger.info(f"Extra pages of agents: {has_next_page}")
            has_next_page, next_cursor, next_agents = self._get_next_page_of_agents(next_cursor)
            agents.extend(next_agents)

        # Filter and return agents
        self.logger.info("No more pages are available and query has completed.")
        self.logger.info("Returning results...")
        return self._filter_agents(agents, ip_address), None

    def _filter_agents(self, agents: List, ip_address: str) -> List:
        filtered_agents = list(
            filter(
                lambda agent_: any(
                    (
                        agent_.get("publicIpAddress") == ip_address,
                        agent_.get("host", {}).get("primaryAddress", {}).get("ip") == ip_address,
                    )
                ),
                clean(agents),
            ),
        )

        # Rename 'agent' field name to 'agent_info'
        for agent in filtered_agents:
            agent["agent_info"] = agent.pop("agent")
        return filtered_agents

    def _get_agent(self, agent_input: str, agent_type: str, next_cursor: str = None) -> dict:
        """
        Gets an agent by MAC address, IP address, or hostname.

        :param agent_input: MAC address, IP address or hostname
        :param agent_type: Is the agent input a MAC, IP_ADDRESS, or HOSTNAME

        :return: dict
        """
        start_time = datetime.now()
        agents = []
        agent = None
        has_next_page = True
        if not next_cursor:
            payload = {
                "query": "query( $orgId:String! ) { organization(id: $orgId) { assets( first: 10000 ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } } } } }",
                "variables": {"orgId": self.org_key},
            }
            self.logger.info("Getting first page of agents...")
            results_object = self._post_payload(payload)

            agents.extend(self._get_agents_from_result_object(results_object))
            self.logger.info("Initial agents received.")

            agent = self._find_agent_in_agents(agents, agent_input, agent_type)
            # See if we have more pages of data, if so get next page and append until we reach the end
            has_next_page = (
                results_object.get("data", {})
                .get("organization", {})
                .get("assets", {})
                .get("pageInfo", {})
                .get("hasNextPage")
            )
            next_cursor = (
                results_object.get("data", {})
                .get("organization", {})
                .get("assets", {})
                .get("pageInfo", {})
                .get("endCursor")
            )
        while agent is None and has_next_page:
            current_time = datetime.now()
            if (current_time - start_time) > timedelta(minutes=TIMEOUT_MINUTES):
                self.logger.info("List of agents is too long, action will time out.")
                self.logger.info("More pages are available, please use the next cursor value to requery.")
                self.logger.info("Returning results...")
                return agent, next_cursor

            self.logger.info(f"Extra pages of agents: {has_next_page}")
            self.logger.info("Getting next page of agents.")
            has_next_page, next_cursor, next_agents = self._get_next_page_of_agents(next_cursor)
            agent = self._find_agent_in_agents(next_agents, agent_input, agent_type)
        if agent:
            return agent, None
        else:
            self.logger.info("No assets were found")
            return {}, None

    def _get_agents(self, agents_input: List[str]) -> [Tuple[str, dict]]:
        """
        Get multiple agents by MAC address, IP address, or hostname.
        :param agents_input: MAC address, IP address or hostnames
        :return: List of found hostname and agent details, list of agent hostnames now found
        """
        agents = []
        payload = {
            "query": "query( $orgId:String! ) { organization(id: $orgId) { assets( first: 10000 ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } } } } }",
            "variables": {"orgId": self.org_key},
        }

        self.logger.info("Getting all agents...")
        results_object = self._post_payload(payload)

        has_next_page = results_object.get("data").get("organization").get("assets").get("pageInfo").get("hasNextPage")
        next_cursor = (
            results_object.get("data", {})
            .get("organization", {})
            .get("assets", {})
            .get("pageInfo", {})
            .get("endCursor")
        )
        agents.extend(self._get_agents_from_result_object(results_object))
        found_agents = []
        self.logger.info("Initial agents received.")
        for agent_input in agents_input:
            agent = self._find_agent_in_agents(agents, agent_input, "Host Name")
            if agent:
                found_agents.append((agent_input, agent))
                agents_input.remove(agent_input)
        # See if we have more pages of data, if so get next page and append until we reach the end
        self.logger.info(f"Extra pages of agents: {has_next_page}")
        if agents_input:
            while has_next_page:
                has_next_page, next_cursor, next_agents = self._get_next_page_of_agents(next_cursor)
                for agent_input in agents_input:
                    agent = self._find_agent_in_agents(next_agents, agent_input, "Host Name")
                    if agent:
                        found_agents.append(Tuple[agent_input, agent])
                        agents_input.remove(agent_input)
        return found_agents

    def _get_next_page_of_agents(self, next_cursor: str) -> (bool, dict, list):
        """
        In the case of multiple pages of returned agents, this will go through each page and append
        those agents to the agents list

        :param next_cursor: str
        :return: tuple (boolean, str, list (agents))
        """
        self.logger.info(f"Getting next page of agents using cursor {next_cursor}")
        payload = {
            "query": "query( $orgId:String! $nextCursor:String! ) { organization(id: $orgId) { assets( first: 10000, after: $nextCursor ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } } } } }",
            "variables": {"orgId": self.org_key, "nextCursor": next_cursor},
        }
        results_object = self._post_payload(payload)

        has_next_page = (
            results_object.get("data", {})
            .get("organization", {})
            .get("assets", {})
            .get("pageInfo", {})
            .get("hasNextPage")
        )
        next_cursor = (
            results_object.get("data", {})
            .get("organization", {})
            .get("assets", {})
            .get("pageInfo", {})
            .get("endCursor")
        )

        next_agents = self._get_agents_from_result_object(results_object)

        return has_next_page, next_cursor, next_agents

    def _find_agent_in_agents(self, agents: [dict], agent_input: str, agent_type: str) -> Optional[dict]:  # noqa: C901
        """
        Given a list of agent objects, find the agent that matches our input.

        If no agent is found this will return None

        :param agents: list (agents)
        :param agent_input: MAC address, IP address, or hostname
        :param agent_type: What type of input to look for (MAC, IP_ADDRESS, or HOSTNAME)

        :return: dict (agent object), None
        """
        self.logger.info(f"Searching for: {agent_input}")
        self.logger.info(f"Search type: {agent_type}")
        self.logger.info("Skipping all agents where host information is not available")
        for agent in agents:
            if agent and len(agent) and agent.get("host"):  # Some hosts come back None...need to check for that
                if agent_type == agent_typer.IP_ADDRESS:
                    if agent_input == agent.get("host", {}).get("primaryAddress", {}).get("ip"):
                        return agent
                elif agent_type == agent_typer.HOSTNAME:
                    # In this case, we have an alpha/numeric value. This could be the ID or the Hostname. Need to check both
                    if agent_input == agent.get("host", {}).get("id"):
                        return agent
                    for host_name in agent.get("host", {}).get("hostNames"):
                        if agent_input.lower() == host_name.get("name", "").lower():
                            return agent
                elif agent_type == agent_typer.MAC_ADDRESS:
                    # MAC addresses can come in with : or - as a separator, remove all of it and compare
                    stripped_input_mac = agent_input.replace("-", "").replace(":", "")
                    stripped_target_mac = (
                        agent.get("host", {}).get("primaryAddress", {}).get("mac", "").replace("-", "").replace(":", "")
                    )
                    if stripped_input_mac == stripped_target_mac:
                        return agent
                else:
                    raise PluginException(
                        cause="Could not determine agent type.",
                        assistance=f"Agent {agent_input} was not a MAC address, IP address, or hostname.",
                    )
        return None  # No agent found

    def _get_agents_from_result_object(self, results_object: dict) -> [dict]:
        """
        This will extract an agent object from the object that's returned from the API

        :param results_object: dict (API result payload)
        :return: list (agent objects)
        """
        agent_list = []

        try:
            edges = results_object.get("data").get("organization").get("assets").get("edges")
            for edge in edges:
                agent = edge.get("node")
                agent_list.append(agent)
        except KeyError:
            raise PluginException(
                cause="Insight Agent API returned data in an unexpected format.\n",
                data=str(results_object),
            )

        return agent_list

    def _check_empty(self, agent_id_list: List[str]):
        """
        This method checks if the provided list is empty.

        :param agent_id_list: List of agent IDs to check
        :return: Either True or a PluginException
        """
        if not agent_id_list:
            raise PluginException(
                cause="Empty list provided.", assistance="\nPlease provide asset IDs to (un)quarantine."
            )
