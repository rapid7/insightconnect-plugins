from icon_palo_alto_cortex_xdr.connection.connection import Connection
from icon_palo_alto_cortex_xdr.connection.schema import Input

from insightconnect_plugin_runtime.task import Task

from typing import Callable, Any, Dict
from unittest import mock

import json
import logging
import os
import sys
import requests

sys.path.append(os.path.abspath("../"))

STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
    Input.API_KEY_ID: 15,
    Input.SECURITY_LEVEL: "Advanced",
    Input.URL: "https://example.com/",
}


class TaskUtil:
    @staticmethod
    def default_connector(task: Task) -> Any:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        task.connection = default_connection
        task.logger = logging.getLogger("task logger")
        return task

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()

    @staticmethod
    def load_expected(filename: str = None) -> Dict[str, Any]:
        if not filename:
            return []
        return json.loads(
            TaskUtil.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    f"expected/{filename}.json.exp",
                )
            )
        )


class MockResponse:
    def __init__(self, status_code: int, filename: str, text: str = "Example Text", url: str = None) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        self.headers = {"Header": "Value"}
        self.url = url

    def json(self):
        if self.filename == "empty_response":
            return {}
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def raise_for_status(self) -> None:
        if self.status_code != 200:
            raise requests.HTTPError(f"{self.status_code}: Client Error", response=self)


def mock_conditions(status_code: int, file_name: str = "", **kwargs: Dict[str, Any]) -> MockResponse:
    if file_name:
        return MockResponse(status_code, file_name)
    raise Exception("Response has been not implemented")


def mocked_response_type(status_code: int, text: str = None) -> requests.Response:
    """
    Function to mock a Response containing a status code and content.
    :param status_code: Status code of the mocked Response
    :param text: Text of the mocked Response
    :return: Response
    """
    response = requests.Response()
    response.status_code = status_code
    if text:
        response._content = text.encode("utf-8")
    return response
