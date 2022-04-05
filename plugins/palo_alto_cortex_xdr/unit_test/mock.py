import json
import os
from typing import Callable
from unittest import mock
from icon_palo_alto_cortex_xdr.connection.schema import Input

import requests

STUB_API_KEY_ID = "1"
STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_SECURITY_LEVEL = "Standard"
STUB_URL = "https://example.com/"

STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.API_KEY_ID: STUB_API_KEY_ID,
    Input.SECURITY_LEVEL: STUB_SECURITY_LEVEL,
    Input.URL: STUB_URL,
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
    mock_function.post = mock.Mock(side_effect=side_effect)


def mock_conditions(url: str, status_code: int) -> MockResponse:
    if url == STUB_URL + "public_api/v1/xql/start_xql_query/":
        return MockResponse("start_xql_query", status_code)
    if url == STUB_URL + "public_api/v1/xql/get_query_results/":
        return MockResponse("get_query_results", status_code)


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 200)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 404)


def mock_request_402(*args, **kwargs) -> MockResponse:
    return mock_conditions(kwargs.get("url"), 402)
