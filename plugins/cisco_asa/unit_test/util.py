import json
import logging
import os
from icon_cisco_asa.connection.connection import Connection
from icon_cisco_asa.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://example.com",
            Input.CREDENTIALS: {"password": "password", "username": "user"},
            Input.PORT: 443,
            Input.SSL_VERIFY: True,
            Input.USER_AGENT: "REST API Agent",
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if kwargs.get("json") == {"commands": ["show shun"]}:
            return MockResponse("blocked_hosts", 200)

        raise Exception("Not implemented")
