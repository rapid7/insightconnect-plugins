import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

import requests


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.base = "https://webrisk.googleapis.com/v1beta1/"
        self.key = params.get("credentials").get("secretKey")

    def test(self):
        test_url = f"{self.base}uris:search"
        parameters = {"key": self.key, "uri": "google.com", "threatTypes": ["MALWARE"]}
        response = requests.get(test_url, params=parameters)
        if response.status_code != 200:
            raise ConnectionTestException(cause=ConnectionTestException.Preset.API_KEY)
