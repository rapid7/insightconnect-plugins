import base64
import time
from json import JSONDecodeError
from logging import Logger
from typing import Callable, Optional, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

RETRY_MESSAGE = "Rate limiting error occurred. Retrying in {delay:.1f} seconds ({attempts_counter}/{max_tries})"

MAX_TRIES = 10


class ApiClient:
    def __init__(self, tenant: str, api_key_v1: str, api_key_v2: str, logger: Optional[Logger] = None) -> None:
        self.api_url_v1 = f"https://{tenant}.goskope.com/api/v1/"
        self.api_url_v2 = f"https://{tenant}.goskope.com/api/v2/"
        self.api_key_v1 = api_key_v1
        self.api_key_v2 = api_key_v2
        self.test_connection = False
        self.logger = logger

    def update_file_hash_list(self, data: dict) -> dict:
        update_file_hash_list_url = f"{self.api_url_v1}updateFileHashList/"
        return self._call_api_v1("GET", update_file_hash_list_url, json_data={"token": self.api_key_v1, **data})

    def get_all_url_list(self, params: dict) -> list:
        get_all_url_list_url = f"{self.api_url_v2}policy/urllist/"
        return self._call_api_v2("GET", get_all_url_list_url, params=params)

    def create_a_new_url_list(self, params: dict) -> list:
        create_a_new_url_list_url = f"{self.api_url_v2}policy/urllist/"
        created_urllist = self._call_api_v2("POST", create_a_new_url_list_url, json_data=params)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(created_urllist[0].get("id"))

    def upload_json_config(self, filename: str, content: bytes) -> dict:
        upload_json_config_url = f"{self.api_url_v2}policy/urllist/file/"
        return self._call_api_v2(
            "POST", upload_json_config_url, files={"urllist": (filename, base64.b64decode(content))}
        )

    def get_url_list_by_id(self, identifier: int) -> dict:
        get_url_list_by_id_url = f"{self.api_url_v2}policy/urllist/{identifier}"
        return self._call_api_v2("GET", get_url_list_by_id_url)

    def replace_url_list_by_id(self, identifier: int, data: dict) -> dict:
        replace_url_list_by_id_url = f"{self.api_url_v2}policy/urllist/{identifier}"
        self._call_api_v2("PUT", replace_url_list_by_id_url, json_data=data)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(identifier)

    def delete_url_list_by_id(self, identifier: int) -> dict:
        delete_url_list_by_id_url = f"{self.api_url_v2}policy/urllist/{identifier}"
        self._call_api_v2("DELETE", delete_url_list_by_id_url)
        deleted_urllist = self.get_url_list_by_id(identifier)
        deleted_urllist["pending"] = 0
        self.apply_pending_url_list_changes()
        return deleted_urllist

    def patch_url_list_by_id(self, identifier: int, action: str, data: dict) -> dict:
        patch_url_list_by_id_url = f"{self.api_url_v2}policy/urllist/{identifier}/{action}"
        self._call_api_v2("PATCH", patch_url_list_by_id_url, json_data=data)
        self.apply_pending_url_list_changes()
        return self.get_url_list_by_id(identifier)

    def apply_pending_url_list_changes(self) -> list:
        apply_pending_url_list_changes_url = f"{self.api_url_v2}policy/urllist/deploy/"
        deployed_lists = self.get_all_url_list({"pending": 1})
        self._call_api_v2("POST", apply_pending_url_list_changes_url)
        return deployed_lists

    def get_single_user_confidence_index(self, data: dict) -> dict:
        get_single_user_uci_url = f"{self.api_url_v2}ubadatasvc/user/uci"
        return self._call_api_v2("POST", get_single_user_uci_url, json_data=data)

    def test_api(self) -> dict:
        GET_TEST_URL = f"{self.api_url_v1}updateFileHashList/"
        self.test_connection = True
        self._call_api_v1("GET", GET_TEST_URL, json_data={"token": self.api_key_v1})
        return self.get_all_url_list({"pending": 1})

    def _rate_limiting(max_tries: int) -> dict:
        """This decorator allows to work API call with rate limiting by using exponential backoff function. Decorator needs to have
        max_tries argument entered obligatory

        :param max_tries: Maximum number of retries calling API function
        :type max_tries: int

        :returns: API call function data
        :rtype: dict
        """

        def _decorate(func: Callable):
            def _wrapper(self, *args, **kwargs):
                retry = True
                attempts_counter, delay = 0, 0
                while retry and attempts_counter < max_tries:
                    if attempts_counter:
                        time.sleep(delay)
                    try:
                        retry = False
                        return func(self, *args, **kwargs)
                    except PluginException as error:
                        attempts_counter += 1
                        delay = 2 ** (attempts_counter * 0.6)
                        if error.cause == PluginException.causes[PluginException.Preset.RATE_LIMIT]:
                            self.logger.info(
                                RETRY_MESSAGE.format(
                                    delay=delay, attempts_counter=attempts_counter, max_tries=max_tries
                                )
                            )
                            retry = True
                return func(self, *args, **kwargs)

            return _wrapper

        return _decorate

    @_rate_limiting(max_tries=MAX_TRIES)
    def _call_api_v1(self, method: str, url: str, json_data: dict = None, params: dict = None) -> dict:
        response = requests.request(method, url, json=json_data, params=params)
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
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        self.logger.info("Call to Netskope API failed")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    @_rate_limiting(max_tries=MAX_TRIES)
    def _call_api_v2(
        self, method: str, url: str, json_data: dict = None, params: dict = None, files: dict = None
    ) -> Union[list, dict]:
        headers = {"Netskope-Api-Token": self.api_key_v2}
        response = requests.request(method, url, json=json_data, params=params, headers=headers, files=files)
        try:
            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code in (400, 404):
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code in (429, 503, 512):
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if 200 <= response.status_code < 300:
                return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        self.logger.info("Call to Netskope API failed")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
