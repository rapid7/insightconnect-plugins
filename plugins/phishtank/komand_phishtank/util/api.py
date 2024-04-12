import uuid

from insightconnect_plugin_runtime.exceptions import PluginException
import requests
from requests import Response
from urllib.parse import quote
from .constants import TIMEOUT, URL

from typing import Dict, Any


class API:
    def __init__(self, credentials: str, username: str) -> None:
        self.credentials = credentials
        self.username = username

    def check(self, url: str) -> Dict[str, Any]:
        if not self.username:
            self.username = f"rapid7-plugin-{uuid.uuid4()}"

        response = requests.post(
            URL,
            data={"format": "json", "url": quote(url), "app_key": self.credentials},
            headers={"User-Agent": f"phishtank/{self.username}"},
            timeout=TIMEOUT,
        )
        try:
            self.response_handler(response)
            return response.json()
        except requests.exceptions.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response)

    def response_handler(self, response: Response) -> None:
        """
        Handles response codes, returning appropriate PluginException Preset
        """
        if 200 <= response.status_code < 300:
            return
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if response.status_code == 409:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        if response.status_code == 429:
            raise PluginException(preset=PluginException.Preset.RATE_LIMIT, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
