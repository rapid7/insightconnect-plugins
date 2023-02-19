import os
import json
from unittest import mock
from typing import Callable, Optional
from komand_cisco_umbrella_enforcement.connection.schema import Input
import requests

STUB_VERSION_NUMBER = "1.0"
STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_SSL_VERIFY = True
BASE_URL = f"https://s-platform.api.opendns.com/{STUB_VERSION_NUMBER}"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.SSL_VERIFY: STUB_SSL_VERIFY,
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


def mock_conditions(method: str, url: str, status_code: int, domain_id_name: Optional[str] = None) -> MockResponse:
    if url == BASE_URL + "/domains":
        if method == "GET":
            return MockResponse("add_event", status_code)
        if method == "DELETE":
            if domain_id_name == "name":
                return MockResponse("delete_domain_by_name", status_code)
            if domain_id_name == "domain_id":
                return MockResponse("delete_domain_by_id", status_code)
    if url == BASE_URL + f"/events":
        return MockResponse("add_event", status_code)


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
        if status_code == 200:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200, args[2])


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 202, args[2])


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204, args[2])


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400, args[2])


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401, args[2])


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403, args[2])


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404, args[2])


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500, args[2])
