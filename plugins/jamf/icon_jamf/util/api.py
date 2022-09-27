import json
from logging import Logger
from typing import Any, Dict, List, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.auth import HTTPBasicAuth

from .endpoints import Endpoint


class ApiClient:
    def __init__(self, base_url: str, username: str, password: str, logger: Logger) -> None:
        self.base_url = base_url if base_url.endswith("/") else f"{base_url}/"
        self.username = username
        self.password = password
        self.logger = logger

    def add_computer_to_group(self, computer_group_id: int, computer_ids: List[int]) -> requests.Response:
        url = self.base_url + Endpoint.ADD_COMPUTER_TO_GROUP.format(computer_group_id)
        computer_id_payload = ""
        for computer_id in computer_ids:
            computer_id_payload = f"<computer><id>{computer_id}</id></computer>" + computer_id_payload
        payload = f"<computer_group><computer_additions>{computer_id_payload}</computer_additions></computer_group>"
        return self._call_api("PUT", url, headers=self._get_headers_xml(), data=payload)

    def erase_computer(self, computer_id: int, passcode: str) -> None:
        url = self.base_url + Endpoint.ERASE_COMPUTER.format(passcode, computer_id)
        self._call_api("POST", url, headers=self._get_headers_json())

    def get_device_groups(self, device_id: str) -> Dict[str, Any]:
        url = self.base_url + Endpoint.GET_DEVICE_GROUPS.format(device_id)
        return self._call_api("GET", url, headers=self._get_headers_json(), return_json=True)

    def get_devices_name_id(self, device_name: str) -> Dict[str, Any]:
        url = self.base_url + Endpoint.GET_DEVICES_NAME_ID.format(device_name)
        return self._call_api("GET", url, headers=self._get_headers_json(), return_json=True)

    def get_group_detail(self, identifier: int) -> Dict[str, Any]:
        url = self.base_url + Endpoint.GET_GROUP_DETAIL.format(identifier)
        return self._call_api("GET", url, headers=self._get_headers_json(), return_json=True)

    def get_user_location(self, device_id: str) -> Dict[str, Any]:
        url = self.base_url + Endpoint.GET_USER_LOCATION.format(device_id)
        return self._call_api("GET", url, headers=self._get_headers_json(), return_json=True)

    def lock_computer(self, computer_id: int, passcode: int) -> None:
        url = self.base_url + Endpoint.LOCK_COMPUTER.format(passcode, computer_id)
        self._call_api("POST", url, headers=self._get_headers_json(), return_json=True)

    def lock_mobile_devices(self, devices_id: List[str]) -> requests.Response:
        url = self.base_url + Endpoint.LOCK_MOBILE_DEVICES.format(",".join(devices_id))
        return self._call_api("POST", url, headers=self._get_headers_json())

    def test_connection(self) -> None:
        url = self.base_url + Endpoint.USERS
        self._call_api("GET", url)

    def _get_headers_json(self) -> Dict[str, str]:
        return {"Accept": "application/json"}

    def _get_headers_xml(self) -> Dict[str, str]:
        return {"Accept": "application/xml"}

    def _call_api(
        self,
        method: str,
        url: str,
        headers: dict = None,
        data: dict = None,
        json_data: Union[List[dict], dict] = None,
        params: dict = None,
        return_json: bool = False,
    ) -> Union[requests.Response, Dict[str, Any]]:
        response = requests.request(
            method,
            url,
            headers=headers,
            data=data,
            json=json_data,
            params=params,
            auth=HTTPBasicAuth(self.username, self.password),
        )
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code in (401, 403):
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if response.status_code == 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        if 200 <= response.status_code < 300:
            try:
                return response.json() if return_json else response
            except json.decoder.JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        self.logger.info("Call to Jamf API failed")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
