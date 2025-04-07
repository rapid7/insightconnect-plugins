import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
import base64
import io
import time
import zipfile
import requests
from json.decoder import JSONDecodeError
from re import match
from typing import Any, Dict, List, Tuple
from urllib.parse import urlsplit, unquote
from logging import Logger
from ..util.helper import rate_limiting

from komand_sentinelone.util.helper import Helper, clean, sanitise_url
from komand_sentinelone.util.constants import (
    SERVICE_USER_HEADER_TOKEN_FIELD,
)
from komand_sentinelone.util.endpoints import (
    ACCOUNT_NAME_AVAILABLE_ENDPOINT,
    ACTIVITY_TYPES_ENDPOINT,
    AGENTS_ACTION_ENDPOINT,
    AGENTS_SUMMARY_ENDPOINT,
    AGENTS_SUPPORT_ACTION_ENDPOINT,
    ALERTS_ENDPOINT,
    ALERT_ANALYST_VERDICT_ENDPOINT,
    ALERT_INCIDENT_ENDPOINT,
    APPS_BY_AGENT_IDS_ENDPOINT,
    BLACKLIST_BY_CONTENT_HASH_ENDPOINT,
    BLOCKLIST_ENDPOINT,
    CANCEL_QUERY_ENDPOINT,
    CREATE_IOC_THREAT_ENDPOINT,
    CREATE_QUERY_ENDPOINT,
    DEVICE_CONTROL_EVENTS,
    DISABLE_AGENT_ENDPOINT,
    ENABLE_AGENT_ENDPOINT,
    FETCH_FILE_BY_AGENT_ID_ENDPOINT,
    GET_EVENTS_ENDPOINT,
    MARK_AS_BENIGN_ENDPOINT,
    MARK_AS_THREAT_ENDPOINT,
    MITIGATE_THREAT_ENDPOINT,
    RUN_REMOTE_SCRIPT_ENDPOINT,
    PROTECTED_ACTIONS_SESSION_ENDPOINT,
    QUERY_STATUS_ENDPOINT,
    SEARCH_AGENTS_ENDPOINT,
    SITES_ENDPOINT,
    THREATS_FETCH_FILE_ENDPOINT,
    THREAT_ANALYST_VERDICT_ENDPOINT,
    THREAT_INCIDENT_ENDPOINT,
    THREAT_SUMMARY_ENDPOINT,
)


