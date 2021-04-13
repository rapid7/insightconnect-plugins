from requests import request
from logging import Logger

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import HTTPError


class IVM_Cloud:
    def __init__(self, token: str, logger: Logger, max_pages: int, region: str):
        self.logger = logger
        self.token = token
        self.base_url = "https://" + region + ".api.insight.rapid7.com/vm/v4/integration/"
        if max_pages:
            self.max_pages = max_pages
        else:
            self.max_pages = 100

    def call_api(self, path: str, request_type: str, params: dict = None) -> dict:
        if params is None:
            params = {}

        api_url = self.base_url + path

        headers = {"x-api-key": self.token}

        try:
            response = request(request_type, self.base_url + path, params=insightconnect_plugin_runtime.helper.clean(params),
                               headers=headers)
            response.raise_for_status()
            return insightconnect_plugin_runtime.helper.clean(response.json())
        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from InsightVM at endpoint {api_url}",
                assistance=f"Response was {httpError.response.text}",
                data=httpError,
            )

    def call_api_pages(self, path: str, params: dict = None):
        responses = []
        for pages in range(self.max_pages):
            cleaned_response = self.call_api(path, params)
            if "data" in cleaned_response:
                responses.extend(cleaned_response.get("data"))

            if "links" not in cleaned_response or "next" not in cleaned_response["links"]:
                break
        return responses

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
