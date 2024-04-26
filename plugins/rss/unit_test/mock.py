import json
from typing import Any, Callable, Dict
from unittest.mock import MagicMock

import requests


class MockSender:
    def __init__(self) -> None:
        self.response = None

    def send(self, payload: Dict[str, Any]) -> None:
        self.response = json.loads(json.dumps(payload))


class MockResponse:
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if not 200 <= self.status_code < 300:
            raise requests.exceptions.HTTPError(response=self)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = MagicMock(side_effect=side_effect)


def mock_conditions(status_code: int) -> MockResponse:
    return MockResponse(status_code)


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(200)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(400)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(500)


def mock_request_501(*args, **kwargs) -> MockResponse:
    return mock_conditions(501)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(503)
