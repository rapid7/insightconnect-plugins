import json
import logging
import os
import sys
from typing import Any, Dict

sys.path.append(os.path.abspath("../"))

from komand_rapid7_intelhub.connection.connection import Connection
from komand_rapid7_intelhub.connection.schema import Input

UNAUTHORIZED_API_KEY = "unauthorized-api-key"
UNLICENSED_API_KEY = "unlicensed-api-key"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": "api-key"},
    Input.REGION: "United States",
}
STUB_UNAUTHORIZED_CONNECTION = {**STUB_CONNECTION, Input.API_KEY: {"secretKey": UNAUTHORIZED_API_KEY}}
STUB_UNLICENSED_CONNECTION = {**STUB_CONNECTION, Input.API_KEY: {"secretKey": UNLICENSED_API_KEY}}
BASE_URL = "https://us.api.insight.rapid7.com/intelligencehub/intelligence-hub/v1"
STUB_CVE_ID = "CVE-2024-3400"
STUB_CVE_ID_WITHOUT_RAPID7_CONTENT = "CVE-2026-103758"
STUB_UNKNOWN_CVE_ID = "CVE-1999-99999"
STUB_THREAT_ACTOR_UUID = "b841ca1d-05d8-488f-ae2f-5bb804720189"
STUB_UNKNOWN_THREAT_ACTOR_UUID = "00000000-0000-0000-0000-000000000000"
STUB_INVALID_LAST_UPDATED = "last 7 days"


class Util:
    @staticmethod
    def default_connector(action: Any, connect_params: Dict[str, Any] = None) -> Any:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(connect_params or STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(**kwargs) -> "MockResponse":
        api_key = kwargs.get("headers", {}).get("X-Api-Key")
        if api_key == UNAUTHORIZED_API_KEY:
            return MockResponse("unauthorized", 401)
        if api_key == UNLICENSED_API_KEY:
            return MockResponse("license_not_found", 401)

        endpoint = kwargs.get("url", "").replace(f"{BASE_URL}/", "")
        if endpoint == "cve" and kwargs.get("params", {}).get("last-updated") == STUB_INVALID_LAST_UPDATED:
            return MockResponse("invalid_filter", 422)

        responses = {
            "cve": ("search_cves", 200),
            f"cve/{STUB_CVE_ID}": ("get_cve", 200),
            f"cve/{STUB_CVE_ID_WITHOUT_RAPID7_CONTENT}": ("get_cve_without_rapid7_content", 200),
            f"cve/{STUB_UNKNOWN_CVE_ID}": ("cve_not_found", 404),
            "threat-actor": ("search_threat_actors", 200),
            f"threat-actor/{STUB_THREAT_ACTOR_UUID}": ("get_threat_actor", 200),
            f"threat-actor/{STUB_THREAT_ACTOR_UUID}/cves": ("get_threat_actor_cves", 200),
            f"threat-actor/{STUB_UNKNOWN_THREAT_ACTOR_UUID}": ("threat_actor_not_found", 404),
            f"threat-actor/{STUB_UNKNOWN_THREAT_ACTOR_UUID}/cves": ("threat_actor_not_found", 404),
        }
        filename, status_code = responses[endpoint]
        return MockResponse(filename, status_code)


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.status_code = status_code
        self.text = Util.read_file_to_string(f"payloads/{filename}.json.resp")

    def json(self) -> Dict[str, Any]:
        return json.loads(self.text)
