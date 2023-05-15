import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
from komand_thehive.connection.connection import Connection
from komand_thehive.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

import requests

STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_USERNAME = "username"
STUB_PASSWORD = "password"
STUB_CONNECTION_API_KEY = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
}
STUB_CONNECTION_USERNAME_PASSWORD = {
    Input.CREDENTIALS.get("username"): STUB_USERNAME,
    Input.CREDENTIALS.get("password"): STUB_PASSWORD
}
STUB_BASE_URL = "http://10.10.10.10/9000"
STUB_CASE_ID = "abcdef123"
STUB_USER_ID = "stubuserid"

# KEEP THIS FOR REFERENCE - DELETE WHEN DONE
STUB_RESPONSE = {
    "success": {
        "status": {"code": 200, "text": "OK"},
        "data": {
            "id": 15755711,
            "access": "allow",
            "isGlobal": False,
            "name": "CreateListTest",
            "thirdpartyCategoryId": None,
            "createdAt": "2022-01-28T16:03:36+0000",
            "modifiedAt": "2022-02-09T11:47:00+0000",
            "isMspDefault": False,
            "markedForDeletion": False,
            "bundleTypeId": 1,
            "meta": {"destinationCount": 5},
        },
    }
}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION_API_KEY)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:

    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}":
        if method == "GET":
            return MockResponse("get_case", status_code)
        if method == "DELETE":
            return MockResponse("close_case", status_code)
    if url == STUB_BASE_URL + f"/api/case/_search":
        return MockResponse("get_cases", status_code)
    if url == STUB_BASE_URL + f"/api/case":
        return MockResponse("create_case", status_code)
    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}/artifact":
        return MockResponse("create_case_observable", status_code)
    if url == STUB_BASE_URL + f"/api/case/{STUB_CASE_ID}/task":
        return MockResponse("create_case_task", status_code)
    if url == STUB_BASE_URL + "/api/user/current":
        return MockResponse("get_current_user", status_code)
    if url == STUB_BASE_URL + f"/api/user/{STUB_USER_ID}":
        return MockResponse("get_user_by_id", status_code)
    raise Exception("Unrecognized endpoint")


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == STUB_BASE_URL:
        if status_code == 200:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500)


def mock_request_200_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 200)


def mock_request_403_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 403)


def mock_request_500_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 500)