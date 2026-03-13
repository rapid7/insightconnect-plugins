import json
import logging
import os
from typing import Any, Dict

from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.connection.schema import Input
from insightconnect_plugin_runtime import Action


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")

        params = {
            Input.API_TOKEN: {"secretKey": "1234567890abcdef1234567890abcdef"},
            Input.EMAIL: "test@test.com",
            Input.CLOUD_ID: "123456789",
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
    def read_file_to_bytes(filename: str) -> bytes:
        with open(filename, "rb") as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    class MockResponse:
        def __init__(self, filename: str = None, status_code: int = 200, headers: Dict[str, Any] = None):
            if headers is None:
                headers = {"Content-Type": "application/json"}

            self.status_code = status_code
            self.headers = headers

            if filename:
                self.content = Util.read_file_to_bytes(
                    os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        f"payloads/{filename}.resp",
                    )
                )
                self.text = self.content.decode("utf-8")

        def json(self) -> Dict[str, Any]:
            return json.loads(self.text)

        def raise_for_status(self) -> None:
            if self.status_code >= 400:
                raise Exception(f"HTTP {self.status_code}")
