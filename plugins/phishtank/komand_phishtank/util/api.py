import logging
import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.exceptions import PluginException
import requests
from requests import Response
import json
from urllib.parse import quote


class API(object):
    def __init__(self, credentials: str):
        self._credentials = credentials

    def check(self, url):
        try:
            r = requests.post(
                "https://checkurl.phishtank.com/checkurl/",
                data={"format": "json", "url": quote(url), "app_key": self._credentials},
                timeout=60,
            )

            try:
                result = r.json()
            except requests.exceptions.JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.UNKNOWN)

            if requests.exceptions:
                API.response_handler(r)

            if "phish_detail_page" in result:
                result["phish_detail_url"] = result["phish_detail_page"]
                del result["phish_detail_page"]
            if "verified_at" in result:
                if result["verified_at"] is None:
                    result["verified_at"] = str(result["verified_at"])

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
            raise PluginException(
                cause="Too Many Requests",
                assistance="With no API key, phishtank does not support"
                "more than a few requests per day. Please try again later",
            )
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if 200 <= response.status_code < 300:
            return response
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
