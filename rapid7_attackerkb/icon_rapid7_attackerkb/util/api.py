from requests import request

import komand
from komand.exceptions import PluginException


class AttackerKB:
    def __init__(self, token, logger, max_pages):
        self.logger = logger
        self.token = token
        self.base_url = 'https://api.attackerkb.com/'
        if max_pages:
            self.max_pages = max_pages
        else:
            self.max_pages = 100

    def call_api(self, path, params=None):
        if params is None:
            params = {}

        api_url = self.base_url + path

        headers = {
            'Authorization': f'basic {self.token}'
        }

        try:
            response = request("GET", self.base_url + path, params=komand.helper.clean(params), headers=headers)
            response.raise_for_status()
            return komand.helper.clean(response.json())
        except Exception as e:
            raise PluginException(
                cause="Failed to get a response from API",
                assistance=f"at endpoint {api_url}",
                data=e
            )

    def call_api_pages(self, path, params=None):
        responses = []
        for pages in range(self.max_pages):
            cleaned_response = self.call_api(path, params)
            if "data" in cleaned_response:
                responses.extend(cleaned_response.get("data"))

            if "links" not in cleaned_response or "next" not in cleaned_response["links"]:
                break
        return responses
