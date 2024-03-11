import json
import os
from typing import Callable
from unittest import mock

import requests
from icon_cisco_ise.connection.schema import Input

from utils import STUB_CONNECTION

BASE_URL = f"https://{STUB_CONNECTION.get(Input.ADDRESS, '')}:9060/ers"


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        self.reason = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable, method: str) -> None:
    mock_function = requests
    setattr(mock_function, method, mock.Mock(side_effect=side_effect))


def mock_conditions(url: str, status_code: int) -> MockResponse:
    print(url)
    if url in (f"{BASE_URL}/config/ancendpoint", f"{BASE_URL}/config/ancendpoint/"):
        return MockResponse("get_anc_endpoint_all", status_code)
    elif url == f"{BASE_URL}/config/ancendpoint/1":
        return MockResponse("get_anc_endpoint_by_id", status_code)
    elif url in (f"{BASE_URL}/config/ancendpoint/apply", f"{BASE_URL}/config/ancendpoint/clear"):
        return MockResponse("anc_endpoint_apply", status_code)
    elif url == f"{BASE_URL}/config/endpoint/name/ExampleHostname":
        return MockResponse("get_endpoint_by_name", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 200)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 401)
