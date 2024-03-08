import json
from logging import Logger
from typing import Any, Dict, List

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class PaloAltoMineMeldAPI:
    def __init__(self, url: str, username: str, password: str, ssl_verify: bool, logger: Logger) -> None:
        self.url = url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.logger = logger

    def update_external_dynamic_list(
        self, list_name: str, updated_indicators_list: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        return self._call_api(
            "PUT",
            f"{self.url}/config/data/{list_name}_indicators",
            json_data=updated_indicators_list,
        )

    def get_indicators(self, list_name: str) -> Dict[str, Any]:
        return self._call_api("GET", f"{self.url}/config/data/{list_name}_indicators")

    def health_check(self) -> Dict[str, Any]:
        return self._call_api("GET", f"{self.url}/config/full", full_response=True).status_code == 200

    def _call_api(  # noqa: MC0001
        self,
        method: str,
        url: str,
        params: Dict[str, Any] = None,
        json_data: Dict[str, Any] = None,
        full_response: bool = False,
    ) -> Dict[str, Any]:
        response = {"text": ""}
        try:
            response = requests.request(
                method,
                url,
                json=json_data,
                params=params,
                auth=(self.username, self.password),
                verify=self.ssl_verify,
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if 400 <= response.status_code < 500:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                if full_response:
                    return response
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            self.logger.info(f"Invalid json: {error}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as error:
            self.logger.info(f"Call to Palo Alto MineMeld failed: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
