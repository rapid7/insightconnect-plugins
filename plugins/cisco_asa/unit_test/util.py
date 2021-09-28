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
                if self.filename == "invalid_hostname":
                    self.text = 'Response was: {"response": "Error: Invalid Hostname"}'
                else:
                    self.text = "Error message"

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if kwargs.get("json") == {"commands": ["show shun"]}:
            return MockResponse("blocked_hosts", 200)
        if kwargs.get("json") == {"commands": ["shun 1.1.1.1 0.0.0.0 0 0 0"]}:
            return MockResponse("block_host", 200)
        if kwargs.get("json") == {"commands": ["shun 2.2.2.2 3.3.3.3 333 444 tcp"]}:
            return MockResponse("block_host2", 200)
        if kwargs.get("json") == {"commands": ["shun 2.2.2.2 3.3.3.3 0 0 tcp"]}:
            return MockResponse("block_host2", 200)
        if kwargs.get("json") == {"commands": ["shun 2.2.2.2 0.0.0.0 333 444 tcp"]}:
            return MockResponse("block_host2", 200)
        if kwargs.get("json") == {"commands": ["shun 2.2.2.2 3.3.3.3 333 444 0"]}:
            return MockResponse("block_host2", 200)
        if kwargs.get("json") == {"commands": ["shun 1.1.1.1 999.999.999.999 333 444 tcp"]}:
            return MockResponse("invalid_hostname", 400)
        if kwargs.get("json") == {"commands": ["shun 999.999.999.999 2.2.2.2 333 444 tcp"]}:
            return MockResponse("invalid_hostname", 400)
        if kwargs.get("json") == {"commands": ["no shun 1.1.1.1"]}:
            return MockResponse("unblock_host", 200)
        if kwargs.get("json") == {"commands": ["no shun 999.999.999.999"]}:
            return MockResponse("invalid_hostname", 400)

        raise Exception("Not implemented")
