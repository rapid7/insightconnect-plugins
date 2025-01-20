import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.action import Action
from komand_duo_auth.connection.connection import Connection
from komand_duo_auth.connection.schema import Input

STUB_CONNECTION = {
    Input.HOSTNAME: "ExampleHostname",
    Input.SECRET_KEY: {"secretKey": "ExampleSecretKey"},
    Input.INTEGRATION_KEY: {"secretKey": "ExampleIntegrationKey"},
}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)
