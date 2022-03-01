import json
import os
from unittest import mock
from typing import Callable
from icon_carbon_black_response.connection.schema import Input

import requests

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
    if url == BASE_URL:
        if method == "GET":
            return MockResponse("dlGetAll", status_code)
        if method == "POST":
            return MockResponse("dlCreate", status_code)
    if url == BASE_URL + SENSOR_URI + STUB_SENSOR_ID:
        if method == "GET":
            return MockResponse("dlGet", status_code)
        if method == "PUT":
            print("reached")
            return MockResponse("dlPatch", status_code)


# Add other test cases for other actions


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
        if status_code == 200 or status_code == 204:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


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


def mock_request_200_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 200)


def mock_request_403_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 403)


def mock_request_500_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 500)
