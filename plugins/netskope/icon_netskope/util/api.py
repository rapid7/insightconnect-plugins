import base64
from json import JSONDecodeError
from logging import Logger
from typing import Optional, Union, List, Dict, Any

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_netskope.util.constants import MAX_TRIES, DEFAULT_TIMEOUT
from icon_netskope.util.utils import rate_limiting, remove_json_version_from_data


class ApiClient:
    def __init__(self, tenant: str, api_key_v1: str, api_key_v2: str, logger: Optional[Logger] = None) -> None:
        self.api_url_v1 = f"https://{tenant}.goskope.com/api/v1/"
        self.api_url_v2 = f"https://{tenant}.goskope.com/api/v2/"
        self.api_key_v1 = api_key_v1
        self.api_key_v2 = api_key_v2
        self.test_connection = False
        self.logger = logger

    def update_file_hash_list(self, name: str, hash_list: List[str]) -> Dict[str, Any]:
        return self._call_api_v1(
            "PUT",
            f"{self.api_url_v1}updateFileHashList",
            params={"name": name, "list": ",".join(hash_list)},
        )

    def get_all_url_list(self, params: Dict[str, Any]) -> list:
        return remove_json_version_from_data(
            self._call_api_v2("GET", f"{self.api_url_v2}policy/urllist", params=params)
        )

    def create_a_new_url_list(self, params: Dict[str, Any]) -> list:
        created_urllist = self._call_api_v2("POST", f"{self.api_url_v2}policy/urllist", json_data=params)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(created_urllist[0].get("id"))

    def upload_json_config(self, filename: str, content: bytes) -> Dict[str, Any]:
        uploaded_urllist = self._call_api_v2(
            "POST", f"{self.api_url_v2}policy/urllist/file", files={"urllist": (filename, base64.b64decode(content))}
        )
        self.apply_pending_url_list_changes()
        return self._get_all_uploaded_json_config(uploaded_urllist)

    def get_url_list_by_id(self, identifier: int) -> Dict[str, Any]:
        return remove_json_version_from_data(self._call_api_v2("GET", f"{self.api_url_v2}policy/urllist/{identifier}"))

    def replace_url_list_by_id(self, identifier: int, data: Dict[str, Any]) -> Dict[str, Any]:
        self._call_api_v2("PUT", f"{self.api_url_v2}policy/urllist/{identifier}", json_data=data)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(identifier)

    def delete_url_list_by_id(self, identifier: int) -> Dict[str, Any]:
        self._call_api_v2("DELETE", f"{self.api_url_v2}policy/urllist/{identifier}")
        deleted_urllist = self.get_url_list_by_id(identifier)
        deleted_urllist["pending"] = 0
        self.apply_pending_url_list_changes()
        return deleted_urllist

    def patch_url_list_by_id(self, identifier: int, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        self._call_api_v2("PATCH", f"{self.api_url_v2}policy/urllist/{identifier}/{action}", json_data=data)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(identifier)

    def apply_pending_url_list_changes(self) -> list:
        deployed_lists = self.get_all_url_list({"pending": 1})
        self._call_api_v2("POST", f"{self.api_url_v2}policy/urllist/deploy")
        return deployed_lists

    def get_single_user_confidence_index(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return self._call_api_v2("POST", f"{self.api_url_v2}ubadatasvc/user/uci", json_data=data)

    def test_api(self) -> None:
        self.test_connection = True
        self._call_api_v1("GET", f"{self.api_url_v1}updateFileHashList/")
        self.get_all_url_list({"pending": 1})

    def _get_all_uploaded_json_config(self, input_list_of_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Gets all the items by ID and returns list of URL lists with data it got.

        :param input_list_of_items: Input list of dict that contains "id" key
        :type input_list_of_items: List[Dict[str, Any]]

        :returns: List of dict of items from upload JSON config file action
        :rtype: List[Dict[str, Any]]
        """

        return [self.get_url_list_by_id(item.get("id")) for item in input_list_of_items]

    @rate_limiting(max_tries=MAX_TRIES)
    def _call_api_v1(
        self,
        method: str,
        url: str,
        json_data: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        timeout: int = DEFAULT_TIMEOUT,
        **kwargs,
    ) -> Dict[str, Any]:
        if json_data is None:
            json_data = {}
        response = requests.request(
            method, url, json={**json_data, "token": self.api_key_v1}, params=params, timeout=timeout, **kwargs
        )
        try:
            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code in (429, 503, 512):
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if 200 <= response.status_code < 300:
                if response.json().get("errors", False) and not self.test_connection:
                    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
                return response.json()
            self.logger.info("Call to Netskope API failed")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

    @rate_limiting(max_tries=MAX_TRIES)
    def _call_api_v2(
        self,
        method: str,
        url: str,
        json_data: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        timeout: int = DEFAULT_TIMEOUT,
        **kwargs,
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        response = requests.request(
            method,
            url,
            json=json_data,
            params=params,
            headers={"Netskope-Api-Token": self.api_key_v2},
            files=files,
            timeout=timeout,
            **kwargs,
        )
        try:
            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code in (400, 404):
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code in (429, 503, 512):
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if 200 <= response.status_code < 300:
                return response.json()
            self.logger.info("Call to Netskope API failed")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
