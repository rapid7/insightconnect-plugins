import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from typing import Dict, Any
from komand_rapid7_intelhub.util.api import IntelHubAPI


class Connection(insightconnect_plugin_runtime.Connection):
    REGION_MAP = {
        "United States": "us",
        "Europe": "eu",
        "Canada": "ca",
        "Australia": "au",
        "Japan": "ap",
    }

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.base_url = None

    def connect(self, params={}) -> None:
        self.api_key = params.get(Input.API_KEY, {}).get("secretKey")
        region = params.get(Input.REGION, "United States")
        region_code = self.REGION_MAP.get(region, "us")
        self.base_url = f"https://{region_code}.api.insight.rapid7.com/intelligencehub/intelligence-hub/v1"
        self.logger.info(f"Connect: Connecting to {self.base_url}")

    def get_headers(self) -> Dict[str, str]:
        return {
            "X-Api-Key": self.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def test(self) -> Dict[str, Any]:
        # Searching CVEs checks both the API key and the license, which the health endpoint does not
        try:
            IntelHubAPI(self, self.logger).search_cves(page=1, page_size=1)
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data) from error
        return {"success": True}
