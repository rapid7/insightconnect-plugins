import json
import os
import logging
from typing import Callable
import requests

from unittest import mock

from icon_zoom.actions.create_user.schema import Input
from icon_zoom.connection.connection import Connection
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    "client_id": {"secretKey": "asdf"},
    "client_secret": {"secretKey": "asdf"},
    "account_id": {"secretKey": "asdf"},
}
STUB_BASE_URL = "https://api.zoom.us/v2"
STUB_OAUTH_URL = "https://zoom.us/oauth/token"
STUB_USER_ID = "user@example.com"
STUB_OAUTH_TOKEN = "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3"
STUB_CREATE_USER = {
    Input.ACTION: "create",
    Input.TYPE: "Basic",
    Input.EMAIL: "user@example.com",
    Input.FIRST_NAME: "FirstName",
    Input.LAST_NAME: "LastName",
}

REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"


class Util:
    @staticmethod
    @mock.patch(REFRESH_OAUTH_TOKEN_PATH)
    def default_connector(action: Action, mock_refresh_call) -> Action:
        mock_refresh_call.return_value = None
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        default_connection.zoom_api.oauth_token = STUB_OAUTH_TOKEN
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


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


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if url == STUB_OAUTH_URL:
        return MockResponse("oauth2_token", status_code)
    if method == "GET":
        return MockResponse("get_user", status_code)
    if method == "POST":
        return MockResponse("create_user", status_code)
    if method == "DELETE":
        return MockResponse("delete_user", status_code)
    raise Exception("Unrecognized endpoint")


def mock_request_201(*args, **kwargs) -> MockResponse:
    method = kwargs.get("method") if not args else args[0]
    url = kwargs.get("url") if not args else args[1]
    return mock_conditions(method, url, 201)


def mock_request_204(*args, **kwargs) -> MockResponse:
    method = kwargs.get("method") if not args else args[0]
    url = kwargs.get("url") if not args else args[1]
    return mock_conditions(method, url, 204)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_409(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 409)


def mock_request_429(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 429)
