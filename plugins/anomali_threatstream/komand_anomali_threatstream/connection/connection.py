import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import logging
from copy import copy
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from ..util.api import API


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        # Silence warnings and request logging
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        logging.getLogger("urllib3").setLevel(logging.CRITICAL)

        username, threatstream_url, api_key = (
            params["username"],
            params["url"],
            params["api_key"]["secretKey"],
        )
        self.api = API(
            url=f"{threatstream_url}/api",
            verify=params.get("ssl_verify"),
            logger=self.logger,
            headers={"Authorization": f"apikey {username}:{api_key}"},
        )
        # Set up the base request

    def test(self):
        self.api.request = copy(self.api.request)
        self.api.request.url, self.api.request.method = self.api.request.url + "/v2/intelligence", "GET"

        response = self.api.session.send(self.api.request.prepare(), verify=self.api.request.verify)

        if response.status_code not in range(200, 299):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.INVALID_JSON, data=response.text)

        return {"connection": "Successful"}
