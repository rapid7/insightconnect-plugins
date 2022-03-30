import json
import os
from typing import Callable
from unittest import mock

import requests

from icon_microsoft_log_analytics.util.endpoints import Endpoint

STUB_SHARED_KEY = "123456=="
STUB_WORKSPACE_ID = "12345"

STUB_RESOURCE_GROUP_NAME = "exampleresourcegroupname"
STUB_WORKSPACE_NAME = "ExampleWorkspace"
STUB_SUBSCRIPTION_ID = "1234"

STUB_CONNECTION = {"client_id": "1234", "client_secret": {"secretKey": "1234"}, "tenant_id": "123"}


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
    if status_code == 201:
        return MockResponse("test_invalid_json_response", status_code)
    if "oauth2/token" in url:
        return MockResponse("test_get_auth_token", status_code)
    if url == Endpoint.GET_SHARED_KEY.format(
        STUB_SUBSCRIPTION_ID,
        STUB_RESOURCE_GROUP_NAME,
        STUB_WORKSPACE_NAME,
        "2020-08-01",
    ):
        return MockResponse("test_get_shared_key", status_code)
    if url == Endpoint.GET_WORKSPACE_ID.format(
        STUB_SUBSCRIPTION_ID,
        STUB_RESOURCE_GROUP_NAME,
        STUB_WORKSPACE_NAME,
        "2021-12-01-preview",
    ):
        return MockResponse("test_get_workspace_id", status_code)
    if url == Endpoint.GET_LOG_DATA.format("v1", STUB_WORKSPACE_ID):
        return MockResponse("test_get_log_data_ok", status_code)
    if url == Endpoint.SEND_LOG_DATA.format(STUB_WORKSPACE_ID, "2016-04-01"):
        return MockResponse("test_send_log_data_ok", status_code)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 201)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 400)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 404)


def mock_request_409(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 409)


def mock_request_429(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 429)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)


def mock_request_503(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 503)
