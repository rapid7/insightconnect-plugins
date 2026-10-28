import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.base_url = None
        self.headers = None
        self.verify = True

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.ssl_verify = params.get(Input.SSL_VERIFY, True)
        self.url = params.get(Input.URL)
        # END INPUT BINDING - DO NOT REMOVE

        self.base_url = self.url.rstrip("/") if self.url else ""
        self.verify = self.ssl_verify
        self.headers = {
            "User-Agent": "Rapid7-InsightConnect-DECTRAX/1.0.0",
            "Accept": "application/json",
        }
        if self.api_key:
            token = self.api_key.get("secretKey") if isinstance(self.api_key, dict) else self.api_key
            if token:
                self.headers["X-API-Key"] = token

    def test(self):
        test_url = f"{self.base_url}/api/v1/health"
        try:
            response = requests.get(test_url, headers=self.headers, verify=self.verify, timeout=10)
            if response.status_code in [200, 204]:
                return {"success": True}
            raise ConnectionTestException(
                cause=f"DECTRAX returned non-200 status code: {response.status_code}.",
                assistance="Please verify the server URL and API key.",
            )
        except requests.exceptions.RequestException as err:
            raise ConnectionTestException(
                cause=f"Could not connect to DECTRAX instance: {err}",
                assistance="Please check that the server is reachable and SSL configuration is correct.",
            )
