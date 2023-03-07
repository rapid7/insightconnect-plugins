import os
import json
from unittest import mock
from typing import Callable, Optional
from icon_cisco_umbrella_reporting.connection.schema import Input
import requests

STUB_API_KEY = "12345688765432"
STUB_API_SECRET = "12345678987654"
STUB_ORG_ID = "1234567"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.API_SECRET: {"secretKey": STUB_API_SECRET},
    Input.ORGANIZATION_ID: STUB_ORG_ID,
}


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    return MockResponse("get_domain_visits", status_code)


def mock_conditions_connection(status_code: int) -> MockResponse:
    if status_code == 200:
        return MockResponse("test_connection_ok", status_code)
    elif status_code >= 400:
        return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


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
