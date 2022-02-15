import json
import os
from typing import Callable
from unittest import mock
from icon_cisco_umbrella_destinations.connection.schema import Input

import requests

STUB_ORG_ID = "1234567"
STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_DESTINATION_LIST_ID = "12345678"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.API_SECRET: {"secretKey": STUB_API_KEY},
    Input.ORGANIZATION_ID: STUB_ORG_ID,
}
STUB_RESPONSE = {
    "success": {
        "status": {"code": 200, "text": "OK"},
        "data": {
            "id": 15755711,
            "organizationId": 2372338,
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
BASE_URL = f"https://management.api.umbrella.com/v1/organizations/{STUB_ORG_ID}/destinationlists"


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
    if url == BASE_URL:
        if method == "GET":
            return MockResponse("dlGetAll", status_code)
        if method == "POST":
            return MockResponse("dlCreate", status_code)
    if url == BASE_URL + f"/{STUB_DESTINATION_LIST_ID}":
        if method == "GET":
            return MockResponse("dlGet", status_code)
        if method == "PATCH":
            return MockResponse("dlPatch", status_code)
        if method == "DELETE":
            return MockResponse("dlDelete", status_code)
    if url == BASE_URL + f"/{STUB_DESTINATION_LIST_ID}/destinations":
        if method == "GET":
            return MockResponse("dGet", status_code)
        if method == "POST":
            return MockResponse("dAdd", status_code)
    if url == BASE_URL + f"/{STUB_DESTINATION_LIST_ID}/destinations/remove":
        return MockResponse("dDelete", status_code)


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
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
