import requests
import json
from requests import Session, Request, Response
import re
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Dict, Any
from logging import Logger


class API(object):
    def __init__(self, url: str, verify: bool, logger: Logger, headers: Dict):
        self.session = Session()
        self.request = Request()
        self.logger = logger
        self.request.url = url
        self.request.verify = verify
        self.request.headers = headers

    def send(self, request) -> Dict[str, Any]:
        try:
            response = self.session.send(request.prepare(), verify=request.verify)
            self.logger.info(response)
            self.response_handler(response)
            return response.json()
        except json.decoder.JSONDecodeError as exception:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=exception)
        except requests.exceptions.HTTPError as exception:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)

    @staticmethod
    def response_handler(response: Response) -> Response:
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if 200 <= response.status_code < 300:
            return response
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    @staticmethod
    def hide_api_key(api_string: str) -> str:
        """
        ThreatStream queries expose the API key as a URL query parameter. This method hides the API key using a regex that
        substitutes with the replacement the first instance in string of a substring that matches pattern.
        The pattern regex matches the api_key URL query parameter. It captures whether or not another parameter
        follows the api_key value in the group named" "end" with an &. The replacement regex retains the end group.
        """
        pattern = r"api_key=([a-zA-Z0-9]+)(?P<end>\&|$)"
        replacement = r"api_key=********\g<end>"
        return re.sub(pattern, replacement, api_string)
