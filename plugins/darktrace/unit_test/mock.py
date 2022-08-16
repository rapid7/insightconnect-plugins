import json
import os
from typing import Any, Callable, Dict
from unittest import TestCase, mock

import requests
import timeout_decorator

STUB_URL = "https://example.com"
STUB_PRIVATE_API_KEY = "1111111111111111111111111111111111111111"
STUB_PUBLIC_API_KEY = "2222222222222222222222222222222222222222"
STUB_SSL_VERIFICATION = True

STUB_CONNECTION = {
    "url": STUB_URL,
    "api_private_token": {"secretKey": STUB_PRIVATE_API_KEY},
    "api_public_token": {"secretKey": STUB_PUBLIC_API_KEY},
    "ssl_verification": STUB_SSL_VERIFICATION,
}

STUB_RESPONSE_TEXT = "Example Text"


def timeout_pass(error_callback=None):
    def function_timeout(function: Callable):
        def function_wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                return error_callback() if error_callback else None

        return function_wrapper

    return function_timeout


class MockTriggerResponse:
    actual = None

    @staticmethod
    def send(parameters: Dict[str, Any]):
        MockTriggerResponse.actual = parameters


class ErrorChecker:
    expected = {}

    @staticmethod
    def set_expected(expected: Dict[str, Any]):
        ErrorChecker.expected = expected

    @staticmethod
    def check_error():
        if MockTriggerResponse.actual == ErrorChecker.expected:
            return True
        TestCase.assertEqual(MockTriggerResponse.actual, ErrorChecker.expected)


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


def mock_conditions(url: str, status_code: int) -> MockResponse:
    if status_code == 201:
        return MockResponse("invalid_json", status_code, STUB_RESPONSE_TEXT)
    if url == f"{STUB_URL}/status":
        return MockResponse("get_status", status_code, STUB_RESPONSE_TEXT)
    elif url == f"{STUB_URL}/intelfeed":
        return MockResponse("update_watched_domains", status_code, STUB_RESPONSE_TEXT)
    elif url == f"{STUB_URL}/modelbreaches":
        return MockResponse("pull_alerts", status_code, STUB_RESPONSE_TEXT)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 201)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 404)


def mock_request_405(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 405)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)
