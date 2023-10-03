import base64
import io
import time
import zipfile
from json import dumps, loads
from json.decoder import JSONDecodeError
from re import match
import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean_list, clean_dict
from typing import List, Any, Dict, Tuple
from urllib.parse import urlsplit
from logging import Logger
import requests
from komand_sentinelone.util.constants import (
    DATA_FIELD,
    API_TOKEN_FIELD,
    CONSOLE_USER_HEADER_TOKEN_FIELD,
    SERVICE_USER_HEADER_TOKEN_FIELD,
    SERVICE_USER_TYPE,
)
from komand_sentinelone.util.endpoints import (
    ACTIVITY_TYPES_ENDPOINT,
    AGENTS_SUMMARY_ENDPOINT,
    CANCEL_QUERY_ENDPOINT,
    CREATE_QUERY_ENDPOINT,
    LOGIN_BY_TOKEN_ENDPOINT,
    ACCOUNT_NAME_AVAILABLE_ENDPOINT,
    MITIGATE_THREAT_ENDPOINT,
    MARK_AS_BENIGN_ENDPOINT,
    MARK_AS_THREAT_ENDPOINT,
    QUERY_STATUS_ENDPOINT,
    APPS_BY_AGENT_IDS_ENDPOINT,
    FETCH_FILE_BY_AGENT_ID_ENDPOINT,
    THREAT_SUMMARY_ENDPOINT,
)

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
    def __init__(self, url: str, make_token_header, api_key: str, user_type: str, logger: Logger):
        self.url = self.split_url(url)
        self._api_key = api_key
        self.user_type = user_type
        self.logger = logger
        self._token, self.api_version = self._get_auth_token()
        self.token_header = make_token_header

    def apps_by_agent_ids(self, identifiers: str) -> list:
        return self._call_api("GET", APPS_BY_AGENT_IDS_ENDPOINT, params={"ids": identifiers})

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
        return self._call_api("POST", MITIGATE_THREAT_ENDPOINT.format(action=action), {"filter": {"ids": [threat_id]}})

    def mark_as_benign(self, threat_id: str, whitening_option: str, target_scope: str) -> dict:
        # Mark as benign does not exist in v2.1
        return self._call_api(
            "POST",
            MARK_AS_BENIGN_ENDPOINT,
            json={
                "filter": {"ids": [threat_id]},
                "data": {"whiteningOption": whitening_option, "targetScope": target_scope},
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
                "data": {"whiteningOption": whitening_option, "targetScope": target_scope},
            },
            override_api_version="2.0",
        )

    def get_threats(self, params: dict, api_version: str = "2.0") -> dict:
        # GET /threats has different response schemas for 2.1 and 2.0
        # Use 2.0 endpoint to be consistent and support as many S1 consoles as possible
        return self._call_api("GET", "threats", params=params, override_api_version=api_version)

    def check_if_threats_exist(self, threat_ids: List[str]):
        threats = self.get_threats({"ids": threat_ids}, api_version="2.1")
        if not threats.get("data"):
            raise PluginException(
                cause="Invalid threat IDs provided.", assistance="Please provide valid threat ID and try again."
            )

    def threats_fetch_file(self, password: str, agents_filter: dict) -> int:
        return self._call_api("POST", "threats/fetch-file", {"data": {"password": password}, "filter": agents_filter})

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
        response = self._call_api("GET", file_url, full_response=True)
        try:
            with zipfile.ZipFile(io.BytesIO(response.content)) as downloaded_zipfile:
                downloaded_zipfile.setpassword(password.encode("UTF-8"))

                return {
                    "filename": file_name,
                    "content": base64.b64encode(downloaded_zipfile.read(downloaded_zipfile.infolist()[-1])).decode(
                        "utf-8"
                    ),
                }
        except Exception as error:
            raise PluginException(
                cause="An error occurred when trying to download file.",
                assistance="Please contact support or try again later.",
                data=error.args,
            )

    def get_activities_list(self, params: dict) -> dict:
        return self._call_api("GET", "activities", params=params)

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
            next_threats = self._call_api("GET", THREAT_SUMMARY_ENDPOINT, params=params, override_api_version="2.0")
            all_threads_data.extend(next_threats.get("data", []))
            params["cursor"] = next_threats.get("pagination", {}).get("nextCursor")
        threats["data"] = all_threads_data
        return threats

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
        elif response.status_code >= 500:
            raise PluginException(
                preset=PluginException.Preset.SERVER_ERROR,
                data=response.text,
            )

    def _get_auth_token(self) -> Tuple[str, str]:
        version = "2.1"
        if self.user_type == SERVICE_USER_TYPE:
            return self._api_key, version
        request_data = {DATA_FIELD: {API_TOKEN_FIELD: self._api_key}}
        self.logger.info(f"Trying to authenticate with API version {version}")
        response = requests.post(
            f"{self.url}{LOGIN_BY_TOKEN_ENDPOINT.format(version=version)}", json=request_data, timeout=60
        )
        self.raise_for_status(response)

        if response.status_code == 200:
            token = response.json().get(DATA_FIELD, {}).get("token")
        else:
            version = "2.0"
            self.logger.info(f"API v2.1 failed... trying v{version}")
            response = requests.post(
                f"{self.url}{LOGIN_BY_TOKEN_ENDPOINT.format(version=version)}", json=request_data, timeout=60
            )
            self.raise_for_status(response)
            token = response.json().get(DATA_FIELD, {}).get("token")
            # We know the connection failed when both 2.1 and 2.0 do not give 200 responses
            if not token:
                raise PluginException(
                    cause=f"Could not authorize with SentinelOne instance at: {self.url}.",
                    assistance="An attempt was made to connect using a version of the API 2.0 and 2.1. "
                    "Check the inputs params and try again. If the problem persists contact with development team.",
                )
        return token, version

    def make_headers(self) -> dict:
        if self.user_type == SERVICE_USER_TYPE:
            token_field = SERVICE_USER_HEADER_TOKEN_FIELD
        else:
            token_field = CONSOLE_USER_HEADER_TOKEN_FIELD
        return {
            "Authorization": f"{token_field} {self._token}",
            "Content-Type": "application/json",
        }

    def _call_api(
        self,
        method: str,
        endpoint: str,
        json: dict = None,
        params: dict = None,
        full_response: bool = False,
        override_api_version: str = "",
    ):
        # We prefer to use the same api version from the token creation,
        # But some actions require 2.0 and not 2.1 (and vice versa), in that case just pass in the right version
        api_version = self.api_version
        if override_api_version:
            api_version = override_api_version
        if json:
            json = insightconnect_plugin_runtime.helper.clean(json)
        if params:
            params = insightconnect_plugin_runtime.helper.clean(params)

        try:
            response = requests.request(
                method,
                f"{self.url}web/api/v{api_version}/{endpoint}",
                json=json,
                params=params,
                headers=self.make_headers(),
            )
            self.raise_for_status(response)
            if full_response:
                return response
            return response.json()
        except JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
        return f"{scheme}://{netloc}/"

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
