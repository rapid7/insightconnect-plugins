import json

import requests
from logging import Logger

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import HTTPError


class IVM_Cloud:
    def __init__(self, token: str, logger: Logger, url: str):
        self.logger = logger
        self.token = token
        self.base_url = url

    def call_api(self, path: str, request_type: str, params: dict = None, body: dict = None) -> dict:
        if params is None:
            params = {}
        if body is None:
            body = {}

        api_url = self.base_url + path
        headers = {"x-api-key": self.token, "content-type": "application/json"}
        try:
            response = requests.request(
                request_type,
                self.base_url + path,
                params=insightconnect_plugin_runtime.helper.clean(params),
                headers=headers,
                data=json.dumps(body),
            )
            self.logger.info(response.json())
            if response.status_code not in [200, 201, 202]:
                data = json.loads(response.text)
                message = data.get("message", "")
                if response.status_code == 400:
                    raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=data)
                raise PluginException(
                    cause=f"Failed to get a valid response from InsightVM at endpoint '{api_url}'",
                    assistance=message,
                    data=data,
                )
            if response.text != "":
                response_json = response.json()
                response_json["status_code"] = response.status_code
                return response_json

        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint '{api_url}'",
                assistance=f"Response was {httpError.response.text}.",
                data=httpError,
            )

    def test_api(self, api_url: str) -> dict:
        params = {}
        headers = {"x-api-key": self.token}

        try:
            response = requests.request(
                "POST", api_url, params=insightconnect_plugin_runtime.helper.clean(params), headers=headers
            )
            response.raise_for_status()
            return insightconnect_plugin_runtime.helper.clean(response.json())
        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint '{api_url}'",
                assistance=f"Response was {httpError.response.text}.",
                data=httpError,
            )
