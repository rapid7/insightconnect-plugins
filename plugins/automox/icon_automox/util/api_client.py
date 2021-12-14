from insightconnect_plugin_runtime.exceptions import PluginException
import json
import requests
from typing import Dict, List


class ApiClient:
    VERSION = "0.1.0"
    PAGE_SIZE = 500

    def __init__(self, logger, api_key, endpoint = "https://console.automox.com/api"):
        self.endpoint = endpoint
        self.api_key = api_key
        self.session = requests.session()

        # Define headers for client
        self.set_headers()

        # Define logger
        self.logger = logger

    def set_headers(self) -> None:
        self.session.headers = {
           'Authorization': 'Bearer ' + self.api_key,
           'User-Agent': f"ax:automox-rapid7-insightconnect-plugin/{ApiClient.VERSION}",
           "content-type": "application/json"
        }

    def _call_api(self, method: str, url: str, params: Dict = dict(), json_data: object = None) -> json:
        try:
            response = self.session.request(method, url, json=json_data, params=params)

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY)

            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)

            if response.status_code == 204:
                return

            if 200 <= response.status_code < 300:
                return response.json()
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Automox Console API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _page_results(self, url: str, init_params: Dict = dict(), sanitize: bool = True) -> json:
        params = self.first_page(init_params)

        page_resp = []

        while True:
            resp = self._call_api("get", url, params)
            if sanitize:
                resp = self.remove_null_values(resp)

            page_resp.extend(resp)

            self.logger.info(f"Page {params.get('page')} result count: {len(resp)}")

            if len(resp) < self.PAGE_SIZE:
                break

            self.next_page(params)

        return page_resp

    # Remove Null from response to avoid type issues
    def remove_null_values(self, d):
        if type(d) is dict:
            return dict((k, self.remove_null_values(v)) for k, v in d.items() if v and self.remove_null_values(v))
        elif type(d) is list:
            return [self.remove_null_values(v) for v in d if v and self.remove_null_values(v)]
        else:
            return d

    @staticmethod
    def _org_param(org_id):
        return {"o": org_id}

    @staticmethod
    def first_page(params: Dict = {}):
        params.update({
            'limit': ApiClient.PAGE_SIZE,
            'page': 0
            })
        return params

    @staticmethod
    def next_page(params: Dict) -> None:
        params['page'] += 1

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

    def find_device_by_attribute(self, org_id: int, attributes: List[str], value: str):
        params = self.first_page({"o": org_id})

        while True:
            devices = self._call_api("get", f"{self.endpoint}/servers", params)

            for device in devices:
                for attr in attributes:
                    if type(device[attr]) is str:
                        if device[attr].casefold() == value.casefold():
                            return device
                    if type(device[attr]) is list:
                        if value.lower() in (v.upper() for v in device[attr]):
                            return device

            if len(devices) < self.PAGE_SIZE:
                break

            self.next_page(params)

    def get_device_software(self, org_id: int, device_id: int) -> Dict:
        return self._page_results(f"{self.endpoint}/servers/{device_id}/packages", self._org_param(org_id))

    def get_devices(self, org_id: int, group_id: int) -> List[Dict]:
        """
        Retrieve Automox managed devices/endpoints
        :param org_id: Organization ID
        :param group_id: Group ID
        :return: Dict of devices
        """
        params = {"o": org_id, "groupId": group_id}
        return self._page_results(f"{self.endpoint}/servers", params)

    def run_device_command(self, org_id: int, device_id: int, command: str):
        """
        Run Command on Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :param command: Command to be run
        :return: Boolean of outcome
        """
        return self._call_api("POST", f"{self.endpoint}/servers/{device_id}/queues",
                              params=self._org_param(org_id), json_data=command)

    def update_device(self, org_id: int, device_id: int, payload: Dict) -> bool:
        """
        Update Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :param payload: Dict of parameters to update on device
        :return: Boolean of outcome
        """
        return self._call_api("PUT", f"{self.endpoint}/servers/{device_id}",
                              params=self._org_param(org_id), json_data=payload)

    def delete_device(self, org_id: int, device_id: int) -> bool:
        """
        Delete Device
        :param org_id: Organization ID
        :param device_id: Device ID
        :return: Boolean of outcome
        """
        return self._call_api("DELETE", f"{self.endpoint}/servers/{device_id}", params=self._org_param(org_id))

    # Policies
    @staticmethod
    def _sanitize_policies(policies) -> List[Dict]:
        for policy in policies:
            for key, fields in {'configuration': ['evaluation_code', 'installation_code', 'remediation_code']}.items():
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
        return self._call_api("POST", f"{self.endpoint}/servergroups",
                              params=self._org_param(org_id), json_data=payload)

    def update_group(self, org_id: int, group_id: int, payload: Dict) -> bool:
        """
        Update Device group
        :param org_id: Organization ID
        :param group_id: Group ID
        :param payload: Dict of parameters to update on group
        :return: Boolean of outcome
        """
        return self._call_api("PUT", f"{self.endpoint}/servergroups/{group_id}",
                              params=self._org_param(org_id), json_data=payload)

    def delete_group(self, org_id: int, group_id: int):
        """
        Delete Device group
        :param org_id: Organization ID
        :param group_id: Group ID
        :return: Boolean of outcome
        """
        return self._call_api("DELETE", f"{self.endpoint}/servergroups/{group_id}", params=self._org_param(org_id))
