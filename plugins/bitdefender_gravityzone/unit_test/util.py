import json
import logging
import os

from komand_bitdefender_gravityzone.connection.connection import Connection
from komand_bitdefender_gravityzone.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://cloud.gravityzone.bitdefender.com",
            Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = ""

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)),
                            f"payloads/{self.filename}.json.resp",
                        )
                    )
                )

            def raise_for_status(self):
                if self.status_code >= 400:
                    from requests.exceptions import HTTPError

                    raise HTTPError(f"HTTP {self.status_code}")

        json_payload = kwargs.get("json", {})
        method = json_payload.get("method", "")

        if method == "getApiKeyDetails":
            return MockResponse("test_connection", 200)
        elif method == "getEndpointsList":
            # Check if there's a name filter for empty results
            params = json_payload.get("params", {})
            filters = params.get("filters", {})
            if filters.get("name", {}).get("value") == "nonexistent*":
                return MockResponse("get_endpoints_list_empty", 200)
            return MockResponse("get_endpoints_list", 200)
        elif method == "createIsolateEndpointTask":
            params = json_payload.get("params", {})
            endpoint_id = params.get("endpointId", "")
            if endpoint_id == "invalid_endpoint_id_000000":
                return MockResponse("isolate_endpoint_error", 200)
            return MockResponse("isolate_endpoint_success", 200)

        return MockResponse("test_connection", 200)
