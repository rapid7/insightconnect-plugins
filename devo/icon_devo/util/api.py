from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import urllib
import requests
import json

# From: https://docs.devo.com/confluence/ndt/api-reference/query-api
REGION_MAP = {
    "USA":"https://apiv2-us.devo.com/search/",
    "EU":"Https://apiv2-eu.devo.com/search/",
    "VDC (Spain)":"https://apiv2-es.devo.com/search/"
}


class DevoAPI():
    def __init__(self, logger, api_token, region):
        self.logger = logger
        self.token = api_token
        self.region = region

        self.base_url = REGION_MAP.get(region)
        if not self.base_url:
            raise PluginException(cause="Region not found.",
                                  assistance=f"The region {self.region} was not reconginzed, please check your connection input and try again.")

        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def test_connection(self):
        """
        This is kind of a cheaty test
        There's not a good "Am I connected" type method in the API
        I send a blank body to the query endpoint and make sure it sends back
        the bad object response instead of an unauthorized (or any other error) response
        """

        try:
            self._post_to_api("/query",{})
        except Exception as e:
            if "405" in e.data:
                return "pass"
            else:
                raise ConnectionTestException(ConnectionTestException.Preset.UNAUTHORIZED,
                                              data=e)


    def _post_to_api(self, endpoint, post_body):
        # Need this because if it starts with / url join thinks it's a root
        url = urllib.parse.urljoin(self.base_url, endpoint.lstrip("/"))
        try:
            response = requests.post(url=url, json=post_body, headers=self.headers)

            response_text = response.text

            if response.status_code == 400:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Bad request or invalid JSON.",
                    data=response_text,
                )
            if response.status_code > 401 and response.status_code < 404:
                raise PluginException(
                    PluginException.Preset.UNAUTHORIZED,
                    data=response_text
                )
            if response.status_code == 404:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance=f"The object at {url} does not exist.",
                    data=response_text,
                )
            # Success; no content
            # if response.status_code == 204:
            #     return None
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Request to {url} failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
