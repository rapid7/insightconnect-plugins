import json
import logging
import sys
import os

import insightconnect_plugin_runtime

from icon_bmc_helix_itsm.util.constants import IncidentRequest, TaskRequest
from icon_bmc_helix_itsm.util.helpers import clean_dict

sys.path.append(os.path.abspath("../"))

from icon_bmc_helix_itsm.connection import Connection
from icon_bmc_helix_itsm.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {
                Input.BASEURL: "https://example-bmc.com:443",
                Input.SSLVERIFY: False,
                Input.USERNAMEPASSWORD: {"password": "my_password", "username": "user"},
            }
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
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
            def __init__(self, status_code: int, response_text: str = None, response_headers: str = None):
                self.status_code = status_code
                self.headers = {}
                self.text = ""
                if response_text:
                    self.text = Util.read_file_to_string(f"responses/{response_text}")
                if response_headers:
                    self.headers = Util.read_file_to_dict(f"responses/{response_headers}")

            def json(self):
                return json.loads(self.text)

        kwargs = clean_dict(kwargs)
        url = kwargs.get("url", "")
        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})

        if url == "https://example-bmc.com:443/api/jwt/login":
            return MockResponse(200, "connection.txt.resp")
        if json_data.get("values", {}).get(IncidentRequest.DESCRIPTION) == "Create Incident Unit test":
            return MockResponse(201, response_headers="create_incident_headers.json.resp")
        if json_data.get("values", {}).get(IncidentRequest.DESCRIPTION) == "Create Incident Unit test - incorrect name":
            return MockResponse(500)
        if (
            url == "https://example.com/INC00002"
            or url == "https://example-bmc.com:443/api/arsys/v1/entry/HPD:Help Desk/INC00002"
        ):
            return MockResponse(200, response_text="incident.json.resp")
        if json_data.get("values", {}).get(IncidentRequest.DESCRIPTION) == "Create Problem Investigation Unit Test":
            return MockResponse(201, response_headers="create_problem_investigation_headers.json.resp")
        if url == "https://example.com/PBI000002":
            return MockResponse(200, response_text="problem.json.resp")
        if (
            json_data.get("values", {}).get(IncidentRequest.DESCRIPTION)
            == "Create Problem Investigation Unit test - incorrect name"
        ):
            return MockResponse(500)
        if params.get("q") == "'Incident Number'=\"INC00002\"":
            return MockResponse(201, response_text="incident_query.json.resp")
        if params.get("q") == "'Incident Number'=\"INC00fake404\"":
            return MockResponse(201, response_text="incident_query_not_found.json.resp")
        if json_data.get("values", {}).get(TaskRequest.NOTES) == "Unit test task notes":
            return MockResponse(201, response_headers="create_task_headers.json.resp")
        if url == "https://example.com/TAS000002":
            return MockResponse(200, response_text="task.json.resp")
        if url == "https://example.com/WLG00002":
            return MockResponse(200, response_text="worklog.json.resp")
        if url == "https://example-bmc.com:443/api/arsys/v1/entry/HPD:IncidentInterface/INC00002|INC00002":
            return MockResponse(204)

        raise NotImplementedError("Not implemented", kwargs)
