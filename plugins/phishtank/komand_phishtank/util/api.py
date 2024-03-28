import logging
import xml

import insightconnect_plugin_runtime
import urllib3.util
import xml

import komand_phishtank.connection
import insightconnect_plugin_runtime.helper
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
from requests import Response
import json
import base64
import urllib.parse

from komand_phishtank.connection.schema import Input, ConnectionSchema


class API(object):
    def __init__(self, credentials):
        self.credentials = credentials

    def check(self, url):
        try:
            # add exception handling for post request - url exception ?
            print(f"URL: {url}")
            print(f"CREDS: {self.credentials}")
            print(f"URL CONTENT {url.__dict__}")
            r = requests.post(
                "https://checkurl.phishtank.com/checkurl/",
                data={
                    "format": "json",
                    "url": urllib.parse.quote(url),
                    "app_key": Input.CREDENTIALS
                },
            )
            print(r.__dict__)
            result = r.json()["results"]
            # add a json decode error ?

            if result.get("phish_detail_page"):
                result["phish_detail_url"] = result["phish_detail_page"]
                del result["phish_detail_page"]
            return result

        except requests.exceptions.HTTPError as exception:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)

    def response_handler(response: Response) -> Response:
        """
        Handles response codes, returning appropriate PluginException Preset
        """
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if response.status_code == 429:
            raise PluginException(cause="Too Many Requests", assistance="With no API key, phishtank does not support"
                                        "more than a few requests per day. Please try again later")
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if 200 <= response.status_code < 300:
            return response
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    # data={
    #     "url": urllib.parse.quote_plus(str(url)),
    #     "format": "json",
    #     "app_key": Input.CREDENTIALS
    #     # .get(Input.CREDENTIALS).get("secretKey")
    #     # "app_key": Input.CREDENTIALS.get("secretKey")
    #     # "url": urllib3.util.parse_url(url)
    # },
