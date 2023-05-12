import json
from typing import Optional, Union
import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException


class HiveAPI:
    def __init__(self, url: str, username: str, password: str, api_key: str, proxies, cert):
        self.url = url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.proxy = proxies
        self.verify = cert

    # Get Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Get%20case
    # Working
    def get_case(self, case_id: str):
        return self._call_api("GET", f"api/case/{case_id}")

    # Create Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Create%20case
    # Issue with input
    def create_case(self, case):
        return self._call_api("POST", "api/case", data=case)

    # Create Observable In Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Create%20Observable%20in%20Case
    # WIP
    def create_case_observable(self, case_id, observable):
        return self._call_api("POST", f"api/case/{case_id}/observable", data=observable)

    # Create Task in Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Create%20Task%20in%20Case
    # WIP
    def create_task_in_case(self, case_id, case):
        return self._call_api("POST", f"api/case/{case_id}/task", data=case)

    # Close Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Delete%20case
    # WIP
    def close_case(self, case_id):
        return self._call_api("DELETE", f"api/case/{case_id}")

    # Get Cases
    # No Docs / Might have to remove this
    def get_cases(self):
        return self._call_api("GET", "api/case/_search", json_data={}, params={"range": "all", "sort": []})

    # Get Current User
    # https://docs.strangebee.com/thehive/api-docs/#operation/Get%20current%20User%20info
    # Working
    def get_current_user(self):
        return self._call_api("GET", f"api/user/current")

    # Get User By ID
    # https://docs.strangebee.com/thehive/api-docs/#operation/Get%20User
    # Working
    def get_user_by_id(self, user_id):
        return self._call_api("GET", f"api/user/{user_id}")

    def _call_api(
        self, method: str, path: str, params: Optional[dict] = None, data: Optional = None, json_data: Optional = None
    ) -> Union[dict, None]:

        # Build out the headers
        headers = {"X-Organisation": "myOrg", "Content-Type": "application/json"}

        # Handle the authentication method
        auth = None

        if self.api_key:
            auth = {"Authorization": f"Bearer {self.api_key}"}

        if self.username and self.password:
            auth = HTTPBasicAuth(self.username, self.password)

        # Jsonify the data
        data = json.dumps(data, sort_keys=True, indent=4, cls=json.JSONEncoder)

        response = requests.request(
            method, self.url + path, params=params, data=data, json=json_data, headers=headers, auth=auth
        )

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response)
        if response.status_code == 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response)
        if response.status_code in (200, 201):
            return response.json()
        if response.status_code == 204:
            return None
