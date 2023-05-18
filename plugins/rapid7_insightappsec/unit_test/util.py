import json
import logging
import sys
import os
import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_rapid7_insightappsec.connection import Connection
from komand_rapid7_insightappsec.connection.schema import Input


class Meta:
    version = "1.0.0"


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {Input.API_KEY: {"secretKey": "api_key"}, Input.URL: "https://example.com"}
        default_connection.meta = Meta()
        default_connection.connect(params)
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
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        url = kwargs.get("url")
        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})

        if url == "https://example.com/ias/v1/search":
            if params == {"size": 1000, "index": 1}:
                return MockResponse(200, "search_vulnerabilities_second_page.json.resp")
            if params == {"size": 1000, "index": 2}:
                return MockResponse(200, "search_vulnerabilities_empty.json.resp")
            return MockResponse(200, "search_vulnerabilities_first_page.json.resp")
        if (
            url == "https://example.com/ias/v1/schedules"
            and json_data.get("rrule") == "FREQ=MONTHLY;INTERVAL=1;BYDAY=FR;BYSETPOS=-1"
        ):
            return MockResponse(201)
        if url == "https://example.com/ias/v1/schedules":
            return MockResponse(201)

        if url.endswith("ias/v1/vulnerabilities/existing-ID"):
            return MockResponse(200, "get_vulnerability.json.resp")

        if url.endswith("ias/v1/vulnerabilities/"):
            if params.get("page-token") == "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz":
                return MockResponse(200, "get_vulnerabilities_all_params.json.resp")
            if params == {}:
                return MockResponse(200, "get_vulnerabilities_no_params.json.resp")

        if url.endswith(
            "vulnerabilities/58972aa5-aa97-455e-90b7-cf569dbd75d5/discoveries/58972aa5-aa97-455e-90b7" "-cf569dbd75d0"
        ):
            return MockResponse(200, "get_vulnerability_discovery_valid.json.resp")
        if url.endswith("vulnerabilities/58972aa5-aa97-455e-90b7-cf569dbd75d5/discoveries"):
            return MockResponse(200, "get_vulnerability_discoveries_valid.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