class SentineloneAPI:
    def __init__(self, url: str, api_key: str, logger: Logger):
        self.url = self.split_url(url)
        self.api_key = api_key
        self.logger = logger
        self.api_version = "2.1"

    def apps_by_agent_ids(self, identifiers: str) -> list:
        return self._call_api("GET", APPS_BY_AGENT_IDS_ENDPOINT, params={"ids": identifiers})

    def agents_action(self, action: str, agents_filter: str) -> dict:
        return self._call_api(
            "POST",
            AGENTS_ACTION_ENDPOINT.format(action=action),
            json={"filter": agents_filter},
        )

    def agents_action_move_agent_to_new_site(self, agents_filter: dict, data: dict, action: str) -> dict:
        return self._call_api(
            "POST",
            AGENTS_ACTION_ENDPOINT.format(action=action),
            json={"filter": agents_filter, "data": data},
        )

    def agents_support_action(self, action: str, json_data: dict) -> dict:
        return self._call_api("POST", AGENTS_SUPPORT_ACTION_ENDPOINT.format(action=action), json=json_data)

    def blacklist_by_content_hash(self, hash_value: str) -> dict:
        self.logger.info(f"Attempting to blacklist file: {hash_value}")
        return self._call_api(
            "POST",
            BLACKLIST_BY_CONTENT_HASH_ENDPOINT,
            json={
                "filter": {"contentHashes": hash_value},
                "data": {"targetScope": "site"},
            },
        )

    def create_blacklist_item(self, blacklist_hash: str, description: str) -> bool:
        sites = self._call_api("GET", SITES_ENDPOINT).get("data", {}).get("sites", [])
        site_ids = []
        for site in sites:
            site_ids.append(site.get("id"))

        if self.get_existing_blacklist(blacklist_hash):
            self.logger.info(f"{blacklist_hash} has already been blacklisted.")
            return False
        else:
            for os_type in ["linux", "windows", "macos"]:
                self._call_api(
                    "POST",
                    BLOCKLIST_ENDPOINT,
                    json={
                        "data": {
                            "value": blacklist_hash,
                            "type": "black_hash",
                            "osType": os_type,
                            "description": description,
                        },
                        "filter": {"siteIds": site_ids},
                    },
                )
        return True

    def delete_blacklist_item_by_hash(self, item_ids: str) -> bool:
        self._call_api(
            "DELETE",
            BLOCKLIST_ENDPOINT,
            json={"data": {"type": "black_hash", "ids": item_ids}},
        )
        return True

    def get_all_paginated_results(self, endpoint: str, params: dict = {}) -> dict:
        results = self._call_api("GET", endpoint, params=params)
        all_result_data = results.get("data")
        next_cursor = results.get("pagination", {}).get("nextCursor", None)
        params["cursor"] = unquote(next_cursor) if next_cursor else None

        while next_cursor:
            next_page = self._call_api("GET", endpoint, params=params)
            all_result_data.extend(next_page.get("data", []))
            next_cursor = next_page.get("pagination", {}).get("nextCursor", None)
            params["cursor"] = unquote(next_cursor) if next_cursor else None
        results["data"] = all_result_data
        return results

    def get_events(self, params: dict, get_all_results: bool) -> dict:
        if get_all_results:
            return self.get_all_paginated_results(GET_EVENTS_ENDPOINT, params)
        return self._call_api("GET", GET_EVENTS_ENDPOINT, params=params)

    def get_device_control_events(
        self, params: dict, full_response: bool = False, raise_for_status: bool = True
    ) -> dict:
        return self._call_api(
            "GET",
            DEVICE_CONTROL_EVENTS,
            params=params,
            full_response=full_response,
            raise_for_status=raise_for_status,
        )

    def get_existing_blacklist(self, blacklist_hash: str) -> bool:
        ids = self.get_item_ids_by_hash(blacklist_hash)
        ids = Helper.join_or_empty(ids)
        if not ids:
            return False

        response = self._call_api(
            "GET",
            BLOCKLIST_ENDPOINT,
            params={
                "type": "black_hash",
                "ids": ids,
                "includeChildren": True,
                "includeParents": True,
            },
        )

        existing_os_types = []
        for blacklist_entry in response.get("data", []):
            existing_os_types.append(blacklist_entry.get("osType"))

        return set(existing_os_types) == {"linux", "windows", "macos"}

    def get_item_ids_by_hash(self, blacklist_hash: str) -> list:
        restrictions = self._call_api(
            "GET",
            BLOCKLIST_ENDPOINT,
            params={
                "type": "black_hash",
                "includeChildren": True,
                "includeParents": True,
                "value": blacklist_hash,
            },
        ).get("data", [])

        ids = []
        for restriction in restrictions:
            ids.append(restriction.get("id"))
        return ids

    def disable_agent(self, data: dict, agent_filter: dict) -> dict:
        return self._call_api("POST", DISABLE_AGENT_ENDPOINT, json={"data": data, "filter": agent_filter})

    def enable_agent(self, reboot: bool, agent_filter: dict) -> dict:
        return self._call_api(
            "POST",
            ENABLE_AGENT_ENDPOINT,
            json={"data": {"shouldReboot": reboot}, "filter": agent_filter},
        )

    def fetch_file_by_agent_id(self, agent_id: str, file_path: str, password: str) -> bool:
        response = self._call_api(
            "POST",
            FETCH_FILE_BY_AGENT_ID_ENDPOINT.format(agent_id=agent_id),
            json={"data": {"password": password, "files": [file_path]}},
        )
        if not response.get("errors", []):
            return True

        errors = "\n".join(response.get("errors"))
        raise PluginException(
            cause="An error occurred when trying to fetch file.",
            assistance="Check the error information and adjust inputs accordingly",
            data=errors,
        )

    def is_account_name_available(self, name: str) -> dict:
        return self._call_api("GET", ACCOUNT_NAME_AVAILABLE_ENDPOINT, params={"name": name})

    def mitigate_threat(self, threat_id: str, action: str) -> dict:
        return self._call_api(
            "POST",
            MITIGATE_THREAT_ENDPOINT.format(action=action),
            {"filter": {"ids": [threat_id]}},
        )

    def mark_as_benign(self, threat_id: str, whitening_option: str, target_scope: str) -> dict:
        # Mark as benign does not exist in v2.1
        return self._call_api(
            "POST",
            MARK_AS_BENIGN_ENDPOINT,
            json={
                "filter": {"ids": [threat_id]},
                "data": {
                    "whiteningOption": whitening_option,
                    "targetScope": target_scope,
                },
            },
            override_api_version="2.0",
        )

    def mark_as_threat(self, threat_id: str, whitening_option: str, target_scope: str) -> dict:
        # Mark as threat does not exist in v2.1
        return self._call_api(
            "POST",
            MARK_AS_THREAT_ENDPOINT,
            {
                "filter": {"ids": [threat_id]},
                "data": {
                    "whiteningOption": whitening_option,
                    "targetScope": target_scope,
                },
            },
            override_api_version="2.0",
        )

    def get_alerts(self, params: dict) -> dict:
        return self._call_api("GET", ALERTS_ENDPOINT, params=params)

    def get_threats(
        self,
        params: dict,
        api_version: str = "2.0",
        full_response: bool = False,
        raise_for_status: bool = True,
    ) -> dict:
        # GET /threats has different response schemas for 2.1 and 2.0
        # Use 2.0 endpoint to be consistent and support as many S1 consoles as possible
        return self._call_api(
            "GET",
            THREAT_SUMMARY_ENDPOINT,
            params=params,
            override_api_version=api_version,
            full_response=full_response,
            raise_for_status=raise_for_status,
        )

    def check_if_threats_exist(self, threat_ids: List[str]):
        threats = self.get_threats({"ids": threat_ids}, api_version="2.1")
        if not threats.get("data"):
            raise PluginException(
                cause="Invalid threat IDs provided.",
                assistance="Please provide valid threat ID and try again.",
            )

    def threats_fetch_file(self, password: str, agents_filter: dict) -> int:
        return self._call_api(
            "POST",
            THREATS_FETCH_FILE_ENDPOINT,
            {"data": {"password": password}, "filter": agents_filter},
        )

    def download_file(self, agent_filter: dict, fetch_date: str, password: str) -> dict:
        agent_filter["activityTypes"] = 86
        agent_filter["sortBy"] = "createdAt"
        agent_filter["sortOrder"] = "desc"
        agent_filter["createdAt__gt"] = fetch_date
        while True:
            activities = self.get_activities_list(agent_filter)
            if activities.get("data"):
                break
            self.logger.info("Waiting 5 seconds for successful threat file upload...")
            time.sleep(5)
        threat_details = activities.get("data", [{}])[0].get("data", {})
        file_url = threat_details.get("filePath", "")[1:]
        file_name = threat_details.get("fileDisplayName")
        sanitised_file_url = sanitise_url(file_url)
        response = self._call_api("GET", sanitised_file_url, full_response=True)
        try:
            with zipfile.ZipFile(io.BytesIO(response.content)) as downloaded_zipfile:
                downloaded_zipfile.setpassword(password.encode("UTF-8"))
                file_info = downloaded_zipfile.infolist()[-1]
                file_content = downloaded_zipfile.read(file_info.filename)

                return {
                    "filename": file_name,
                    "content": base64.b64encode(file_content).decode("utf-8"),
                }
        except Exception as error:
            raise PluginException(
                cause="An error occurred when trying to download file.",
                assistance="Please contact support or try again later.",
                data=error.args,
            )

    def get_activities_list(self, params: dict, full_response: bool = False, raise_for_status: bool = True) -> dict:
        return self._call_api(
            "GET",
            "activities",
            params=params,
            full_response=full_response,
            raise_for_status=raise_for_status,
        )

    def get_activity_types(self) -> dict:
        return self._call_api("GET", ACTIVITY_TYPES_ENDPOINT)

    def get_agents_summary(self, parameters: dict) -> dict:
        if self.api_version == "2.0":
            raise PluginException(
                cause="Endpoint not found.",
                assistance="This action is not supported in SentinelOne API v2.0. Verify that your SentinelOne console "
                "supports SentinelOne API v2.1 and try again.",
            )
        return self._call_api("GET", AGENTS_SUMMARY_ENDPOINT, params=parameters)

    def cancel_running_query(self, json_data: dict) -> dict:
        return self._call_api("POST", CANCEL_QUERY_ENDPOINT, json=json_data)

    def create_query(self, json_data: dict) -> dict:
        return self._call_api("POST", CREATE_QUERY_ENDPOINT, json=json_data)

    def get_query_status(self, parameters: dict) -> dict:
        return self._call_api("GET", QUERY_STATUS_ENDPOINT, params=parameters)

    def get_threat_summary(self) -> dict:
        params = {"limit": 1000}

        # API v2.0 and 2.1 have different responses -- revert to 2.0
        threats = self._call_api("GET", THREAT_SUMMARY_ENDPOINT, params=params, override_api_version="2.0")
        all_threads_data = threats.get("data")
        params["cursor"] = threats.get("pagination", {}).get("nextCursor")

        while params.get("cursor"):
            next_threats = self._call_api(
                "GET",
                THREAT_SUMMARY_ENDPOINT,
                params=params,
                override_api_version="2.0",
            )
            all_threads_data.extend(next_threats.get("data", []))
            params["cursor"] = next_threats.get("pagination", {}).get("nextCursor")
        threats["data"] = all_threads_data
        return threats

    def update_analyst_verdict(self, incident_type: str, json_data: dict) -> dict:
        if incident_type == "threats":
            return self._call_api("POST", THREAT_ANALYST_VERDICT_ENDPOINT, json=json_data)
        return self._call_api("POST", ALERT_ANALYST_VERDICT_ENDPOINT, json=json_data)

    def update_incident_status(self, incident_type: str, json_data: dict) -> dict:
        if incident_type == "threats":
            return self._call_api("POST", THREAT_INCIDENT_ENDPOINT, json=json_data)
        return self._call_api("POST", ALERT_INCIDENT_ENDPOINT, json=json_data)

    def validate_incidents(self, incidents_ids: list, incident_type: str, new_state: str, attribute: str) -> list:
        attribute_message = "analyst verdict" if attribute == "analystVerdict" else "incident status"
        if not incidents_ids:
            raise PluginException(
                cause="No incident IDs were provided.",
                assistance="Please provide incident IDs and try again.",
            )
        incidents = self.remove_non_existing_incidents(list(set(incidents_ids)), incident_type)
        incidents = self.validate_incident_state(incidents, incident_type, new_state, attribute)
        if not incidents:
            raise PluginException(
                cause=f"No {incident_type} to update in SentinelOne.",
                assistance=f"Please verify the log, the {incident_type} are already set to the new {attribute_message} "
                "or do not exist in SentinelOne.",
            )
        return incidents

    def remove_non_existing_incidents(self, incident_ids: list, incident_type: str) -> list:
        incident_ids_copy = incident_ids.copy()
        for incident_id in incident_ids:
            response_data = self.get_incident(incident_id, incident_type).get("data", [])
            if isinstance(response_data, list) and len(response_data) == 0:
                self.logger.info(f"Incident {incident_id} was not found.")
                incident_ids_copy.remove(incident_id)
        return incident_ids_copy

    def validate_incident_state(self, incident_ids: list, incident_type: str, new_state: str, attribute: str) -> list:
        incident_ids_copy = incident_ids.copy()
        for incident_id in incident_ids:
            response_data = self.get_incident(incident_id, incident_type).get("data", [])
            for incident in response_data:
                if incident_type == "threats":
                    object_name = "threatInfo"
                    resp_incident_id = incident.get("id")
                else:
                    object_name = "alertInfo"
                    resp_incident_id = incident.get(object_name, {}).get("alertId")

                attribute_name = "analystVerdict" if attribute == "analystVerdict" else "incidentStatus"
                if resp_incident_id == incident_id and incident.get(object_name, {}).get(attribute_name) == new_state:
                    self.logger.info(f"Incident {incident_id} has the {attribute_name} already set to {new_state}.")
                    incident_ids_copy.remove(incident_id)
        return incident_ids_copy

    def get_incident(self, incident_id: str, incident_type: str) -> dict:
        params = {"ids": [incident_id]}
        if incident_type == "threats":
            return self.get_threats(params, api_version="2.1")
        return self.get_alerts(params)

    def run_remote_script(self, json_data: dict) -> dict:
        return self._call_api("POST", RUN_REMOTE_SCRIPT_ENDPOINT, json=json_data)

    def elevate_protected_actions_session(self, json_data: dict) -> dict:
        return self._call_api("POST", PROTECTED_ACTIONS_SESSION_ENDPOINT, json=json_data)

    def create_ioc_threat(self, json_data: dict) -> dict:
        return self._call_api("POST", CREATE_IOC_THREAT_ENDPOINT, json=json_data)

    @staticmethod
    def raise_for_status(response: requests.Response):
        if response.status_code == 401:
            raise PluginException(
                preset=PluginException.Preset.API_KEY,
                data=response.text,
            )
        elif response.status_code == 403:
            raise PluginException(
                preset=PluginException.Preset.UNAUTHORIZED,
                data=response.text,
            )
        elif response.status_code == 404:
            raise PluginException(
                cause="Resource not found.",
                assistance="Please provide valid inputs and try again.",
                data=response.text,
            )
        elif response.status_code == 400:
            raise PluginException(
                preset=PluginException.Preset.BAD_REQUEST,
                data=response.text,
            )
        elif response.status_code == 429:
            raise PluginException(
                preset=PluginException.Preset.RATE_LIMIT,
                data=response.text,
            )
        elif 400 < response.status_code < 500:
            raise PluginException(
                preset=PluginException.Preset.UNKNOWN,
                data=response.text,
            )
        elif response.status_code == 503:
            raise PluginException(
                preset=PluginException.Preset.SERVICE_UNAVAILABLE,
                data=response.text,
            )
        elif response.status_code >= 500:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=response.text,
            )

    def make_headers(self) -> dict:
        return {
            "Authorization": f"{SERVICE_USER_HEADER_TOKEN_FIELD} {self.api_key}",
            "Content-Type": "application/json",
        }

    @rate_limiting(10)
    def _call_api(
        self,
        method: str,
        endpoint: str,
        json: dict = None,
        params: dict = None,
        full_response: bool = False,
        override_api_version: str = "",
        raise_for_status: bool = True,
    ):
        # We prefer to use the same api version from the token creation,
        # But some actions require 2.0 and not 2.1 (and vice versa), in that case just pass in the right version
        api_version, json, params = self.clean_call_inputs(override_api_version, json, params)

        try:
            response = requests.request(
                method,
                f"{self.url}web/api/v{api_version}/{endpoint}",
                json=json,
                params=params,
                headers=self.make_headers(),
            )
            if raise_for_status:
                self.raise_for_status(response)
            if full_response:
                return response
            return response.json()
        except JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.SSLError,
        ) as error:
            raise PluginException(
                data=error,
                cause=PluginException.causes.get(PluginException.Preset.CONNECTION_ERROR),
                assistance="Please ensure your connection details are correct and your SentinelOne instance accessible.",
            )
        except requests.exceptions.RequestException as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def clean_call_inputs(
        self, override_api_version: str = None, json: str = None, params: str = None
    ) -> Tuple[str, str, str]:
        api_version = self.api_version
        if override_api_version:
            api_version = override_api_version
        if json:
            json = insightconnect_plugin_runtime.helper.clean(json)
        if params:
            params = insightconnect_plugin_runtime.helper.clean(params)
        return api_version, json, params

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
        return f"{scheme}://{netloc}/"

    def get_agents_data(
        self,
        agent: str,
        api_version: str,
        search: str,
        agent_active: bool,
        results: List[Dict[str, Any]],
    ) -> None:
        """
        Gets agents Data
        :param agent: Agent to get details for
        :type: str

        :param api_version: Version of API
        :type: str

        :param search: String that will be searched for
        :type: str

        :param agent_active: If the Agent is Active
        :type: bool

        :param results: Array containing agent results
        :type: List[Dict[str, Any]]
        """
        params = {search: agent, "isActive": agent_active}
        output = self._call_api(
            "GET",
            SEARCH_AGENTS_ENDPOINT,
            params=params,
            override_api_version=api_version,
        )
        for agent_data in output.get("data", []):
            if agent_data not in results:
                results.append(agent_data)

    def search_agents(
        self,
        agent_details: str,
        agent_active: bool = None,
        operational_state: str = None,
        api_version: str = "2.1",
    ) -> List[Dict[str, Any]]:
        """
        Searches for agents
        :param agent_details: Details of agent
        :type: str

        :param agent_active: If the Agent is Active
        :type: bool

        :param operational_state: If in Operational states
        :type: bool

        :param api_version: API Version
        :type: str

        :return: self.clean(results)
        :rtype: List[Dict[str, Any]]
        """
        results = []
        if agent_details:
            for search in self.__get_searches(agent_details):
                self.get_agents_data(agent_details, api_version, search, agent_active, results)
        else:
            output = self._call_api(
                "GET",
                SEARCH_AGENTS_ENDPOINT,
                params={"isActive": agent_active},
                override_api_version=api_version,
            )
            results.extend(output.get("data", []))
        if operational_state and operational_state != "Any":
            return clean([agent for agent in results if agent.get("operationalState") == operational_state])
        else:
            return clean(results)

    def get_agent_uuid(self, agent: str) -> str:
        """
        Get Agent UUID
        :param agent: The Agent
        :type: str

        :return agent_uuid: The agent UUID
        :rtype: str
        """
        agents = self.search_agents(agent, api_version="2.1")
        if self.__check_agents_found(agents):
            raise PluginException(
                cause=f"No agents found for: {agent}.",
                assistance="Please check provided information and try again.",
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
        if len(agent_details) == 19 and agent_details.isdigit():
            return ["ids"]
        if match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", agent_details):
            return ["networkInterfaceInet__contains", "externalIp__contains"]
        if match(r"((?:(\d{1,2}|[a-fA-F]{1,2}){2})(?::|-*)){6}", agent_details):
            return ["networkInterfacePhysical__contains", "uuid"]
        else:
            return ["computerName"]

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
                assistance="Please provide a unique agent identifier so the action can be performed on the intended "
                "agent.",
            )
        if len(agents) == 0:
            return True
        return False
