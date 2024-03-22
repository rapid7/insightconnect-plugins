from komand_cherwell.connection import Connection
from komand_cherwell.connection.schema import Input
import insightconnect_plugin_runtime
import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

STUB_URL = "http://0.0.0.0:0000"
STUB_AUTHENTICATION_MODE = "Internal"
STUB_CLIENT_ID = "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99"
STUB_USERNAME_AND_PASSWORD = {"username": "user@example.com", "password": "mypassword"}

class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
          Input.URL: STUB_URL,
          Input.CLIENT_ID: STUB_URL,
          Input.SSL_VERIFY: False,
          Input.AUTHENTICATION_MODE: STUB_AUTHENTICATION_MODE,
          Input.USERNAME_AND_PASSWORD: STUB_USERNAME_AND_PASSWORD,
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
    def mock_request(*args, **kwargs):
        url = kwargs.get("url")
        # Create Incident
        if url == f"{STUB_URL}/CherwellAPI/api/V1/SaveBusinessObject":
            return MockResponse(200, "create_incident_success.json.resp")
        # Lookup Incident
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/1":
            return MockResponse(200, "lookup_incident_success.json.resp")
        # Perform Ad Hoc Search
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getsearchresults":
            return MockResponse(200, "get_search_results_success.json.resp")
        # Update Incident
        if url == f"{STUB_URL}/CherwellAPI/api/V1/SaveBusinessObject":
            return MockResponse(200, "update_incident_success.json.resp")
        # Error Handling
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/400":
            return MockResponse(400, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/401":
            return MockResponse(401, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/403":
            return MockResponse(403, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/404":
            return MockResponse(404, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/418":
            return MockResponse(418, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/500":
            return MockResponse(500, "error.json.resp")
        if url == f"{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/202":
            return MockResponse(202, "error.json.resp")
        raise NotImplementedError("Not implemented", kwargs)


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status_code = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"responses/{filename}")
            self.content = bytes(Util.read_file_to_string(f"responses/{filename}"), "utf-8")

    def json(self):
        return json.loads(self.text)