import json
import os
from typing import Callable
from unittest import mock

import requests
from icon_jamf.connection.schema import Input

STUB_CONNECTION = {
    Input.CLIENT_LOGIN: {"username": "ExmapleUser", "password": "ExamplePassword"},
    Input.TIMEOUT: 30,
    Input.URL: "http://example.com",
}
STUB_DEVICE_ID = 1
STUB_DEVICE_IDS = ["1", "2"]
STUB_DEVICE_PASSCODE = "123456"
STUB_DEVICE_NAME = "Example Name"


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
    if status_code == 405:
        return MockResponse("wrong_json", status_code)
    if url == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/users":
        return MockResponse("", status_code)
    elif url == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/mobiledevices/id/{STUB_DEVICE_ID}":
        return MockResponse("get_user_location", status_code)
    elif url == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/computergroups/id/{STUB_DEVICE_ID}":
        return MockResponse("add_computer_to_group", status_code)
    elif (
        url
        == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/computercommands/command/EraseDevice/passcode/{STUB_DEVICE_PASSCODE}/id/{STUB_DEVICE_ID}"
    ):
        return MockResponse("add_computer_to_group", status_code)
    elif url == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/users/name/{STUB_DEVICE_NAME}":
        return MockResponse("get_devices_name_id", status_code)
    elif url == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/mobiledevicegroups/id/{STUB_DEVICE_ID}":
        return MockResponse("get_group_detail", status_code)
    elif (
        url
        == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/computercommands/command/DeviceLock/passcode/{STUB_DEVICE_PASSCODE}/id/{STUB_DEVICE_ID}"
    ):
        return MockResponse("add_computer_to_group", status_code)
    elif (
        url
        == f"{STUB_CONNECTION.get(Input.URL)}/JSSResource/mobiledevicecommands/command/DeviceLock/id/{','.join(STUB_DEVICE_IDS)}"
    ):
        return MockResponse("add_computer_to_group", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 200)


def mock_request_201(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 201)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 400)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 403)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 404)


def mock_request_405(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 405)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 500)


def mock_request_505(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[1], 505)
