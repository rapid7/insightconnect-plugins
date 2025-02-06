import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
import requests
from insightconnect_plugin_runtime.action import Action
from icon_joe_sandbox.connection.connection import Connection
from icon_joe_sandbox.connection.schema import Input

STUB_CONNECTION = {Input.URL: "https://example.com", Input.API_KEY: {"secretKey": "abcdef"}}


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
        self.ok = True

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(url: str, status_code: int) -> MockResponse:
    if url == "https://example.com/v2/server/online":
        return MockResponse("check_server_status", status_code)
    if url == "https://example.com/v2/analysis/delete":
        return MockResponse("delete_analysis", status_code)
    if url == "https://example.com/v2/analysis/download":
        return MockResponse("download_analysis", status_code)
    if url == "https://example.com/v2/account/info":
        return MockResponse("get_account_info", status_code)
    if url == "https://example.com/v2/analysis/info":
        return MockResponse("get_analysis_info", status_code)
    if url == "https://example.com/v2/server/info":
        return MockResponse("get_server_info", status_code)
    if url == "https://example.com/v2/submission/info":
        return MockResponse("get_submitted_info", status_code)
    if url == "https://example.com/v2/submission/new":
        return MockResponse("submit_sample", status_code)
    if url == "https://example.com/v2/submission/chunked-sample":
        return MockResponse("chunked_sample", status_code)
    if url == "https://example.com/v2/submission/info":
        return MockResponse("get_submitted_info", status_code)
    if url == "https://example.com/v2/analysis/list":
        return MockResponse("list_analysis", status_code)
    if url == "https://example.com/v2/server/lia_countries":
        return MockResponse("list_countries", status_code)
    if url == "https://example.com/v2/server/systems":
        return MockResponse("list_systems", status_code)
    if url == "https://example.com/v2/analysis/search":
        return MockResponse("search_analysis", status_code)

    raise Exception("Unrecognised Endpoint")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)
