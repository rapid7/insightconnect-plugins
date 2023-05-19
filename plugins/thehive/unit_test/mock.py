import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
from komand_thehive.connection.connection import Connection
from insightconnect_plugin_runtime.action import Action
from constants import STUB_CASE_ID, STUB_CONNECTION_API_KEY, STUB_USER_ID, STUB_BASE_URL

import requests


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION_API_KEY)
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

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:

    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}":
        if method == "GET":
            return MockResponse("get_case", status_code)
        if method == "DELETE":
            return MockResponse("close_case", status_code)
    if url == STUB_BASE_URL + f"/api/case/_search":
        return MockResponse("get_cases", status_code)
    if url == STUB_BASE_URL + f"/api/case":
        return MockResponse("create_case", status_code)
    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}/artifact":
        return MockResponse("create_case_observable", status_code)
    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}/task":
        return MockResponse("create_case_task", status_code)
    if url == STUB_BASE_URL + "/api/user/current":
        return MockResponse("get_current_user", status_code)
    if url == STUB_BASE_URL + f"/api/user/{STUB_USER_ID}":
        return MockResponse("get_user_by_id", status_code)
    raise Exception("Unrecognized endpoint")


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == STUB_BASE_URL:
        if status_code == 200:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("method"), kwargs.get("url"), 500)


def mock_request_200_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 200)


def mock_request_403_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 403)


def mock_request_500_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 500)
