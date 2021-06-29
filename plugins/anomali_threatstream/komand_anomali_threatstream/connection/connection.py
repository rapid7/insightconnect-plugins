import komand
from .schema import ConnectionSchema

# Custom imports below
import requests
from requests import Session, Request
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
from copy import copy
import re
from komand.exceptions import ConnectionTestException, PluginException


class Connection(komand.Connection):
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
            return self.session.send(request.prepare(), verify=request.verify)
        except Exception as e:
            raise PluginException(
                cause=f"The following exception was raised: {self.hide_api_key(str(e))}",
                assistance="Please verify your ThreatStream server status and try again. "
                "If the issue persists please contact support.",
            ) from None  # Suppresses the exception context from the original error that exposes API key

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
