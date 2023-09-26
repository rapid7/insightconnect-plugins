import json
import logging
import os
import sys
from typing import Callable

import requests

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import mock

from icon_carbon_black_cloud.connection.connection import Connection
from icon_carbon_black_cloud.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    Input.API_ID: "12345",
    Input.API_SECRET_KEY: {"secretKey": "12345"},
    Input.ORG_KEY: "123456",
    Input.URL: "defense.conferdeploy.net",
}
BASE_URL = f"https://{STUB_CONNECTION.get(Input.URL, '')}"


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
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

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def raise_for_status(self) -> None:
        raise Exception()


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.post = mock.Mock(side_effect=side_effect)


def mock_conditions(url: str, status_code: int, **kwargs: Dict[str, Any]) -> MockResponse:
    if url == f"{BASE_URL}/appservices/v6/orgs/{STUB_CONNECTION.get(Input.ORG_KEY, '')}/devices/_search":
        return MockResponse("get_agent_details", status_code)
    elif url == f"{BASE_URL}/appservices/v6/orgs/{STUB_CONNECTION.get(Input.ORG_KEY, '')}/device_actions":
        return MockResponse("quarantine", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 200, **kwargs)


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


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], 503, **kwargs)
