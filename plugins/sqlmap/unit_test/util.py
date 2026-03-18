import json
import logging
import os
import re
from typing import Any, Dict, Tuple
from unittest.mock import Mock

from icon_sqlmap.connection.connection import Connection
from insightconnect_plugin_runtime.action import Action
from requests.exceptions import HTTPError

STUB_CONNECTION: Dict[str, str] = {"api_host": "127.0.0.1", "api_port": "8775"}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(STUB_CONNECTION)
        action.connection = connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def default_connector_connection() -> Connection:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(STUB_CONNECTION)
        return connection

    @staticmethod
    def load_parameters(filename: str) -> Dict[str, Any]:
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"parameters/{filename}",
        )
        with open(path) as file:
            return json.load(file)


class MockResponse:
    def __init__(self, filename: str, status_code: int = 200) -> None:
        self.filename = filename
        self.status_code = status_code
        self._json = self._load(filename)

    @staticmethod
    def _load(filename: str) -> dict:
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f"responses/{filename}",
        )
        with open(path) as file:
            return json.load(file)

    def json(self) -> dict:
        return self._json

    def raise_for_status(self) -> None:
        if not 200 <= self.status_code < 400:
            response = Mock()
            response.status_code = self.status_code
            raise HTTPError(response=response)

    def __enter__(self) -> "MockResponse":
        return self

    def __exit__(self, *args: Any) -> None:
        pass


ROUTE_TABLE: list[Tuple[str, str]] = [
    (r"/version", "version.json.resp"),
    (r"/task/new", "task_new.json.resp"),
    (r"/option/.+/set", "option_set.json.resp"),
    (r"/scan/.+/start", "scan_start.json.resp"),
    (r"/scan/.+/status", "scan_status_terminated.json.resp"),
    (r"/scan/.+/log", "scan_log.json.resp"),
    (r"/task/.+/delete", "task_delete.json.resp"),
]


def mocked_requests_success(*args: Any, **kwargs: Any) -> MockResponse:
    url = args[1] if len(args) > 1 else kwargs.get("url", "")
    for pattern, fixture in ROUTE_TABLE:
        if re.search(pattern, url):
            return MockResponse(fixture)
    raise NotImplementedError(f"No mock for: {url}")
