import json
import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from icon_manage_engine_service_desk.connection import Connection
from icon_manage_engine_service_desk.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        params = {
            Input.API_KEY: {"secretKey": "valid_api_key"},
            Input.SDP_BASE_URL: "http://me-sdeskplus.example.com:8080",
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
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        if kwargs.get("url").startswith("http://me-sdeskplus.example.com:8080/api/v3/requests/404"):
            return MockResponse(404, "request_not_found.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/notes/404":
            return MockResponse(404, "note_not_found.json.resp")

        if kwargs.get("data"):
            data = kwargs.get("data", {})
            if '"subject": "Add valid request",' in data.get("input_data"):
                return MockResponse(201, "add_request.json.resp")
            if '"subject": "Add invalid request",' in data.get("input_data"):
                return MockResponse(400, "add_request_incorrect_level.json.resp")
            if '"description": "<p>Add request note</p><h1>Hello</h1>",' in data.get("input_data"):
                return MockResponse(201, "add_request_note.json.resp")
            if '"content": "Add resolution",' in data.get("input_data"):
                return MockResponse(201, "add_resolution.json.resp")
            if '"requester_ack_comments": "Close request",' in data.get("input_data"):
                return MockResponse(201, "close_request.json.resp")
            if '"requester_ack_comments": "Request already closed",' in data.get("input_data"):
                return MockResponse(400, "close_request_request_already_closed.json.resp")
            if '"name": "Assign request"' in data.get("input_data"):
                return MockResponse(200, "assign_request.json.resp")
            if '"subject": "Edit request",' in data.get("input_data"):
                return MockResponse(200, "edit_request.json.resp")

        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests" and kwargs.get("params"):
            if "not_existing_filter" in kwargs.get("params", {}).get("input_data"):
                return MockResponse(400, "get_list_request_invalid_filter.json.resp")
            return MockResponse(200, "get_list_request.json.resp")

        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/move_to_trash":
            return MockResponse(200, "delete_request.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/400/move_to_trash":
            return MockResponse(400, "delete_request_request_already_deleted.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/notes/200":
            return MockResponse(200, "delete_request_note.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/notes/201":
            return MockResponse(200, "edit_request_note.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/notes":
            return MockResponse(200, "get_list_request_notes.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/201":
            return MockResponse(200, "get_request.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/201/resolutions":
            return MockResponse(200, "get_resolution.json.resp")
        if kwargs.get("url") == "http://me-sdeskplus.example.com:8080/api/v3/requests/200/pickup":
            return MockResponse(200, "pickup_request.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
