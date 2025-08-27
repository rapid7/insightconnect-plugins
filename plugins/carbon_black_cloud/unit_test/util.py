import json
import os
import sys
from typing import Any, Callable, Dict
from unittest import mock

import requests
import structlog
from icon_carbon_black_cloud.connection.connection import Connection
from icon_carbon_black_cloud.connection.schema import Input

sys.path.append(os.path.abspath("../"))

STUB_CONNECTION = {
    Input.API_ID: "12345",
    Input.API_SECRET_KEY: {"secretKey": "12345"},
    Input.ORG_KEY: "123456",
    Input.URL: "defense.conferdeploy.net",
}
BASE_URL = f"https://{STUB_CONNECTION.get(Input.URL, '')}"


class Util:
    @staticmethod
    def default_connector(action: Any) -> Any:
        default_connection = Connection()
        default_connection.logger = structlog.get_logger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = structlog.get_logger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(filename))


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "Example Text") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        self.headers = {"Header": "Value"}

    def json(self):
        if self.filename == "empty_response":
            return {}
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def raise_for_status(self) -> None:
        raise Exception()


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_conditions(status_code: int, file_name: str = "", **kwargs: Dict[str, Any]) -> MockResponse:
    url = kwargs.get("url")
    if url == f"{BASE_URL}/appservices/v6/orgs/{STUB_CONNECTION.get(Input.ORG_KEY, '')}/devices/_search":
        return MockResponse("get_agent_details", status_code)
    elif url == f"{BASE_URL}/appservices/v6/orgs/{STUB_CONNECTION.get(Input.ORG_KEY, '')}/device_actions":
        return MockResponse("quarantine", status_code)
    elif file_name:
        return MockResponse(file_name, status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(**kwargs) -> MockResponse:
    return mock_conditions(200, **kwargs)


def mock_request_400(**kwargs) -> MockResponse:
    return mock_conditions(400, **kwargs)


def mock_request_401(**kwargs) -> MockResponse:
    return mock_conditions(401, **kwargs)


def mock_request_403(**kwargs) -> MockResponse:
    return mock_conditions(403, **kwargs)


def mock_request_404(**kwargs) -> MockResponse:
    return mock_conditions(404, **kwargs)


def mock_request_409(**kwargs) -> MockResponse:
    return mock_conditions(409, **kwargs)


def mock_request_429(**kwargs) -> MockResponse:
    return mock_conditions(429, **kwargs)


def mock_request_503(**kwargs) -> MockResponse:
    return mock_conditions(503, **kwargs)
