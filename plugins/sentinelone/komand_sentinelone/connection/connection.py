import base64
import io
import time
import zipfile

import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from typing import Tuple
from datetime import datetime, timedelta, timezone

from komand_sentinelone.util.api import SentineloneAPI
from komand_sentinelone.util.helper import Helper
from .schema import ConnectionSchema, Input
from komand_sentinelone.util.constants import (
    DATA_FIELD,
    API_TOKEN_FIELD,
    CONSOLE_USER_HEADER_TOKEN_FIELD,
    SERVICE_USER_HEADER_TOKEN_FIELD,
    SERVICE_USER_TYPE,
)


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.url = None
        self.api_version = None
        self.api_key = None
        self.token = None
        self.user_type = None
        self.header = None

    def connect(self, params={}):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        self.logger.info("Connect: Connecting...")
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.url = params.get(Input.URL)
        self.user_type = params.get(Input.USER_TYPE)

        index = self.url.find("/", self._get_start_index(self.url))
        if index >= 0:
            self.url = self.url[:index]

        # Add trailing slash if needed
        if not self.url.endswith("/"):
            self.url = self.url + "/"

        self.token, self.api_version = self.get_auth_token()
        self.client = SentineloneAPI(self.url, self.make_token_header())
        self.logger.info("Token: " + "*************" + str(self.token[len(self.token) - 5 : len(self.token)]))

    @staticmethod
    def _get_start_index(url):
        if url.startswith("https://"):
            return 9
        return 0

    def get_auth_token(self) -> Tuple[str, str]:
        version = "2.1"
        if self.user_type == SERVICE_USER_TYPE:
            return self.api_key, version
        request_url = self._prepare_auth_url_based_on_version(version)
        request_data = self._prepare_body_for_auth_request()
        self.logger.info(f"Trying to authenticate with API version {version}")
        response = requests.post(request_url, json=request_data)
        self._handle_auth_response(request_url, response)

        if response.status_code == 200:
            token = response.json().get(DATA_FIELD).get("token")
        else:
            version = "2.0"
            self.logger.info(f"API v2.1 failed... trying v{version}")
            request_url = self._prepare_auth_url_based_on_version(version)
            response = requests.post(request_url, json=request_data)
            self._handle_auth_response(request_url, response)
            token = response.json().get(DATA_FIELD).get("token")
            # We know the connection failed when both 2.1 and 2.0 do not give 200 responses
            if not token:
                raise ConnectionTestException(
                    cause=f"Could not authorize with SentinelOne instance at: {self.url}.",
                    assistance="An attempt was made to connect using a version of the API 2.0 and 2.1. "
                    "Check the inputs params and try again. "
                    "If the problem persists contact with development team.",
                )

        return token, version

    def _handle_auth_response(self, url: str, response):
        if response.status_code == 401:
            raise ConnectionTestException(
                cause=f"Could not authorize with SentinelOne instance at: {url}.",
                assistance="User authentication failed. Check your input for connection and try again.",
                data=response.json(),
            )
        elif response.status_code == 400:
            raise PluginException(
                cause=f"Could not authorize with SentinelOne instance at: {url}.",
                assistance="Invalid user input received. Check the response to get error information.",
                data=response.json(),
            )

    def _prepare_auth_url_based_on_version(self, version: str) -> str:
        url = f"{self.url}web/api/v{version}/users/login"
        return f"{url}/by-api-token"

    def _prepare_body_for_auth_request(self):
        if self.api_key:
            return {DATA_FIELD: {API_TOKEN_FIELD: self.api_key}}
        else:
            raise PluginException(
                cause="Inputs related to API key authentication is invalid.",
                assistance="Check API key input and try again. "
                "If the problem persists contact with development team.",
            )

    def make_token_header(self):
        if self.user_type == SERVICE_USER_TYPE:
            token_field = SERVICE_USER_HEADER_TOKEN_FIELD
        else:
            token_field = CONSOLE_USER_HEADER_TOKEN_FIELD

        self.header = {
            "Authorization": f"{token_field} {self.token}",
            "Content-Type": "application/json",
        }
        return self.header

    def activities_list(self, parameters):
        return self._call_api("GET", "activities", None, parameters)

    def name_available(self, name):
        return self._call_api("GET", "private/accounts/name-available", None, {"name": name})

    def activities_types(self):
        return self._call_api("GET", "activities/types")

    def ad_settings(self, parameters):
        return self._call_api("GET", "settings/active-directory", None, parameters)

    def agent_info(self, identifier: str):
        return self._call_api("GET", "settings/active-directory", None, {"id": identifier})

    def apps_by_agent_ids(self, identifiers: str):
        return self._call_api("GET", "agents/applications", None, {"ids": identifiers})

    def agents_summary(self, site_ids, account_ids):
        return self._call_api(
            "GET",
            "private/agents/summary",
            None,
            {"siteIds": site_ids, "accountIds": account_ids},
        )

    def agents_action(self, action: str, agents_filter: str):
        return self._call_api("POST", f"agents/actions/{action}", {"filter": agents_filter})

    def agents_action(self, action: str, agents_filter: str):
        return self._call_api("POST", f"agents/actions/{action}", {"filter": agents_filter})

    def fetch_file_by_agent_id(self, agent_id: str, file_path: str, password: str):
        response =  self._call_api(
            "POST", f"agents/{agent_id}/actions/fetch-files", {"data": {"password": password, "files": [file_path]}}
        )
        if len(response.get("errors", [])) == 0:
            return True

        errors = "\n".join(response.get("errors"))
        raise PluginException(
            cause="An error occurred when trying to fetch file.",
            assistance=f"Check the error information and adjust inputs accordingly",
            data=errors
        )

    def run_remote_script(self, user_filter: dict, data: dict) -> dict:
        endpoint = "remote-scripts/execute"
        response = self._call_api(
            "POST",
            endpoint,
            {"filter": user_filter, "data": data},
        )
        affected = 0
        if len(response.get("errors", [])) == 0:
            returned_data = response.get("data", [])
            if returned_data:
                affected = returned_data["affected"]
            return affected

        errors = "\n".join(response.get("errors"))
        raise PluginException(
            cause="An error occurred when trying to fetch file.",
            assistance=f"Check the error information and adjust inputs accordingly",
            data=errors
        )

    def download_file(self, agent_filter: dict, password: str):
        self.get_auth_token()
        agent_filter["activityTypes"] = 86
        agent_filter["sortBy"] = "createdAt"
        agent_filter["sortOrder"] = "desc"
        activities = self.activities_list(agent_filter)
        while not activities["data"]:
            self.logger.info("Waiting 5 seconds for successful threat file upload...")
            time.sleep(5)
            activities = self.activities_list(agent_filter)
        self.get_auth_token()
        response = self._call_api("GET", activities["data"][0]["data"]["filePath"][1:], full_response=True)
        try:
            file_name = activities["data"][-1]["data"]["fileDisplayName"]
            with zipfile.ZipFile(io.BytesIO(response.content)) as downloaded_zipfile:
                downloaded_zipfile.setpassword(password.encode("UTF-8"))

                return {
                    "filename": file_name,
                    "content": base64.b64encode(downloaded_zipfile.read(downloaded_zipfile.infolist()[-1])).decode(
                        "utf-8"
                    ),
                }
        except KeyError:
            raise PluginException(
                cause="An error occurred when trying to download file.",
                assistance="Please contact support or try again later.",
            )

    def threats_fetch_file(self, password: str, agents_filter: dict) -> int:
        self.get_auth_token()
        return self._call_api("POST", "threats/fetch-file", {"data": {"password": password}, "filter": agents_filter})

    def agents_support_action(self, action: str, agents_filter: str, module: str):
        return self._call_api(
            "POST", f"private/agents/support-actions/{action}", {"filter": agents_filter, "data": {"module": module}}
        )

    def get_threat_summary(self, limit: int = 1000):
        first_page_endpoint = f"threats?limit={limit}"

        # API v2.0 and 2.1 have different responses -- revert to 2.0
        threats = self._call_api("GET", first_page_endpoint, override_api_version="2.0")
        all_threads_data = threats["data"]
        next_cursor = threats.get("pagination", {}).get("nextCursor")

        while next_cursor:
            next_threats = self._call_api(
                "GET", f"{first_page_endpoint}&cursor={next_cursor}", override_api_version="2.0"
            )
            all_threads_data += next_threats["data"]
            next_cursor = next_threats["pagination"]["nextCursor"]

        threats["data"] = all_threads_data
        return threats

    def blacklist_by_content_hash(self, hash_value: str):
        endpoint = f"{self.url}web/api/v{self.api_version}/threats/add-to-blacklist"
        self.logger.info("Attempting to blacklist file: " + hash_value)
        self.logger.info("Using endpoint: " + endpoint)

        headers = self.make_token_header()
        body = {"filter": {"contentHashes": hash_value}, "data": {"targetScope": "site"}}

        results = requests.post(endpoint, json=body, headers=headers)
        if results.status_code != 200:
            raise PluginException(cause="Could not blacklist file hash.", assistance=f"Result was: {results.text}")

        return results.json()

    def create_ioc_threat(self, hash_, group_id, path, agent_id, note=""):
        body = {
            "data": [
                {
                    "hash": hash_,
                    "groupId": group_id,
                    "path": path,
                    "agentId": agent_id,
                    "note": note,
                }
            ]
        }
        response = self._call_api("POST", "private/threats/ioc-create-threats", body, full_response=True)

        return response.json()["data"]["affected"]

    def mitigate_threat(self, threat_id, action):
        body = {"filter": {"ids": [threat_id]}}
        action_url = "threats/mitigate/" + action
        return self._call_api("POST", action_url, body)["data"]["affected"]

    def mark_as_benign(self, threat_id, whitening_option, target_scope):
        body = {
            "filter": {"ids": [threat_id]},
            "data": {"whiteningOption": whitening_option, "targetScope": target_scope},
        }
        # Mark as threat does not exist in v2.1
        return self._call_api("POST", "threats/mark-as-benign", body, override_api_version="2.0")["data"]["affected"]

    def mark_as_threat(self, threat_id, whitening_option, target_scope):
        body = {
            "filter": {"ids": [threat_id]},
            "data": {"whiteningOption": whitening_option, "targetScope": target_scope},
        }

        # Mark as threat does not exist in v2.1
        return self._call_api("POST", "threats/mark-as-threat", body, override_api_version="2.0")["data"]["affected"]

    def get_threats(self, params: dict, api_version: str = "2.0") -> dict:
        # GET /threats has different response schemas for 2.1 and 2.0
        # Use 2.0 endpoint to be consistent and support as many S1 consoles as possible
        return self._call_api("GET", "threats", params=params, override_api_version=api_version)

    def get_alerts(self, params: dict) -> dict:
        return self._call_api("GET", "cloud-detection/alerts", params=params)

    def create_blacklist_item(self, blacklist_hash: str, description: str):
        sites = self._call_api("GET", "sites").get("data", {}).get("sites", [])
        site_ids = []
        for site in sites:
            site_ids.append(site.get("id"))
        errors = []

        already_blacklisted = self.get_existing_blacklist(blacklist_hash)

        if already_blacklisted:
            self.logger.info(f"{blacklist_hash} has already been blacklisted.")
        else:
            for os_type in ["linux", "windows", "macos"]:
                errors.extend(
                    self._call_api(
                        "POST",
                        "restrictions",
                        json={
                            "data": {
                                "value": blacklist_hash,
                                "type": "black_hash",
                                "osType": os_type,
                                "description": description,
                            },
                            "filter": {"siteIds": site_ids},
                        },
                    ).get("errors", [])
                )

        return errors

    def get_existing_blacklist(self, blacklist_hash: str):
        ids = self.get_item_ids_by_hash(blacklist_hash)
        ids = Helper.join_or_empty(ids)
        if not ids:
            return False

        response = self._call_api(
            "GET",
            "restrictions",
            params={
                "type": "black_hash",
                "ids": ids,
            },
        )

        existing_os_types = []
        for blacklist_entry in response.get("data", []):
            existing_os_types.append(blacklist_entry.get("osType"))

        return set(existing_os_types) == {"linux", "windows", "macos"}

    def get_item_ids_by_hash(self, blacklist_hash: str):
        response = self._call_api(
            "GET",
            "restrictions",
            params={"type": "black_hash", "includeChildren": True, "includeParents": True, "value": blacklist_hash},
        )

        if len(response.get("errors", [])) == 0:
            ids = []
            restrictions = response.get("data", [])
            for restriction in restrictions:
                ids.append(restriction.get("id"))
            return ids

        errors = "\n".join(response.get("errors"))

        raise PluginException(
            cause="An error occurred when trying to unblacklist.",
            assistance=f"The following error(s) occurred: {errors}",
        )

    def delete_blacklist_item_by_hash(self, item_ids: str):
        return self._call_api(
            "DELETE",
            "restrictions",
            json={"data": {"type": "black_hash", "ids": item_ids}},
        ).get("errors", [])

    def disable_agent(self, data: dict, agent_filter: dict) -> dict:
        return self._call_api("POST", "agents/actions/disable-agent", json={"data": data, "filter": agent_filter})

    def enable_agent(self, reboot: bool, agent_filter: dict) -> dict:
        return self._call_api(
            "POST", "agents/actions/enable-agent", json={"data": {"shouldReboot": reboot}, "filter": agent_filter}
        )

    def create_query(self, payload: dict) -> dict:
        return self._call_api("POST", "dv/init-query", json=payload)

    def cancel_running_query(self, query_id: str) -> dict:
        return self._call_api("POST", "dv/cancel-query", json={"queryId": query_id})

    def get_query_status(self, query_id: str) -> dict:
        return self._call_api("GET", "dv/query-status", params={"queryId": query_id})

    def get_events(self, params: dict, get_all_results: bool, event_type: str = None) -> dict:
        endpoint = "dv/events"
        if event_type:
            endpoint = endpoint + f"/{event_type}"
        if get_all_results:
            return insightconnect_plugin_runtime.helper.clean(self.get_all_paginated_results(endpoint, params=params))

        return insightconnect_plugin_runtime.helper.clean(self._call_api("GET", endpoint, params=params))

    def update_analyst_verdict(self, incident_ids: list, analyst_verdict: str, _type: str) -> dict:
        if _type == "threats":
            endpoint = "threats/analyst-verdict"
        else:
            endpoint = "cloud-detection/alerts/analyst-verdict"

        return self._call_api(
            "POST",
            endpoint,
            {"filter": {"ids": incident_ids}, "data": {"analystVerdict": analyst_verdict}},
        )

    def update_incident_status(self, incident_ids: list, incident_status: str, _type: str) -> dict:
        if _type == "threats":
            endpoint = "threats/incident"
        else:
            endpoint = "cloud-detection/alerts/incident"

        return self._call_api(
            "POST",
            endpoint,
            {"filter": {"ids": incident_ids}, "data": {"incidentStatus": incident_status}},
        )

    def remove_non_existing_incidents(self, incident_ids: list, _type: str) -> list:
        """
        This function checks each incident ID in the provided list
        of incident IDs, against the SentinelOne instance, to see
        if they exist. Only incident IDs that do exist within that
        instance are returned.
        @param incident_ids: list of incidents IDs to check if they
        exist in the SentinelOne instance
        @param _type: type of the incident - either 'threats' or
        'alerts'
        @return: returns a list of incident IDs that exist in the
        SentinelOne instance
        """
        incident_ids_copy = incident_ids.copy()
        for incident_id in incident_ids:
            response_data = self.get_incident(incident_id, _type).get("data")
            if isinstance(response_data, list) and len(response_data) == 0:
                self.logger.info(f"Incident {incident_id} was not found.")
                incident_ids_copy.remove(incident_id)

        return incident_ids_copy

    def validate_incident_state(self, incident_ids: list, _type: str, new_state: str, attribute: str) -> list:
        """
        This function checks each incident ID in the provided list
        of incident IDs, against the SentinelOne instance, validating
        that the current value of a certain attribute (either
        'analystVerdict' or 'incidentStatus') of the incident is
        different to the 'new_state' attribute. Only incident IDs that
        have different status are returned.
        @param incident_ids: list of incidents IDs to validate the
        status of in the SentinelOne instance
        @param _type: type of the incident - either 'threats' or
        'alerts'
        @param new_state: the new state of the incident we wish to
        update the incident status on
        @param attribute: attribute to update, either 'analystVerdict'
        or 'incidentStatus'
        @return: returns a list of incidents that have different status
        compared to the `new_state` argument
        """
        for incident_id in incident_ids:
            response_data = self.get_incident(incident_id, _type).get("data")
            for incident in response_data:
                if _type == "threats":
                    object_name = "threatInfo"
                    resp_incident_id = incident.get("id")
                else:
                    object_name = "alertInfo"
                    resp_incident_id = incident.get(object_name, {}).get("alertId")

                attribute_name = "analystVerdict" if attribute == "analystVerdict" else "incidentStatus"
                if resp_incident_id == incident_id and incident.get(object_name, {}).get(attribute_name) == new_state:
                    self.logger.info(f"Incident {incident_id} has the {attribute_name} already set to {new_state}.")
                    incident_ids.remove(incident_id)

        return incident_ids

    def get_incident(self, incident_id: str, _type: str) -> dict:
        params = {"ids": [incident_id]}
        if _type == "threats":
            response = self.get_threats(params, api_version="2.1")
        else:
            response = self.get_alerts(params)

        return response

    def get_all_paginated_results(
        self,
        endpoint: str,
        limit: int = 1000,
        json: dict = None,
        params: dict = None,
    ) -> dict:
        first_endpoint_page = f"{endpoint}?limit={limit}"
        results = self._call_api("GET", first_endpoint_page, json, params)
        all_result_data = results["data"]

        try:
            next_cursor = results["pagination"]["nextCursor"]
        except KeyError:
            return results

        while next_cursor:
            next_page = self._call_api("GET", f"{first_endpoint_page}&cursor={next_cursor}")
            all_result_data += next_page["data"]
            try:
                next_cursor = next_page["pagination"]["nextCursor"]
            except KeyError:
                next_cursor = False

        results["data"] = all_result_data
        return results

    def _call_api(
        self,
        method,
        endpoint,
        json=None,
        params=None,
        full_response: bool = False,
        override_api_version: str = "",
    ):
        # We prefer to use the same api version from the token creation,
        # But some actions require 2.0 and not 2.1 (and vice versa), in that case just pass in the right version
        api_version = self.api_version
        if override_api_version:
            api_version = override_api_version
        endpoint = self.url + f"web/api/v{api_version}/" + endpoint

        headers = self.make_token_header()

        if json:
            json = insightconnect_plugin_runtime.helper.clean(json)
        if params:
            params = insightconnect_plugin_runtime.helper.clean(params)

        response = requests.request(method, endpoint, json=json, params=params, headers=headers)

        try:
            response.raise_for_status()
            if full_response:
                return response

            return response.json()
        except requests.HTTPError:
            raise PluginException(cause="API call failed: " + response.text)

    def test(self):
        self.get_auth_token()
