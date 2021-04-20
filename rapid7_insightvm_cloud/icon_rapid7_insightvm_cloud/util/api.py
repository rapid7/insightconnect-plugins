from requests import request
from logging import Logger

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import HTTPError


class IVM_Cloud:

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code",
    }

    def __init__(self, token: str, logger: Logger, max_pages: int, url: str):
        self.logger = logger
        self.token = token
        self.base_url = url
        if max_pages:
            self.max_pages = max_pages
        else:
            self.max_pages = 100

    def call_api_pages(self, path: str, request_type: str, params: dict = None):
        responses = []
        for pages in range(self.max_pages):
            params.append(("page", pages))
            response = self.call_api(path, request_type, params)
            responses.append(response)

        return responses

    def call_api(self, path: str, request_type: str, params: dict = None):
        if params is None:
            params = {}

        api_url = self.base_url + path

        headers = {"x-api-key": self.token}

        try:
            response = request(request_type, self.base_url + path,
                               params=insightconnect_plugin_runtime.helper.clean(params),
                               headers=headers)
            if response.status_code not in [200, 201, 202]:
                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                raise PluginException(
                    cause=f"Failed to get a valid response from InsightVM at endpoint {api_url}",
                    assistance=f"Response was {status_code_message}",
                    data=response.status_code,
                )
            if response.text == '':
                return response.status_code
            if "data" in response:
                return response.get("data")
            else:
                return response.json()
        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint {api_url}",
                assistance=f"Response was {httpError.response.text}",
                data=httpError,
            )

    def test_api(self, params: dict = None) -> dict:
        if params is None:
            params = {}

        api_url = "https://us.api.insight.rapid7.com/validate"

        headers = {"x-api-key": self.token}

        try:
            response = request("POST", api_url, params=insightconnect_plugin_runtime.helper.clean(params),
                               headers=headers)
            response.raise_for_status()
            return insightconnect_plugin_runtime.helper.clean(response.json())
        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint {api_url}",
                assistance=f"Response was {httpError.response.text}",
                data=httpError,
            )
