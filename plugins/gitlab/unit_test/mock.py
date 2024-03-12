import json
import logging
import os
from typing import Callable
from unittest import mock
import requests
from insightconnect_plugin_runtime.action import Action
from icon_gitlab.connection.connection import Connection
from icon_gitlab.connection.schema import Input

STUB_CONNECTION = {
    Input.URL: "https://example.com",
    Input.CREDENTIALS: {"username": "user", "password": "pass"},
    Input.SSL_VERIFY: True,
}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("Connection Logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("Action Logger")
        return action


class MockResponse:
    def __init__(self, filename: str, status_code: 200) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if url == "https://example.com/api/v4/users/123":
        if method == "GET":
            return MockResponse("get_user", status_code)
        if method == "DELETE":
            return MockResponse("delete_user", status_code)
    if url == "https://example.com/api/v4/users/123/block":
        return MockResponse("block_user", status_code)
    if url == "https://example.com/api/v4/projects/123/issues":
        return MockResponse("create_issue", status_code)
    if url == "https://example.com/api/v4/users/123/keys/123":
        return MockResponse("delete_ssh", status_code)
    if url == "https://example.com/api/v4/users/123/keys":
        return MockResponse("list_ssh", status_code)
    if url == "https://example.com/api/v4/users/123/unblock":
        return MockResponse("unblock_user", status_code)

    raise Exception("Unrecognised Endpoint")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)
