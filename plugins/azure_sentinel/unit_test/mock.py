import json
from pathlib import Path
from typing import Any, Callable, Dict
from unittest import mock

import requests
from requests.models import Response


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        if status_code == 500:
            response = Response()
            response.status_code = 500
            self.to_raise = requests.exceptions.HTTPError(response=response)
        elif status_code == 408:
            self.to_raise = requests.exceptions.Timeout
        else:
            self.to_raise = None
        self.headers = {"content-type": "application/json; charset=utf-8"}

    def raise_for_status(self) -> None:
        if self.to_raise:
            raise self.to_raise
        return

    def json(self) -> Dict[Any, Any]:
        path = Path(__file__).parent / f"payloads/{self.filename}.json"

        with open(path) as file:
            return json.load(file)


def mock_conditions(url: str, status_code: int) -> MockResponse:
    if "oauth2/token" in url:
        return MockResponse("test_connection_ok", status_code)
    elif url == "https://fake.azure.com":
        return MockResponse("test__call_api_ok", status_code)
    elif url == "https://fake.azure.com/invalid":
        return MockResponse("test__call_api_invalid_json", status_code)
    raise Exception(f"Response has been not implemented: {url}")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)


def mock_request_408(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 408)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)
