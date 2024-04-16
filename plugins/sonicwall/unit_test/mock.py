import json
import os
from typing import Callable
from unittest import mock

import requests
from icon_sonicwall.connection.schema import Input

from utils import STUB_CONNECTION

BASE_URL = STUB_CONNECTION.get(Input.URL, "")
PORT = STUB_CONNECTION.get(Input.PORT, "")


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


def mocked_request(side_effect: Callable, method: str) -> None:
    mock_function = requests
    setattr(mock_function, method, mock.Mock(side_effect=side_effect))


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if method in ("POST", "DELETE"):
        if url in (
            f"{BASE_URL}:{PORT}/api/sonicos/auth",
            f"{BASE_URL}:{PORT}/api/sonicos/config/pending",
            f"{BASE_URL}:{PORT}/api/sonicos/address-objects/fqdn",
            f"{BASE_URL}:{PORT}/api/sonicos/address-objects/fqdn/name/ExampleAddressObject",
        ):
            return MockResponse("auth", status_code)
        elif url == f"{BASE_URL}:{PORT}/api/sonicos/direct/cli":
            return MockResponse("remove_address_from_group", status_code)
    elif method in ("GET", "PUT"):
        if url in (
            f"{BASE_URL}:{PORT}/api/sonicos/address-objects/fqdn/name/ExampleAddressObject",
            f"{BASE_URL}:{PORT}/api/sonicos/address-objects/fqdn/name/string",
        ):
            return MockResponse("address_objects", status_code)
        elif url == f"{BASE_URL}:{PORT}/api/sonicos/address-groups/ipv4/name/ExampleGroupName":
            return MockResponse("address_groups_ipv4_name", status_code)
        elif url == f"{BASE_URL}:{PORT}/api/sonicos/address-groups/ipv4/name/ExampleGroupName2":
            return MockResponse("address_groups_ipv4_name_v2", status_code)
        elif url == f"{BASE_URL}:{PORT}/api/sonicos/zones/name/WAN":
            return MockResponse("zones", status_code)
    if "InvalidJSON" in method:
        return MockResponse("invalid_json", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500)


def mock_request_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions("InvalidJSON", args[1], 200)
