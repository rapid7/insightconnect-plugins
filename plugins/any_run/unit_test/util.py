import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

import json

from icon_any_run.connection.connection import Connection
from icon_any_run.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.CREDENTIALS: {"username": "user", "password": "password"},
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
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code) -> None:
                self.filename = filename
                self.status_code = status_code
                self.text = ""

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("params") == {"team": False, "skip": 0, "limit": 25}:
            return MockResponse("get_history", 200)
        if kwargs.get("params") == {"team": True, "skip": 0, "limit": 25}:
            return MockResponse("get_history2", 200)
        if kwargs.get("params") == {"team": False, "skip": 10, "limit": 25}:
            return MockResponse("get_history2", 200)
        if kwargs.get("params") == {"team": False, "skip": 0, "limit": 1}:
            return MockResponse("get_history2", 200)
        if kwargs.get("params") == {"team": False, "skip": 50, "limit": 25}:
            return MockResponse("get_history_empty", 200)
        if args[1] == "https://api.any.run/v1/analysis/44d88612-fea8-a8f3-6de8-2e1278abb02f":
            return MockResponse("get_report", 200)
        if args[1] == "https://api.any.run/v1/analysis/not_found":
            return MockResponse("not_found", 404)
        if kwargs.get("files") == {"file": ("file.txt", b"Rapid7 InsightConnect\n")}:
            return MockResponse("run_analysis", 201)
        if kwargs.get("data", {}).get("obj_url") == "http://example.com":
            return MockResponse("run_analysis", 201)
        if kwargs.get("data", {}).get("obj_url") == "https://upload.example.com/test.png":
            return MockResponse("run_analysis", 201)
        raise Exception("Not implemented")
