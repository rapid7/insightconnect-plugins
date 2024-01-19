import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock

from icon_domaintools_phisheye.connection.connection import Connection
from icon_domaintools_phisheye.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {Input.API_KEY: "11111-aaaaa-aaa11-111aa-aaa11", Input.USERNAME: "user1"}


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
    def __init__(self, status_code: int, json_object: str = ""):
        self.status_code = status_code
        self.text = json.dumps(json_object)
        self.content = json.dumps(json_object)
        self.json_object = json_object

    def json(self):
        return self.json_object


