import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
from komand_domaintools.connection.connection import Connection
from komand_domaintools.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

import requests


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect("api-key")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


class MockResponse:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
          return json.load(file)


def mocked_action(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_responder(*args, **kwargs) -> MockResponse:
    action = args[1]
    _input = args[2]
    if action == "action something":
        if input == "GET":
            return MockResponse("action something")
        if input == "DELETE":
            return MockResponse("action something")

    raise Exception("Unrecognized endpoint")