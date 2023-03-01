import json
import logging
import os
import sys
from typing import Callable

import requests

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import mock

from komand_microsoft_atp.connection.connection import Connection
from komand_microsoft_atp.connection.schema import Input

STUB_CONNECTION = {
    Input.DIRECTORY_ID: "12345",
    Input.APPLICATION_ID: {"secretKey": "12345"},
    Input.APPLICATION_SECRET: {"secretKey": "12345"},
}
RESOURCE_URL = "https://api.securitycenter.windows.com/api/"


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "Example Text") -> None:
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


def mock_conditions(method: str, url: str, status_code: int, **kwargs: Dict[str, Any]) -> MockResponse:
    if status_code == 201:
        return MockResponse("test_invalid_json_response", status_code)
    if "oauth2/token" in url:
        return MockResponse("test_get_auth_token", status_code)
    if url == f"{RESOURCE_URL}alerts?$top=1":
        return MockResponse("test_get_alerts", status_code)
    if url == f"{RESOURCE_URL}machines/1234":
        return MockResponse("test_get_machine_information_by_id", status_code)
    if f"{RESOURCE_URL}machines" in url:
        filter_parameter = kwargs.get("params", {}).get("$filter", "")
        if "computerDnsName" in filter_parameter or "lastIpAddress" in filter_parameter:
            return MockResponse("test_get_machine_information_second", status_code)
        return MockResponse("test_get_machine_information_first", status_code)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200, **kwargs)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201, **kwargs)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401, **kwargs)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403, **kwargs)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404, **kwargs)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500, **kwargs)
