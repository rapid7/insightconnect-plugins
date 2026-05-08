import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_anthropic_claude.connection.connection import Connection
from komand_anthropic_claude.connection.schema import Input


class MockResponse:
    def __init__(self, status_code: int, filename: str = None):
        self.status_code = status_code
        self.text = ""
        if filename:
            filepath = os.path.join(os.path.dirname(__file__), "responses", filename)
            with open(filepath) as file:
                self.text = file.read()

    def json(self):
        return json.loads(self.text)


def default_connector(action):
    default_connection = Connection()
    default_connection.logger = logging.getLogger("connection logger")
    params = {
        Input.API_KEY: {"secretKey": "sk-ant-api03-test-key"},
        Input.MODEL: "claude-sonnet-4-6",
    }
    default_connection.connect(params)
    action.connection = default_connection
    action.logger = logging.getLogger("action logger")
    return action
