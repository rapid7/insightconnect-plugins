import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime

from icon_broadcom_symantec_endpoint_protection.connection import Connection
from icon_broadcom_symantec_endpoint_protection.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.HOST: "sepm-14",
            Input.PORT: 8446,
            Input.CREDENTIALS: {"username": "example", "password": "test"},
            Input.DOMAIN: "example.com",
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
    def mock_request(*args, **kwargs):
        print("ARGS")
        print(args)
        print("KWARGS")
        print(kwargs)
        url = kwargs.get("url", "")
        # Authenticate
        if url == "https://sepm-14:8446/sepm/api/v1/identity/authenticate":
            return MockResponse(200, "authenticate.json.resp")
        # Get agent details
        if url == "https://sepm-14:8446/sepm/api/v1/computers":
            return MockResponse(200, "get_computers.json.resp")
        # Quarantine
        if url == "https://sepm-14:8446/sepm/api/v1/command-queue/quarantine":
            return MockResponse(200, "quarantine.json.resp")
        raise NotImplementedError("Not implemented", kwargs)

    @staticmethod
    async def async_mock_request(*args, **kwargs):
        url = kwargs.get("url", "")
        # Blacklist
        if url == "https://sepm-14:8446/sepm/api/v1/policy-objects/fingerprints":
            return AsyncMockResponse(200, "blacklist_success.json.resp")
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


class AsyncMockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"responses/{filename}")

    async def json(self):
        return json.loads(self.text)
