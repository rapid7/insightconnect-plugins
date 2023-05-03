import json
from logging import Logger
from typing import Optional
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
    def get_case(self, case_id: str) -> dict:
        return self._call_api("GET", case_id, None, None)

    # Create Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Create%20case
    def create_case(self, case):
        return self._call_api("POST", None, None, case)

    # Create Task in Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Create%20Task%20in%20Case
    def create_task_in_case(self, case_id, case):
        return self._call_api("POST", case_id, None, case)

    # Close Case
    # https://docs.strangebee.com/thehive/api-docs/#operation/Delete%20case
    def close_case(self, case_id):
        return self._call_api("DELETE", case_id, None, None)

    # TODO
    # Create Case Observable
    # Docs

    # Get Cases
    # Docs

    # Get User
    # https://docs.strangebee.com/thehive/api-docs/#operation/Get%20User
    def get_user(self, user_id):
        return self._call_api("GET", user_id, None, None)

    def _call_api(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        data: Optional = None,
    ) -> dict:

        auth = None
        headers = {"X-Organisation": "myOrg", "Content-Type": "application/json"}

        if self.api_key:
            auth = f"Authorization: Bearer {self.api_key}"

        if self.username and self.password:
            auth = HTTPBasicAuth(self.username, self.password)

        response = requests.request(method, self.url + path, params=params, data=data, headers=headers, auth=auth)

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json())
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.something, data=response.json())
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.json())
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json())
        if response.status_code == 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.json())
        if 200 <= response.status_code < 300:
            return response.json()
