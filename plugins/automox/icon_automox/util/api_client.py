from insightconnect_plugin_runtime.exceptions import PluginException
import io
import json
import requests
from typing import Dict, List, Optional, Collection


class ApiClient:
    INTEGRATION_NAME = "rapid7-insightconnect-plugin"
    VERSION = "2.0.0"
    PAGE_SIZE = 500

    OUTCOME_FAIL = "failure"
    OUTCOME_SUCCESS = "success"

    def __init__(self, logger, api_key, endpoint="https://console.automox.com/api"):
        self.endpoint = endpoint
        self.api_key = api_key
        self.session = requests.session()

        # Define headers for client
        self.set_headers()

        # Define logger
        self.logger = logger

    def set_headers(self) -> None:
        self.session.headers = {
            "Authorization": "Bearer " + self.api_key,
            "User-Agent": f"ax:automox-{ApiClient.INTEGRATION_NAME}/{ApiClient.VERSION}",
            "content-type": "application/json",
        }

    def _call_api(self, method: str, url: str, params=None, json_data: object = None) -> Optional[dict]:
        if params is None:
            params = {}
        try:
            response = self.session.request(method, url, json=json_data, params=params)
            self.logger.info(f"Request URL: {url}, Method: {method}, Response code: {response.status_code}")
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)

            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)

            if response.status_code == 204:
                return

            if response.status_code == 202:
                return

            if 200 <= response.status_code < 300:
                return response.json()

            # Non-success and unknown
            raise PluginException(
                cause=f"An error occurred when making {method} request to {url}.",
                assistance=f"Response code: {response.status_code}, Content: {response.text}.",
            )
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Automox Console API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _page_results(self, url: str, params=None, sanitize: bool = True) -> [dict]:
        if params is None:
            params = {}
        params = self.first_page(params)

        page_resp = []

        while True:
            resp = self._call_api("GET", url, params)
            if sanitize:
                resp = self.remove_null_values(resp)

            page_resp.extend(resp)

            self.logger.info(f"Page {params.get('page')} result count: {len(resp)}")

            if len(resp) < self.PAGE_SIZE:
                break

            self.next_page(params)

        return page_resp

    def _page_results_data(self, url: str, params=None) -> [dict]:
        if params is None:
            params = {}
        params = self.first_page(params)

        page_resp = []

        while True:
            print(url)
            resp = self._call_api("GET", url, params)
            resp_data = self.remove_null_values(resp.get("data"))

            page_resp.extend(resp_data)

            self.logger.info(f"Page {params.get('page')} result count: {len(resp_data)}")

            if len(resp_data) < self.PAGE_SIZE:
                break

            self.next_page(params)

        return page_resp

    # Remove Null from response to avoid type issues
    def remove_null_values(self, d: Collection):
        if isinstance(d, dict):
            return dict((k, self.remove_null_values(v)) for k, v in d.items() if v and self.remove_null_values(v))
        elif isinstance(d, list):
            return [self.remove_null_values(v) for v in d if v and self.remove_null_values(v)]
        else:
            return d

    @staticmethod
    def _org_param(org_id: int) -> dict:
        if not org_id:
            return {}

        return {"o": org_id}

    @staticmethod
    def first_page(params=None) -> Dict:
        if params is None:
            params = {}
        params.update({"limit": ApiClient.PAGE_SIZE, "page": 0})
        return params

    @staticmethod
    def next_page(params: Dict) -> None:
        params["page"] += 1

    # Organizations
    def get_orgs(self) -> Dict:
        """
        Retrieve Automox organizations
        :return: Dict of organizations
        """
        return self._page_results(f"{self.endpoint}/orgs")

    def get_org_users(self, org_id: int) -> Dict:
        """
        Retrieve Automox organization users
        :param org_id: Organization ID
        :return: Dict of users
        """
        return self._page_results(f"{self.endpoint}/users", self._org_param(org_id))

    # Devices/Endpoints
    def get_device(self, org_id: int, device_id: int) -> Dict:
        return self._call_api("GET", f"{self.endpoint}/servers/{device_id}", params=self._org_param(org_id))

    def find_device_by_attribute(self, org_id: int, attributes: List[str], value: str) -> dict:
        params = self.first_page(self._org_param(org_id))

        while True:
            devices = self._call_api("GET", f"{self.endpoint}/servers", params)

            for device in devices:
                for attr in attributes:
                    if isinstance(device[attr], str):
                        if device[attr].casefold() == value.casefold():
                            return self.remove_null_values(device)
                    if isinstance(device[attr], list):
                        if value.lower() in (v.upper() for v in device[attr]):
                            return self.remove_null_values(device)

            if len(devices) < self.PAGE_SIZE:
                break

            self.next_page(params)
        self.logger.info(f"Device {value} not found")
        return {}

    def get_device_software(self, org_id: int, device_id: int) -> Dict:
        return self._page_results(f"{self.endpoint}/servers/{device_id}/packages", self._org_param(org_id))

    def get_devices(self, org_id: int, group_id: int) -> List[Dict]:
        """
        Retrieve Automox managed devices/endpoints
        :param org_id: Organization ID
        :param group_id: Group ID
        :return: Dict of devices
        """
        params = self._org_param(org_id)
        params["groupId"] = group_id
        return self._page_results(f"{self.endpoint}/servers", params)

    def run_device_command(self, org_id: int, device_id: int, command: str) -> bool:
        """
        Run Command on Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :param command: Command to be run
        :return: Boolean of outcome
        """
        resp = self._call_api(
            "POST", f"{self.endpoint}/servers/{device_id}/queues", params=self._org_param(org_id), json_data=command
        )
        return resp is not None

    def update_device(self, org_id: int, device_id: int, payload: Dict) -> bool:
        """
        Update Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :param payload: Dict of parameters to update on device
        :return: Boolean of outcome
        """
        resp = self._call_api(
            "PUT", f"{self.endpoint}/servers/{device_id}", params=self._org_param(org_id), json_data=payload
        )
        return resp is not None

    def delete_device(self, org_id: int, device_id: int) -> bool:
        """
        Delete Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :return: Boolean of outcome
        """
        resp = self._call_api("DELETE", f"{self.endpoint}/servers/{device_id}", params=self._org_param(org_id))
        return resp is not None

    # Policies
    @staticmethod
    def _sanitize_policies(policies: [dict]) -> List[Dict]:
        for policy in policies:
            for key, fields in {"configuration": ["evaluation_code", "installation_code", "remediation_code"]}.items():
                if key in policy:
                    for f in fields:
                        try:
                            del policy[key][f]
                        except KeyError:
                            pass
        return policies

    def get_policies(self, org_id: int) -> List[Dict]:
        """
        Retrieve Automox policies
        :param org_id: Organization ID
        :return: List of Policies
        """
        policies = self._page_results(f"{self.endpoint}/policies", self._org_param(org_id))
        return self._sanitize_policies(policies)

    # Device Groups
    def get_group(self, org_id: int, group_id: int) -> Dict:
        return self._call_api("GET", f"{self.endpoint}/servergroups/{group_id}", params=self._org_param(org_id))

    def get_groups(self, org_id: int, sanitize: bool = True) -> List[Dict]:
        """
        Retrieve Automox groups
        :param org_id: Organization ID
        :param sanitize: Boolean defining whether null values should be removed
        :return: List of Groups
        """
        return self._page_results(f"{self.endpoint}/servergroups", self._org_param(org_id), sanitize)

    def create_group(self, org_id: int, payload: Dict) -> Dict:
        """
        Create Device group
        :param org_id: Organization ID
        :param payload: Dict of parameters to create group
        :return: Dict of Group
        """
        return self._call_api(
            "POST", f"{self.endpoint}/servergroups", params=self._org_param(org_id), json_data=payload
        )

    def update_group(self, org_id: int, group_id: int, payload: Dict) -> bool:
        """
        Update Device group
        :param org_id: Organization ID
        :param group_id: Group ID
        :param payload: Dict of parameters to update on group
        :return: Boolean of outcome
        """
        resp = self._call_api(
            "PUT", f"{self.endpoint}/servergroups/{group_id}", params=self._org_param(org_id), json_data=payload
        )
        return resp is not None

    def delete_group(self, org_id: int, group_id: int) -> bool:
        """
        Delete Device group
        :param org_id: Organization ID
        :param group_id: Group ID
        :return: Boolean of outcome
        """
        resp = self._call_api("DELETE", f"{self.endpoint}/servergroups/{group_id}", params=self._org_param(org_id))
        return resp is not None

    # Vulnerability Sync
    def upload_vulnerability_sync_file(self, org_id: int, file_content, filename, report_source) -> Dict:
        with io.BytesIO(file_content) as file:
            files = [("file", (filename, file, "text/csv"))]

            headers = {"Authorization": f"Bearer {self.api_key}"}
            params = self._org_param(org_id)
            params['source'] = report_source

            try:
                response = requests.post(
                    f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/upload",
                    params=params,
                    files=files,
                    headers=headers,
                )  # nosec B113

                if response.status_code == 201:
                    return {
                        "id": response.json().get("id"),
                        "status": response.json().get("status"),
                    }
                else:
                    raise PluginException(
                        cause="Failed to upload file to Vulnerability Sync",
                        assistance=f"Response code: {response.status_code}, Content: {response.content}",
                    )
            except Exception as e:
                raise PluginException(
                    cause="Failed to upload file to Vulnerability Sync",
                    assistance=f"Review encoded CSV file and try again: {e}",
                )

    def list_vulnerability_sync_action_sets(self, org_id: int, params=None) -> List[Dict]:
        if params is None:
            params = {}
        params.update(self._org_param(org_id))
        return self._page_results_data(f"{self.endpoint}/orgs/{org_id}/remediations/action-sets",
                                       params=params)

    def list_vulnerability_sync_action_set_issues(self, org_id: int, action_set_id: int, params=None) -> List[Dict]:
        if params is None:
            params = {}
        params.update(self._org_param(org_id))
        return self._page_results_data(f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/{action_set_id}/issues",
                                       params=params)

    def list_vulnerability_sync_action_set_solutions(self, org_id: int, action_set_id: int, params=None) -> List[Dict]:
        if params is None:
            params = {}
        params.update(self._org_param(org_id))
        return self._page_results_data(
            f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/{action_set_id}/solutions",
            params=params)

    def get_vulnerability_sync_action_set(self, org_id: int, action_set_id: int) -> Dict:
        params = self._org_param(org_id)
        return self._call_api("GET",
                              f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/{action_set_id}",
                              params=params)

    def delete_vulnerability_sync_action_set(self, org_id: int, action_set_id: int) -> bool:
        params = self._org_param(org_id)
        resp = self._call_api("DELETE", f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/{action_set_id}",
                              params=params)
        # 204 No Content
        return resp is None

    def execute_vulnerability_sync_actions(self, org_id: int, action_set_id: int, actions: List[Dict]) -> Dict:
        params = self._org_param(org_id)
        data = {
            "actions": actions
        }
        return self._call_api("POST", f"{self.endpoint}/orgs/{org_id}/remediations/action-sets/{action_set_id}/actions",
                              json_data=data, params=params)

    # Events
    def get_events(self, org_id: int, event_type: str, page: int = 0) -> List[Dict]:
        params = self._org_param(org_id)
        params.update({"eventName": event_type, "page": page, "limit": self.PAGE_SIZE})
        return self.remove_null_values(self._call_api("GET", f"{self.endpoint}/events", params))

    # Instrumentation for usage/adoption
    def report_api_outcome(self, outcome: str, function: str, elapsed_time: int, fail_reason: str = ""):
        """
        Record API Outcome to Automox
        :param outcome: Success/failure
        :param function: Capability being instrumented
        :param fail_reason: Optional failure reason
        :param elapsed_time: Elapsed time in seconds
        """
        payload = {
            "name": ApiClient.INTEGRATION_NAME,
            "version": ApiClient.VERSION,
            "function": function,
            "outcome": outcome,
            "elapsed_time": elapsed_time,
        }

        if outcome == ApiClient.OUTCOME_FAIL:
            payload["reason_for_failure"] = fail_reason

        try:
            self._call_api("POST", f"{self.endpoint}/integration-health", json_data=payload)
        except Exception:
            # Do nothing, we don't care if it fails
            return
