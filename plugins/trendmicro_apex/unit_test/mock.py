import json
import logging
import os
from typing import Callable
from unittest import mock
from unittest.mock import MagicMock
import requests
from insightconnect_plugin_runtime.action import Action
from icon_trendmicro_apex.connection.connection import Connection

STUB_CONNECTION = {"url": "URL", "application_id": {"secretKey": "ABCDEF"}, "api_key": {"secretKey": "ABCDEF"}}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = json.dumps(self.json())
        self.request = MagicMock()
        self.headers = MagicMock()
        self.raise_for_status = MagicMock()

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.Session.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    # breakpoint()
    if url == "URL/WebApp/API/SuspiciousObjectResource/FileUDSO":
        if method == "put":
            return MockResponse("add_file_to_usdo_list", status_code)

    if url == "URL/WebApp/api/SuspiciousObjects/UserDefinedSO":
        if method == "put":
            return MockResponse("blacklist", status_code)

    if "URL/WebApp/IOCBackend/OpenIOCResource/File?param=" in url:
        if method == "delete":
            return MockResponse("delete_openioc_file", status_code)

    if "URL/WebApp/IOCBackend/OpenIOCResource/FilingCabinet?param=" in url:
        return MockResponse("openioc_files_list", status_code)

    if "URL/WebApp/API/AgentResource/ProductAgents" in url:
        if method == "post":
            return MockResponse("quarantine", status_code)
        if method == "get":
            return MockResponse("search_agents", status_code)

    if url == "URL/WebApp/IOCBackend/OpenIOCResource/File":
        return MockResponse("upload_openioc_file", status_code)

    if url == "URL/WebApp/OSCE_iES/OsceIes/ApiEntry":
        if method == "put":
            return MockResponse("download_openioc_file", status_code)
        if method == "put":
            return MockResponse("get_agent_status", status_code)
        if method == "put":
            return MockResponse("get_rca_object", status_code)
        if method == "put":
            return MockResponse("download_rca_csv_file", status_code)

    raise Exception("Unrecognized endpoint")


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
