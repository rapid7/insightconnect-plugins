import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import requests
import json
from requests import Session, Request, Response
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
from copy import copy
import re
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session = Session()
        self.request = Request()

    def connect(self, params):
        # Silence warnings and request logging
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)

        username, threatstream_url, api_key = (
            params["username"],
            params["url"],
            params["api_key"]["secretKey"],
        )
        # Set up the base request
        self.request.url = threatstream_url + "/api/v1"
        self.request.verify = params.get("ssl_verify")
        self.request.params = {"username": username, "api_key": api_key}

    def test(self):
        self.request = copy(self.request)
        self.request.url, self.request.method = self.request.url + "/intelligence", "GET"

        response = self.session.send(self.request.prepare(), verify=self.request.verify)

        if response.status_code not in range(200, 299):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON, data=response.text)

        return {"connection": "successful"}

    def send(self, request):
        try:
            response = self.session.send(request.prepare(), verify=request.verify)
            self.logger.info(response)
            self.response_handler(response)
            return response
        except json.decoder.JSONDecodeError as exception:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=exception)
        except requests.exceptions.HTTPError as exception:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)

    @staticmethod
    def response_handler(response: Response) -> Response:
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
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
    def hide_api_key(string):
        """
        ThreatStream queries expose the API key as a URL query parameter. This method hides the API key using a regex that
        substitutes with the replacement the first instance in string of a substring that matches pattern.
        The pattern regex matches the api_key URL query parameter. It captures whether or not another parameter
        follows the api_key value in the group named" "end" with an &. The replacement regex retains the end group.
        """
        pattern = r"api_key=([a-zA-Z0-9]+)(?P<end>\&|$)"
        replacement = r"api_key=********\g<end>"
        return re.sub(pattern, replacement, string)
