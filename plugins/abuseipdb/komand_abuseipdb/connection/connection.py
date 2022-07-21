import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import json
import requests


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.base = None
        self.headers = None

    def connect(self, params):
        self.api_key = params.get("credentials").get("secretKey")
        self.base = "https://api.abuseipdb.com/api/v2"
        self.headers = {"Accept": "application/json", "Key": self.api_key}
        self.logger.info(f"Connect: Connecting to {self.base}...")

    def test(self):
        # Use private IP Addresses for testing the API (e.g. 127.0.0.1) from https://www.abuseipdb.com/api
        url = "https://api.abuseipdb.com/api/v2/check"
        params = {"ipAddress": "127.0.0.0"}
        try:
            response = requests.get(url, params=params, headers=self.headers)
            json_ = response.json()
        except json.decoder.JSONDecodeError:
            raise ConnectionTestException(
                cause="Received an unexpected response from AbuseIPDB.",
                assistance=f"(non-JSON or no response" f" was received). Response was: {response.text}",
            )
        except Exception as error:
            self.logger.error(error)
            raise
        if response.status_code not in range(200, 299):
            raise ConnectionTestException(
                cause="Received an unexpected response from AbuseIPDB.",
                assistance=f"(unexpected response was received). Response was: {response.text}; Status Code was: {response.status_code}",
            )
        return json_
