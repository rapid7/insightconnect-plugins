import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_samanage.connection.connection import Connection
from komand_samanage.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            "phone": "12345",
            "mobile_phone": "1234567",
            "name": "ExampleUser",
            "token": {"secretKey": "Examplesecretkey"},
            "email": "example@user.com",
            "role": "Example role",
            "department": "Example department",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename: str) -> dict:
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str, status_code: int):
                self.filename = filename
                self.status_code = status_code
                self.text = None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

            def raise_for_status(self):
                pass

        if kwargs.get("url") == "https://api.samanage.com/users.json" and kwargs.get("verb") == "POST":
            return MockResponse("create_user", 200)
        if kwargs.get("url") == "https://api.samanage.com/users/5353.json" and kwargs.get("verb") == "DELETE":
            return MockResponse("delete_user", 200)
        if kwargs.get("url") == "https://api.samanage.com/users.json":
            return MockResponse("list_users", 200)
        if kwargs.get("url") == "https://api.samanage.com/attachments.json":
            return MockResponse("attach_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/11111.json":
            return MockResponse("assign_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents.json" and kwargs.get("verb") == "POST":
            return MockResponse("create_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents.json":
            return MockResponse("list_incidents", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/55555.json":
            return MockResponse("tag_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/77777.json":
            return MockResponse("change_incident_state", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/12345.json":
            return MockResponse("get_incident", 200)
        if (
            kwargs.get("url") == "https://api.samanage.com/incidents/676767/comments.json"
            and kwargs.get("verb") == "POST"
        ):
            return MockResponse("comment_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/121212.json" and kwargs.get("verb") == "DELETE":
            return MockResponse("delete_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/6789/comments.json":
            return MockResponse("get_comments", 200)

        raise Exception("Not implemented")


def mock_request_200(*args, **kwargs):
    return Util.mocked_requests(verb=args[0], url=args[1], status_code=200)

