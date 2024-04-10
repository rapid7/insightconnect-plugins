import uuid

from insightconnect_plugin_runtime.exceptions import PluginException
import requests
from requests import Response
from urllib.parse import quote


class API(object):
    def __init__(self, credentials: str, username: str):
        self.credentials = credentials
        self.username = username

    def check(self, url):
        if self.username:
            headers = {"User-Agent": f"phishtank/{self.username}"}
        else:
            string = "rapid7-plugin-{random_id}"
            self.username = string.format(random_id=uuid.uuid4())
            headers = {"User-Agent": f"phishtank/{self.username}"}

        phishtank_request = requests.post(
            "https://checkurl.phishtank.com/checkurl/",
            data={"format": "json", "url": quote(url), "app_key": self.credentials},
            headers=headers,
            timeout=60,
        )
        if requests.exceptions:
            API.response_handler(phishtank_request)

        try:
            result = phishtank_request.json()
        except requests.exceptions.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=phishtank_request)

        return result

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
        if response.status_code == 409:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
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
