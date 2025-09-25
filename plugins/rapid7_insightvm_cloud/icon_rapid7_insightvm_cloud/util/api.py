import json

import requests
from logging import Logger
from typing import Any

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from requests.exceptions import HTTPError
from uuid import uuid4
from os import environ
from flask import request


class IVM_Cloud:
    def __init__(self, region: str, token: str, version: str, logger: Logger):
        self.logger = logger
        self.token = token
        self.base_url = f"https://{region}.api.insight.rapid7.com/vm/v4/integration/"
        self.version = version

    def call_api(
        self, path: str, request_type: str, params: dict[str, Any] = None, body: dict[str, Any] = None
    ) -> dict[str, Any]:
        if params is None:
            params = {}

        if body is None:
            body = {}

        endpoint = f"{self.base_url}{path}"
        headers = self._get_headers()
        try:
            self.logger.info(
                f"Making request to {endpoint} with request ID: {headers.get('R7-Correlation-Id', 'N/A')}",
            )
            response = requests.request(
                request_type,
                endpoint,
                params=insightconnect_plugin_runtime.helper.clean(params),
                headers=headers,
                data=json.dumps(insightconnect_plugin_runtime.helper.clean(body)),
            )
            if response.status_code not in [200, 201, 202]:
                data = json.loads(response.text)
                message = data.get("message", "")
                if response.status_code == 400:
                    raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=data)
                raise PluginException(
                    cause=f"Failed to get a valid response from InsightVM at endpoint '{endpoint}'. Request ID: {headers.get('R7-Correlation-Id', 'N/A')}'",
                    assistance=message,
                    data=data,
                )
            response_json = {}
            if response.text != "":
                response_json = response.json()
            response_json["status_code"] = response.status_code
            return response_json

        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint '{endpoint}'",
                assistance=f"Response was {httpError.response.text}.",
                data=httpError,
            )

    def test_api(self, endpoint: str) -> dict[str, Any]:
        headers = self._get_headers()
        try:
            response = requests.request("POST", endpoint, headers=headers)
            response.raise_for_status()
            return insightconnect_plugin_runtime.helper.clean(response.json())
        except HTTPError as httpError:
            raise ConnectionTestException(
                cause=f"Failed to get a valid response from InsightVM at endpoint '{endpoint}'. Request ID: {headers.get('R7-Correlation-Id', 'N/A')}'",
                assistance=f"Response was {httpError.response.text}.",
                data=httpError,
            )

    def _get_headers(self) -> dict[str, str]:
        return {
            "x-api-key": self.token,
            "content-type": "application/json",
            "User-Agent": f"r7:insightconnect-insightvm-cloud-plugin/{self.version}",
            "R7-Correlation-Id": self._get_correlation_id(),
        }

    @staticmethod
    def _get_correlation_id() -> str:
        if environ.get("PLUGIN_RUNTIME_ENVIRONMENT") == "cloud":
            return request.headers.get("X-REQUEST-ID", str(uuid4()))
        return str(uuid4())
