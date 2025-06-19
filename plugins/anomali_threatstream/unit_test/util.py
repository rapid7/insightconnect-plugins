import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime

from komand_anomali_threatstream.connection import Connection
from komand_anomali_threatstream.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.USERNAME: "test",
            Input.URL: "https://example.com",
            Input.API_KEY: {"secretKey": "anomali_api_key"},
            Input.SSL_VERIFY: False,
        }
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
    def mock_wrapper(url=""):
        return Util.mock_request(url=url)

    @staticmethod
    def mock_empty_response(**kwargs):
        return MockResponse(200, "get_logs_empty_response.resp", {"link": ""})

    @staticmethod
    def mock_request(*args, **kwargs):
        url = args[0].url
        # Get Observables
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable&limit=1000&offset=0"
        ):
            return MockResponse(200, "get_observables_success.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+400&limit=1000&offset=0"
        ):
            return MockResponse(400, "get_observables_failure.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+401&limit=1000&offset=0"
        ):
            return MockResponse(401, "get_observables_failure.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+403&limit=1000&offset=0"
        ):
            return MockResponse(403, "get_observables_failure.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+404&limit=1000&offset=0"
        ):
            return MockResponse(404, "get_observables_failure.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+409&limit=1000&offset=0"
        ):
            return MockResponse(409, "get_observables_failure.json.resp")
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&value=Example+observable+500&limit=1000&offset=0"
        ):
            return MockResponse(500, "get_observables_failure.json.resp")
        # Get Sandbox Report
        if url == "https://example.com/api/v1/submit/exampleid/report/?username=test&api_key=anomali_api_key":
            return MockResponse(200, "get_sandbox_report_success.json.resp")
        # Import Observables
        if url == "https://example.com/api/v1/intelligence/import/?username=test&api_key=anomali_api_key":
            return MockResponse(200, "import_observable_success.json.resp")
        # Lookup Hash
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&md5=275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f&limit=1000&offset=0"
        ):
            return MockResponse(200, "lookup_hash_success.json.resp")
        # Lookup IP
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&ip=0.0.0.0&limit=1000&offset=0"
        ):
            return MockResponse(200, "lookup_ip_success.json.resp")
        # Lookup URL
        if (
            url
            == "https://example.com/api/v1/intelligence?username=test&api_key=anomali_api_key&url=www.example.com&limit=1000&offset=0"
        ):
            return MockResponse(200, "lookup_url_success.json.resp")
        # Submit File
        if url == "https://example.com/api/v1/submit/new/?username=test&api_key=anomali_api_key":
            return MockResponse(200, "submit_file_success.json.resp")
        # Submit Url
        if url == "https://example.com/api/v1/submit/new":
            return MockResponse(200, "submit_url_success.json.resp")
        raise NotImplementedError("Not implemented", kwargs)


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status_code = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"responses/{filename}")

    def json(self):
        return json.loads(self.text)
