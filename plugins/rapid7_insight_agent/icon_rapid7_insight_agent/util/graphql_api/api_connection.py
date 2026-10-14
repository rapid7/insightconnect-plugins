import logging
from typing import Optional, List, Tuple, Dict, Any

import requests
from datetime import datetime, timedelta, timezone

from icon_rapid7_insight_agent.util.graphql_api import agent_typer
from icon_rapid7_insight_agent.util.graphql_api.region_map import region_map
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from insightconnect_plugin_runtime.helper import clean

TIMEOUT_MINUTES = 3
ONLINE = "ONLINE"
OFFLINE = "OFFLINE"
STALE = "STALE"


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
        Find an agent based on a MAC address, IP address, hostname, or agent ID

        :param agent_input: MAC address, IP address, hostname, or agent ID
        :return:
        """

        agent_type = agent_typer.get_agent_type(agent_input)
        if agent_type != agent_typer.HOSTNAME:
            return self._get_agent(agent_input, agent_type, next_cursor)

        if not next_cursor and agent_typer.looks_like_agent_id(agent_input):
            if agent := self._get_agent_by_id(agent_input):
                return agent, None
        return self._get_agent_by_hostname(agent_input, next_cursor)

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
        agent_status = agent.get("agentStatus")
        if agent_status in (OFFLINE, STALE):
            self.logger.warning(
                f"Agent {agent_id} is {agent_status}. The unquarantine request will take effect when it comes back "
                "online."
            )

        # if exists then unquarantine it
        unquarantine_payload = {
            "query": "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id},
        }

        results_object = self._post_payload(unquarantine_payload)
        failed = results_object.get("data", {}).get("unquarantineAssets", {}).get("results", [])[0].get("failed")
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
            if quarantine and self._agent_status(agent) == STALE:
                unsuccessful_operations.append(
                    {"hostname": hostname, "error": f"Agent ID {agent_id} is stale and will not receive the request"}
                )
                continue
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
            assets = results_object.get("data", {}).get("assets", [])
            if assets and assets[0]:
                agent = assets[0].get("agent", {})
                quarantine_state = agent.get("quarantineState", {}).get("currentState")
                agent_status = agent.get("agentStatus")
            else:
                raise PluginException(
                    cause="No agents found",
                    assistance="Please verify the agent ID is correct.",
                    data=str(results_object),
                )
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

    def get_agent_state(self, agent_id: str) -> Optional[dict]:
        """
        Get the agent status and quarantine state of an agent

        :param agent_id: Agent ID to look up
        :return: dict with agentStatus and quarantineState, or None if no agent has this ID
        """
        payload = {
            "query": "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ agent { id quarantineState{ currentState } agentStatus } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id},
        }
        results_object = self._post_payload(payload)
        assets = results_object.get("data", {}).get("assets") or []
        return (assets[0] or {}).get("agent") if assets else None

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
        return result_object.get("data", {}).get("organizations", {}).get("edges", [])[0].get("node", {}).get("id")

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
            # Only fetched to choose between agents that share a hostname, so it is not part of the output
            agent["agent_info"].pop("timestamp", None)
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

    def _get_agent_by_id(self, agent_id: str) -> Optional[dict]:
        """
        Get an agent directly by its ID, without searching all pages of agents

        :param agent_id: Agent ID, with or without dashes
        :return: dict (agent object), or None if no agent has this ID
        """
        payload = {
            "query": "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } }",
            "variables": {"orgID": self.org_key, "agentID": agent_id.replace("-", "")},
        }
        self.logger.info(f"Looking up agent ID: {agent_id}")
        try:
            results_object = self._post_payload(payload)
        except PluginException as error:
            # The input may be a hostname that only looks like an ID; a real API problem also fails the search below
            self.logger.info(f"Agent ID lookup failed, searching by hostname instead: {error.cause}")
            return None
        assets = results_object.get("data", {}).get("assets") or []
        agent = assets[0] if assets else None
        return agent if agent and agent.get("host") else None

    def _get_agent_by_hostname(self, hostname: str, next_cursor: str = None) -> Tuple[Optional[dict], Optional[str]]:
        """
        Find the agent for a hostname. Pages are read until an online agent with the hostname is found, or there
        are no pages left. Of the agents found, an online one is used, otherwise the one that checked in most
        recently (see _choose_agent).

        :param hostname: Hostname
        :param next_cursor: Cursor to continue a previous search
        :return: tuple (agent object or empty dict, next cursor if the time limit was reached)
        """
        start_time = datetime.now()
        self.logger.info(f"Searching for: {hostname}")
        self.logger.info(f"Search type: {agent_typer.HOSTNAME}")
        matches = []
        has_next_page = True
        if not next_cursor:
            self.logger.info("Getting first page of agents...")
            has_next_page, next_cursor, agents = self._get_first_page_of_agents()
            self.logger.info("Initial agents received.")
            matches.extend(self._find_hostname_matches(agents, hostname))
        while not self._has_online_agent(matches) and has_next_page:
            current_time = datetime.now()
            if (current_time - start_time) > timedelta(minutes=TIMEOUT_MINUTES):
                self.logger.info("List of agents is too long, action will time out.")
                stopped = (
                    f"Stopped searching for '{hostname}' at the {TIMEOUT_MINUTES}-minute limit before all pages "
                    "were read."
                )
                if matches:
                    self.logger.warning(
                        f"{stopped} Returning the first agent found with this hostname; other agents with the same "
                        "hostname may exist on the pages that were not searched."
                    )
                    return matches[0], None
                self.logger.info(f"{stopped} Run the action again with the next cursor to search the remaining pages.")
                return None, next_cursor

            self.logger.info(f"Extra pages of agents: {has_next_page}")
            has_next_page, next_cursor, next_agents = self._get_next_page_of_agents(next_cursor)
            matches.extend(self._find_hostname_matches(next_agents, hostname))

        if not matches:
            self.logger.info("No assets were found")
            return {}, None
        return self._choose_agent(matches, hostname, all_pages_read=not has_next_page), None

    def _get_agents(self, agents_input: List[str]) -> [Tuple[str, dict]]:
        """
        Get multiple agents by hostname, choosing between agents that share a hostname as Get Agent Details does
        :param agents_input: Hostnames
        :return: List of found hostname and agent details
        """
        matches = {hostname: [] for hostname in agents_input}

        self.logger.info("Getting all agents...")
        has_next_page, next_cursor, agents = self._get_first_page_of_agents()
        self.logger.info("Initial agents received.")
        self._match_hostnames(agents, matches)
        # See if we have more pages of data, if so get next page and append until we reach the end
        self.logger.info(f"Extra pages of agents: {has_next_page}")
        while has_next_page and not all(self._has_online_agent(found) for found in matches.values()):
            has_next_page, next_cursor, next_agents = self._get_next_page_of_agents(next_cursor)
            self._match_hostnames(next_agents, matches)

        found_agents = []
        for hostname, found in matches.items():
            if found:
                found_agents.append((hostname, self._choose_agent(found, hostname, all_pages_read=not has_next_page)))
        return found_agents

    def _match_hostnames(self, agents: List[dict], matches: Dict[str, List[dict]]) -> None:
        """
        Add the agents on one page to the matches of each hostname that has no online agent yet

        :param agents: Agents from one page of results
        :param matches: Matching agents per hostname, updated in place
        :return: None
        """
        for hostname, found in matches.items():
            if not self._has_online_agent(found):
                found.extend(self._find_hostname_matches(agents, hostname))

    def _find_hostname_matches(self, agents: List[dict], hostname: str) -> List[dict]:
        """
        Find the agents on one page that match a hostname

        :param agents: Agents from one page of results
        :param hostname: Hostname to match
        :return: The matching agents, in page order
        """
        return [agent for agent in agents if agent and agent.get("host") and self._is_hostname_match(agent, hostname)]

    def _choose_agent(self, matches: List[dict], hostname: str, all_pages_read: bool) -> dict:
        """
        Choose one agent from those that match a hostname: an online one if there is one, otherwise the one that
        checked in most recently. Agents without a check-in time count as the oldest, and ties keep the order in
        which the agents were found. When more than one agent matches, the choice is logged.

        :param matches: Agents that match the hostname, in the order they were found
        :param hostname: The hostname that was searched for, used in the log message
        :param all_pages_read: Whether every page of agents was searched
        :return: The chosen agent
        """
        chosen = max(matches, key=lambda agent: (self._is_online(agent), self._last_check_in(agent) or 0))
        if len(matches) > 1:
            count = str(len(matches)) if all_pages_read else f"At least {len(matches)}"
            last_check_in = self._last_check_in(chosen)
            if self._is_online(chosen):
                reason = "it is online"
            elif last_check_in:
                checked_in = datetime.fromtimestamp(last_check_in / 1000, tz=timezone.utc)
                reason = (
                    f"none is online and it checked in most recently, at {checked_in.isoformat(timespec='seconds')}"
                )
            else:
                reason = "none is online or has a check-in time, so it is the first one found"
            self.logger.warning(
                f"{count} agents share the hostname '{hostname}'. Using agent {chosen.get('id')} because {reason}."
            )
        return chosen

    def _has_online_agent(self, agents: List[dict]) -> bool:
        return any(self._is_online(agent) for agent in agents)

    @staticmethod
    def _agent_status(agent: dict) -> Optional[str]:
        # Some assets come back without an agent
        return (agent.get("agent") or {}).get("agentStatus")

    def _is_online(self, agent: dict) -> bool:
        return self._agent_status(agent) == ONLINE

    @staticmethod
    def _last_check_in(agent: dict) -> Optional[float]:
        # Time of the last check-in to the platform, in Unix milliseconds
        return (agent.get("agent") or {}).get("timestamp")

    def _get_first_page_of_agents(self) -> (bool, str, list):
        """
        Get the first page of agents

        :return: tuple (boolean, str, list (agents))
        """
        payload = {
            "query": "query( $orgId:String! ) { organization(id: $orgId) { assets( first: 10000 ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } timestamp } } } } } }",
            "variables": {"orgId": self.org_key},
        }
        results_object = self._post_payload(payload)
        page_info = results_object.get("data", {}).get("organization", {}).get("assets", {}).get("pageInfo", {})
        return (
            page_info.get("hasNextPage"),
            page_info.get("endCursor"),
            self._get_agents_from_result_object(results_object),
        )

    def _get_next_page_of_agents(self, next_cursor: str) -> (bool, dict, list):
        """
        In the case of multiple pages of returned agents, this will go through each page and append
        those agents to the agents list

        :param next_cursor: str
        :return: tuple (boolean, str, list (agents))
        """
        self.logger.info(f"Getting next page of agents using cursor {next_cursor}")
        payload = {
            "query": "query( $orgId:String! $nextCursor:String! ) { organization(id: $orgId) { assets( first: 10000, after: $nextCursor ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } timestamp } } } } } }",
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

    def _is_ip_match(self, agent: dict, agent_input: str) -> bool:
        """
        Check if the agent's primary IP address matches the input.

        :param agent: Agent dictionary
        :param agent_input: IP address to match
        :return: True if IP matches, False otherwise
        """
        return agent_input == agent.get("host", {}).get("primaryAddress", {}).get("ip")

    def _is_hostname_match(self, agent: dict, agent_input: str) -> bool:
        """
        Check if the agent's ID or any of its hostnames match the input.

        :param agent: Agent dictionary
        :param agent_input: Hostname or ID to match
        :return: True if hostname or ID matches, False otherwise
        """
        if agent_input == agent.get("host", {}).get("id"):
            return True
        for host_name in agent.get("host", {}).get("hostNames", []):
            if agent_input.lower() == host_name.get("name", "").lower():
                return True
        return False

    def _is_mac_match(self, agent: dict, agent_input: str) -> bool:
        """
        Check if the agent's MAC address matches the input, ignoring separators.

        :param agent: Agent dictionary
        :param agent_input: MAC address to match
        :return: True if MAC matches, False otherwise
        """
        stripped_input_mac = agent_input.replace("-", "").replace(":", "")
        stripped_target_mac = (
            agent.get("host", {}).get("primaryAddress", {}).get("mac", "").replace("-", "").replace(":", "")
        )
        return stripped_input_mac == stripped_target_mac

    def _find_agent_in_agents(self, agents: [dict], agent_input: str, agent_type: str) -> Optional[dict]:  # noqa: C901
        """
        Given a list of agent objects, find the agent that matches our input. Hostnames are matched by
        _find_hostname_matches instead.

        If no agent is found this will return None

        :param agents: list (agents)
        :param agent_input: MAC address or IP address
        :param agent_type: What type of input to look for (MAC or IP_ADDRESS)

        :return: dict (agent object), None
        """
        self.logger.info(f"Searching for: {agent_input}")
        self.logger.info(f"Search type: {agent_type}")
        self.logger.info("Skipping all agents where host information is not available")
        for agent in agents:
            if agent and len(agent) and agent.get("host"):  # Some hosts come back None...need to check for that
                if agent_type == agent_typer.IP_ADDRESS:
                    if self._is_ip_match(agent, agent_input):
                        return agent
                elif agent_type == agent_typer.MAC_ADDRESS:
                    # MAC addresses can come in with : or - as a separator, remove all of it and compare
                    if self._is_mac_match(agent, agent_input):
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
            edges = results_object.get("data", {}).get("organization", {}).get("assets", {}).get("edges")
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
