import os
import json
from unittest import mock
from typing import Callable, Optional
from komand_cisco_umbrella_enforcement.connection.schema import Input
import requests

STUB_VERSION_NUMBER = "1.0"
STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
STUB_SSL_VERIFY = True
BASE_URL = f"https://s-platform.api.opendns.com/{STUB_VERSION_NUMBER}"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.SSL_VERIFY: STUB_SSL_VERIFY,
}
STUB_ID = 12345678
STUB_NAME = "https://example.com"
STUB_EVENT_INPUT = {
    "dstUrl": "http://google.com",
    "alertTime": "2013-02-09T11:14:26.0Z",
    "deviceId": "12345678-1234-1234-1234-12345678912",
    "deviceVersion": "11.1a",
    "dstDomain": "http://google.com",
    "eventTime": "2013-02-09T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform",
    "disableDstSafeguards": True,
    "eventHash": "e88b372b1f98882dca933fa8a2589670",
    "fileName": "https://www.fuw.edu.pl/~rwys/pk/notatki_cl.txt",
    "fileHash": "da89127fbe1d78313dbfff610b59ff24874bb983",
    "externalURL": "https://www.fuw.edu.pl/~rwys/pk/notatki_cl.txt",
    "src": "8.8.8.8",
    "eventSeverity": "severe",
    "eventType": "severe",
    "eventDescription": "Some another threat",
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
    # breakpoint()

    if url == BASE_URL + "/domains":
        return MockResponse("domains", status_code)
    if url == BASE_URL + f"/domains/{STUB_ID}" or url == BASE_URL + f"/domains/{STUB_NAME}":
        return MockResponse("delete_domain", status_code)
    if url == BASE_URL + f"/events":
        return MockResponse("add_event", status_code)


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
        if status_code == 200:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 202)


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204)


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
