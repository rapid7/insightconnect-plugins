from requests import request
from logging import Logger

import komand
from komand.exceptions import PluginException
from requests.exceptions import HTTPError


class AttackerKB:
    def __init__(self, token: str, logger: Logger, max_pages: int):
        self.logger = logger
        self.token = token
        self.base_url = "https://api.attackerkb.com/"
        if max_pages:
            self.max_pages = max_pages
        else:
            self.max_pages = 100

    def call_api(self, path: str, params: dict = None) -> dict:
        if params is None:
            params = {}

        api_url = self.base_url + path

        headers = {
            "Authorization": f"basic {self.token}"
        }

        try:
            response = request("GET", self.base_url + path, params=komand.helper.clean(params), headers=headers)
            response.raise_for_status()
            return komand.helper.clean(response.json())
        except HTTPError as httpError:
            raise PluginException(
                cause=f"Failed to get a valid response from AttackerKB at endpoint {api_url}",
                assistance=f"Response was {httpError.response.text}",
                data=httpError
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
