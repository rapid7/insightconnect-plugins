import json
import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_sentinelone_active_response.actions.execute_response.action import ExecuteResponse
from komand_sentinelone_active_response.connection.connection import Connection
from unittest.mock import MagicMock, patch

RESPONSES_DIR = os.path.join(os.path.dirname(__file__), "responses")


class MockResponse:
    """Mock HTTP response for testing API client."""

    def __init__(self, status_code, filename=None, data=None):
        self.status_code = status_code
        self.text = ""
        if filename:
            filepath = os.path.join(RESPONSES_DIR, filename)
            with open(filepath, "r") as f:
                self._json_data = json.load(f)
                self.text = json.dumps(self._json_data)
        elif data:
            self._json_data = data
            self.text = json.dumps(data)
        else:
            self._json_data = {}

    def json(self):
        return self._json_data


def default_connector(action=None):
    """Set up an action with a mocked connection client."""
    if action is None:
        action = ExecuteResponse()

    connection = Connection()
    connection.logger = MagicMock()
    connection.client = MagicMock()

    action.connection = connection
    action.logger = MagicMock()

    return action
