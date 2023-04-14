import json
import os
from typing import Callable
from unittest import mock

import requests
from icon_threatcrowd.connection.schema import Input

STUB_CONNECTION = {Input.SSL_VERIFICATION: True}

STUB_RESPONSE_TEXT = "RESPONSE"


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = STUB_RESPONSE_TEXT) -> None:
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
        return MockResponse("invalid_json", status_code)
    elif status_code == 401:
        return MockResponse("empty_response", status_code)
    if url == "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=54.192.230.36":
        return MockResponse("empty_response", status_code)
    elif url == "https://www.threatcrowd.org/searchApi/v2/ip/report/":
        return MockResponse("address", status_code)
    elif url == "https://www.threatcrowd.org/searchApi/v2/antivirus/report/":
        return MockResponse("av", status_code)
    elif url == "https://www.threatcrowd.org/searchApi/v2/domain/report/":
        return MockResponse("domain", status_code)
    elif url == "https://www.threatcrowd.org/searchApi/v2/email/report/":
        return MockResponse("email", status_code)
    elif url == "https://www.threatcrowd.org/searchApi/v2/file/report/":
        return MockResponse("hash", status_code)
    elif url == "https://www.threatcrowd.org/vote.php":
        return MockResponse("empty_response", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 201)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 401)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 503)
