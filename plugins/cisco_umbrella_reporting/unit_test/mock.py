import sys

sys.path.append("../")

import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock

import requests
from icon_cisco_umbrella_reporting.connection.connection import Connection
from icon_cisco_umbrella_reporting.connection.schema import Input
from icon_cisco_umbrella_reporting.util.endpoints import Endpoints
from insightconnect_plugin_runtime.action import Action

STUB_API_KEY = "12345688765432"
STUB_API_SECRET = "12345678987654"

STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.API_SECRET: {"secretKey": STUB_API_SECRET},
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

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests.Session
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if method == "POST":
        if url == Endpoints.OAUTH20_TOKEN_URL and status_code == 200:
            return MockResponse("oauth2_token", status_code)
        return MockResponse("invalid_json", status_code)
    elif method == "GET":
        if status_code == 201:
            return MockResponse("invalid_json", status_code)
        if url == "https://api.umbrella.com/reports/v2/activity/dns":
            return MockResponse("get_domain_visits", status_code)
    raise Exception("Response has not been implemented")


def mock_request_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201)


def mock_request_200(*args, **kwargs) -> MockResponse:
    method = kwargs.get("method") if not args else args[0]
    url = kwargs.get("url") if not args else args[1]
    return mock_conditions(method, url, 200)


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 202)


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500)
