import json
import os
from typing import Callable
from unittest import mock

import requests

STUB_ORG_ID = "1234567"
STUB_DESTINATION_LIST_ID = "12345678"


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
    base_url = f"https://management.api.umbrella.com/v1/organizations/{STUB_ORG_ID}/destinationlists"
    if url == base_url:
        if method == 'GET':
            return MockResponse("dlGetAll", status_code)
        if method == 'POST':
            return MockResponse('dlCreate', status_code)
    if url == base_url + f'{STUB_DESTINATION_LIST_ID}':
        if method == 'GET':
            return MockResponse('dlGet', status_code)
        if method == 'PATCH':
            return MockResponse('dlPatch', status_code)
        if method == 'DELETE':
            return MockResponse('dlDelete', status_code)
    if url == base_url + f'{STUB_DESTINATION_LIST_ID}/destinations':
        if method == 'GET':
            return MockResponse('dGet', status_code)
        if method == 'POST':
            return MockResponse('dAdd', status_code)
    if url == base_url + f'{STUB_DESTINATION_LIST_ID}/destinations/remove':
        return MockResponse('dDelete', status_code)


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
