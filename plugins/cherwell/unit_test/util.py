from komand_cherwell.connection import Connection
from komand_cherwell.connection.schema import Input
import insightconnect_plugin_runtime
import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

STUB_URL = "0.0.0.0"
STUB_AUTHENTICATION_MODE = "Internal"
STUB_CLIENT_ID = {"secretKey": "a5zy0a6g-504e-46bz-84xx-1b3f5ci36l99"}
STUB_USERNAME_AND_PASSWORD = {"username": "user@example.com", "password": "mypassword"}
STUB_QUERY_PARAMS = "?auth_mode=Internal"


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: STUB_URL,
            Input.CLIENT_ID: STUB_CLIENT_ID,
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
        url = args[0].url
        if url == f"http://{STUB_URL}/CherwellAPI/token{STUB_QUERY_PARAMS}":
            return MockResponse(200, "token.json.resp")
        # Create Incident
        if url == f"http://{STUB_URL}/CherwellAPI/api/V1/SaveBusinessObject":
            return MockResponse(200, "create_incident_success.json.resp")
        if url == f"http://{STUB_URL}/CherwellAPI/api/V1/GetBusinessObjectTemplate":
            return MockResponse(200, "get_business_object_template.json.resp")
        # Lookup Incident
        if url == f"http://{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/1":
            return MockResponse(200, "lookup_incident_success.json.resp")
        # Perform Ad Hoc Search
        if url == f"http://{STUB_URL}/CherwellAPI/api/V1/getsearchresults":
            return MockResponse(200, "perform_ad_hoc_search_success.json.resp")
        # Update Incident
        if url == f"http://{STUB_URL}/CherwellAPI/api/V1/SaveBusinessObject":
            return MockResponse(200, "update_incident_success.json.resp")
        # Error Handling
        status_codes = [400, 401, 403, 404, 409, 500, 202]
        for status_code in status_codes:
            if url == f"http://{STUB_URL}/CherwellAPI/api/V1/getbusinessobject/busobid/1/publicid/{status_code}":
                return MockResponse(status_code, "error.json.resp")
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
