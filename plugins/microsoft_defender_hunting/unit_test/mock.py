import json
import os
from typing import Callable
from unittest import mock

import requests

from icon_microsoft_defender_hunting.util.endpoints import Endpoint

STUB_CONNECTION = {"client_id": "1234", "client_secret": {"secretKey": "1234"}, "tenant_id": "123"}


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
    if status_code == 201:
        return MockResponse("test_invalid_json_response", status_code)
    if "oauth2/token" in url:
        return MockResponse("test_get_auth_token", status_code)
    if url == Endpoint.ADVANCED_HUNTING:
        return MockResponse("test_advanced_hunting", status_code)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_429(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 429)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 503)


def mock_request_505(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 505)
