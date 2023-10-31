import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from komand_pagerduty.connection.connection import Connection
from komand_pagerduty.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not params:
            params = {
                Input.API_KEY: {"secretKey": "example-secret-key"},
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
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                self.content = b""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")
                    self.content = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        payload = kwargs.get("json", {})
        url = args[1]
        method = args[0]

        if data:
            data = json.loads(data)
        print(f"{data = }")

        if url == "https://api.pagerduty.com/users/":
            if method == "POST":
                name = payload.get("user", {}).get("name")
                if name == "Test minimum fields":
                    return MockResponse(200, "create_user_minimum_fields.json.resp")
                elif name == "Test additional fields":
                    return MockResponse(200, "create_user_additional_fields.json.resp")
                elif name == "Test api error":
                    return MockResponse(500)
                else:
                    raise NotImplementedError("Not implemented", kwargs)
            elif method == "GET":
                query = params.get("query", {})
                if query == "valid_email":
                    return MockResponse(200, "get_user_by_email_valid.json.resp")
                elif query == "invalid_email":
                    return MockResponse(200, "get_user_by_email_not_found.json.resp")

        elif url == "https://api.pagerduty.com/users/valid_id/":
            if method == "DELETE":
                return MockResponse(204, "")
            elif method == "GET":
                return MockResponse(200, "get_user_valid.json.resp")

        elif url == "https://api.pagerduty.com/users/invalid_id/":
            return MockResponse(404)

        elif url == "https://api.pagerduty.com/incidents/valid_id/" and method == "PUT":
            incident_status = data.get("incident", {}).get("status")
            if incident_status == "resolved":
                return MockResponse(200, "test_resolve_valid.json.resp")
            elif incident_status == "acknowledged":
                return MockResponse(200, "test_acknowledge_valid.json.resp")

        elif url == "https://api.pagerduty.com/incidents/invalid_id/" and method == "PUT":
            return MockResponse(404)

        elif url == "https://api.pagerduty.com/incidents/" and method == "POST":
            title = payload.get("incident", {}).get("title", "")
            if title == "test minimum fields":
                return MockResponse(200, "trigger_event_minimum_fields.json.resp")
            elif title == "test additional fields escalation":
                return MockResponse(200, "trigger_event_additional_fields_escalation.json.resp")
            elif title == "test additional fields assignments":
                return MockResponse(200, "trigger_event_additional_fields_assignments.json.resp")

        elif url == "https://api.pagerduty.com/schedules/no_users/":
            return MockResponse(200, "test_get_on_call_no_users.json.resp")
        elif url == "https://api.pagerduty.com/schedules/user_missing_id/":
            return MockResponse(200, "test_user_missing_id.json.resp")
        elif url == "https://api.pagerduty.com/schedules/user_has_been_deleted/":
            return MockResponse(200, "test_deleted_user.json.resp")
        elif url == "https://api.pagerduty.com/schedules/test_valid_on_call/":
            return MockResponse(200, "test_valid_on_call.json.resp")
        elif url == "https://api.pagerduty.com/schedules/test_cannot_find_user/":
            return MockResponse(200, "test_cannot_find_user.json.resp")

        elif url == "https://api.pagerduty.com/users/PYGDZB8/":
            return MockResponse(200, "valid_get_on_call_user.json.resp")
        elif url == "https://api.pagerduty.com/users/PYGDZB9/":
            return MockResponse(404)

        raise NotImplementedError("Not implemented", kwargs)
