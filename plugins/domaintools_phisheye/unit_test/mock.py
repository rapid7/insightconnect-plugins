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


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
