import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
from icon_infoblox.connection.connection import Connection
from icon_infoblox.connection.schema import Input
from insightconnect_plugin_runtime.action import Action
import requests


STUB_CONNECTION = {
    Input.URL: "https://8.8.8.8",
    Input.CREDENTIALS: {"username": "user", "password": "pass"},
    Input.API_VERSION: "2.7",
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
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()
        self.raise_for_status = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if "ipv4address" in url and status_code == 200:
        return MockResponse("search_by_ip", status_code)

    if "fixedaddress" in url and status_code == 200:
        if method == "GET":
            return MockResponse("search_by_mac", status_code)

    if "record:host" in url and status_code == 200:
        if method == "GET":
            return MockResponse("search_by_name", status_code)

    raise Exception("Unrecognized endpoint")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 200)
