import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
import requests
from typing import Dict, Any


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
        try:
            response = requests.get(
                f"{self.base_url}/cve",
                headers=self.get_headers(),
                params={"page": 1, "page-size": 1},
                timeout=30,
            )
            if response.status_code == 200:
                return {"success": True}
            elif response.status_code == 401:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
            elif response.status_code == 403:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
            elif response.status_code in range(500, 599):
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
            else:
                raise ConnectionTestException(
                    cause=f"Unknown error occurred. Response code: {response.status_code}",
                    assistance="Please verify your API key and region settings.",
                )
        except requests.exceptions.RequestException as e:
            raise ConnectionTestException(
                cause=f"Connection error: {str(e)}",
                assistance="Please check your network connection and try again.",
            )
