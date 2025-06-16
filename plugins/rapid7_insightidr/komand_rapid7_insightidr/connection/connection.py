import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
import requests
from komand_rapid7_insightidr.util.endpoints import Investigations


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None
        self.headers = {}
        self.cloud_log_values = {}   # todo- this should be removed or populated in request helper properly

    def connect(self, params={}):
        api_key = params.get(Input.API_KEY).get("secretKey")

        self.region = params.get(Input.REGION)
        self.url = Investigations.connection_api_url(self.region)

        if not self.url.endswith("/"):
            self.url = f"{self.url}/"

        self.headers = {
            "X-Api-Key": api_key,
            "Accept-version": "investigations-preview",
            "User-Agent": "test-version" if not hasattr(self, "meta.version") else self.meta.version
        }

        self.logger.info(f"Connect: Connecting...")

    def test(self):
        response = requests.get(f"{self.url}validate", headers=self.headers)
        if response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        if response.status_code in range(500, 599):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(response.text)
            raise ConnectionTestException(
                cause=f"An unknown error occurred." f" InsightIDR responded with a {response.status_code} code.",
                assistance="See log for more details. If the problem persists, please contact support.",
            )
