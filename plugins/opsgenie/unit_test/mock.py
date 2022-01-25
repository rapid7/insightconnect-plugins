import json
import os
from typing import Callable
from unittest import mock

import requests

STUB_ALERT_ID = "8418d193-2dab-4490-b331-8c02cdd196b7"
STUB_SCHEDULE_ID = "d875alp4-9b4e-4219-alp3-0c26936d18de"


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
    if url == "https://api.opsgenie.com/v2/alerts/":
        return MockResponse("create_alert", status_code)
    elif url == f"https://api.opsgenie.com/v2/alerts/{STUB_ALERT_ID}/close":
        return MockResponse("close_alert", status_code)
    elif url == f"https://api.opsgenie.com/v2/alerts/{STUB_ALERT_ID}":
        return MockResponse("get_alert", status_code)
    elif url == f"https://api.opsgenie.com/v2/schedules/{STUB_SCHEDULE_ID}/on-calls":
        return MockResponse("get_on_calls", status_code)
    elif url == "https://api.opsgenie.com/v2/alerts/count":
        if status_code == 200:
            return MockResponse("test_connection_ok", status_code)
        else:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 202)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)
