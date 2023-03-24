import json
import os
from typing import Callable
from unittest import mock
from icon_zoom.actions.create_user.schema import Input
import requests

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
    if url == STUB_BASE_URL:
        if method == "GET":
            return MockResponse("get_user", status_code)
        if method == "POST":
            return MockResponse("create_user", status_code)
        if method == "DELETE":
            return MockResponse("delete_user", status_code)


def mock_request_201(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201)


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_409(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 409)


def mock_request_429(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 429)
