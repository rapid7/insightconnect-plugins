import json
import logging
import os
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.action import Action
from komand_twilio.connection.connection import Connection
from komand_twilio.connection.schema import Input

STUB_CONNECTION = {
    Input.TWILIO_PHONE_NUMBER: "000111222",
    Input.CREDENTIALS: {"username": "ExampleUsername", "password": "ExamplePassword"},
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
        self.text = json.dumps(self.json(), sort_keys=True)
        self.request = MagicMock()
        self.headers = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)
