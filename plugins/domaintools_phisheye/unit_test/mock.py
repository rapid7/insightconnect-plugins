import json
import logging
import os
from typing import Callable
from unittest import mock

from icon_domaintools_phisheye.connection.connection import Connection
from icon_domaintools_phisheye.connection.schema import Input
from insightconnect_plugin_runtime.action import Action
import requests

STUB_CONNECTION = {Input.API_KEY: {"secretKey": "11111-aaaaa-aaa11-111aa-aaa11"}, Input.USERNAME: "user1"}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))


class MockResponse:
    def __init__(self, filename: str, status_code: int):
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())
        self.content = json.dumps(self.json())

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mock_conditions(status: str) -> MockResponse:
    if status == "success":
        return MockResponse("domain_list", 200)
    if status == "bad_request":
        return MockResponse("", 400)
    if status == "service_unavailable":
        return MockResponse("", 503)
    if status == "not_authorised":
        return MockResponse("", 403)
    if status == "not_found":
        return MockResponse("", 404)
    if status == "internal_service_error":
        return MockResponse("", 500)

    raise Exception("Unrecognized endpoint")


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions("success")
