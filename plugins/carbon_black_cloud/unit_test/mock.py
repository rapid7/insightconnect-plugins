import json
import os
from typing import Any, Callable, Dict
from unittest import mock

import requests

STUB_CONNECTION = {"client_id": "1234", "client_secret": {"secretKey": "1234"}, "tenant_id": "123"}


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self) -> Dict[str, Any]:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def raise_for_status(self) -> None:
        raise Exception


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.post = mock.Mock(side_effect=side_effect)


def mock_conditions(url: str, status_code: int, *args, **kwargs) -> MockResponse:
    if url == "https://example.com/appservices/v6/orgs/12345/devices/_search":
        if kwargs.get("json", {}).get("query", "") == "ExampleAgent2":
            status_code = 404
        return MockResponse("get_user_agent", status_code)
    elif url == "https://example.com/appservices/v6/orgs/12345/device_actions":
        return MockResponse("quarantine", status_code)
    raise Exception("Response has been not implemented")


def mock_request_201(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 201, **kwargs)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 400, **kwargs)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 401, **kwargs)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 403, **kwargs)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 404, **kwargs)


def mock_request_409(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 409, **kwargs)
