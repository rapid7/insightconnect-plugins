import datetime
import logging

import dateparser
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import urllib
import requests
import json
from typing import Optional, Callable

# From: https://docs.devo.com/confluence/ndt/api-reference/query-api
REGION_MAP = {
    "USA": "https://apiv2-us.devo.com/",
    "EU": "Https://apiv2-eu.devo.com/",
    "VDC (Spain)": "https://apiv2-es.devo.com/",
}

RESPONSE_MAXSIZE = 2e8  # 200 MB in bytes


def request_execution_time(func: Callable):
    def _wrap(*args, **kwargs):
        start_request_time = datetime.datetime.now()
        response = func(*args, **kwargs)
        end_request_time = datetime.datetime.now()
        return response, end_request_time - start_request_time

    return _wrap


class DevoAPI:
    def __init__(self, logger: logging.Logger, api_token: str, region: str):
        self.logger = logger
        self.token = api_token
        self.region = region

        self.base_url = REGION_MAP.get(region)
        if not self.base_url:
            raise PluginException(
                cause="Region not found.",
                assistance=f"The region {self.region} was not recognized, please check your connection input and try again.",
            )

        self.headers = {"Authorization": f"Bearer {self.token}"}

        self.session = requests.Session()

    @request_execution_time
    def query(self, query: str, from_date: str, to_date: str) -> dict:
        endpoint = "/search/query"

        from_epoch = self._convert_time_to_epoch(from_date)
        to_epoch = self._convert_time_to_epoch(to_date)

        post_payload = {
            "query": query,
            "from": from_epoch,
            "to": to_epoch,
            "mode": {"type": "json"},
            "dateFormat": "iso",
            "ipAsString": True,
        }

        results = self._post_to_api(endpoint, post_payload)
        return results

    def test_connection(self):
        """
        This is kind of a cheaty test
        There's not a good "Am I connected" type method in the API
        I send a blank body to the query endpoint and make sure it sends back
        the bad object response instead of an unauthorized (or any other error) response
        """

        try:
            self._post_to_api("/search/query", {})
        except Exception as e:
            if "405" in e.data:
                return "pass"
            else:
                raise ConnectionTestException(ConnectionTestException.Preset.UNAUTHORIZED, data=e)

    #################
    # Private Methods
    #################
    def _convert_time_to_epoch(self, time_string: str) -> int:
        try:
            parsed_time = dateparser.parse(time_string)
        except Exception as e:  # I don't think this will ever happen, leaving as a safeguard.
            raise PluginException(
                cause=f"{time_string} does not appear to be a valid time",
                assistance="Please check your step inputs and try again.",
                data=e,
            )

        if not parsed_time:
            raise PluginException(
                cause=f"{time_string} does not appear to be a valid time",
                assistance="Please check your step inputs and try again.",
            )

        return int(parsed_time.timestamp())

    def _post_to_api(self, endpoint: str, post_body: dict) -> Optional[dict]:
        self.logger.info(f"Starting post to API: {endpoint}")

        # Need this because if it starts with / url join thinks it's a root
        url = urllib.parse.urljoin(self.base_url, endpoint.lstrip("/"))
        try:
            response = self.session.post(url=url, json=post_body, headers=self.headers, stream=True)

            if response.status_code == 400:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance="Bad request or invalid JSON.",
                    data=response.text,
                )
            if response.status_code > 401 and response.status_code < 404:
                raise PluginException(PluginException.Preset.UNAUTHORIZED, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause=f"API Error. API returned {response.status_code}",
                    assistance=f"The object at {url} does not exist.",
                    data=response.text,
                )
            # Success; no content
            if response.status_code == 204:
                return None

            if response.status_code >= 200 and response.status_code < 300:
                self.logger.info("Returning from post to API")
                output = self._get_stream(response)
                return output

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=f"Response was:\n{response.text}")
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Request to {url} failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def _get_stream(self, request: requests.Request) -> dict:
        content = ""
        for chunk in request.iter_content(2048):
            content += chunk.decode()
            if len(content) > RESPONSE_MAXSIZE:
                request.close()
                raise PluginException(
                    cause="Response too large.",
                    assistance="The response received from the server was too large, please edit your input to reduce the returned data size and try again. See the trouble shooting section in the help for this plugin.",
                )

        if content:
            try:
                return json.loads(content)
            except Exception as e:
                raise PluginException(PluginException.Preset.INVALID_JSON)
        else:
            return {}
