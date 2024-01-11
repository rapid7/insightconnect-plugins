import json
import logging
import os
import sys
from typing import Callable, Union

import requests

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import mock

from insightconnect_plugin_runtime.action import Action
from icon_automox.connection.connection import Connection
from icon_automox.connection.schema import Input

STUB_CONNECTION = {Input.API_KEY: {"secretKey": "11111111-1111-1111-1111-111111111111"}}

BASE_URL = "https://console.automox.com"
ORG_ID = 1234
BATCH_ID = 12345
TASK_ID = 123
DEVICE_ID = 1234
POLICY_ID = 1234
GROUP_ID = 1111
ACTION_SET_ID = 1234
ACTION = "accept"


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
    def __init__(self, filename: Union[str, None], status_code: int, text: str = "Example Text") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self):
        # Allow for empty responses
        if self.filename is None:
            return None
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests.Session
    mock_function.request = mock.Mock(side_effect=side_effect)


def mocked_post(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.post = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int, **kwargs: Dict[str, Any]) -> MockResponse:
    if kwargs.get("invalid_json"):
        return MockResponse("test_invalid_json_response", status_code)
    if method == "GET":
        if url == f"{BASE_URL}/api/servers" and kwargs.get("get_device_by_hostname_or_ip"):
            return MockResponse("test_get_device_by_hostname_or_ip", status_code)
        elif url == f"{BASE_URL}/api/servers":
            return MockResponse("test_list_devices", status_code)
        # This is not exposed in the plugin, but is used internally
        elif url == f"{BASE_URL}/api/servers/{DEVICE_ID}":
            return MockResponse("test_get_device_by_id", status_code)
        elif url == f"{BASE_URL}/api/servers/{DEVICE_ID}/packages":
            return MockResponse("test_get_device_software", status_code)
        elif url == f"{BASE_URL}/api/users":
            return MockResponse("test_list_organization_users", status_code)
        elif url == f"{BASE_URL}/api/orgs":
            return MockResponse("test_list_organizations", status_code)
        elif url == f"{BASE_URL}/api/servergroups":
            return MockResponse("test_list_groups", status_code)
        # This is not exposed in the plugin, but is used internally
        elif url == f"{BASE_URL}/api/servergroups/{GROUP_ID}":
            return MockResponse("test_get_group_by_id", status_code)
        elif url == f"{BASE_URL}/api/policies":
            return MockResponse("test_list_policies", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets":
            return MockResponse("test_list_vulnerability_sync_action_sets", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/{ACTION_SET_ID}":
            return MockResponse("test_get_vulnerability_sync_action_set", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/{ACTION_SET_ID}/solutions":
            return MockResponse("test_list_vulnerability_sync_action_set_solutions", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/{ACTION_SET_ID}/issues":
            return MockResponse("test_list_vulnerability_sync_action_set_issues", status_code)

    elif method in ["POST", "PATCH"]:
        if url == f"{BASE_URL}/api/servergroups":
            return MockResponse("test_create_group", status_code)
        elif url == f"{BASE_URL}/api/servers/{DEVICE_ID}":
            return MockResponse("test_update_device", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/{ACTION_SET_ID}/actions":
            return MockResponse("test_request_success", status_code)
        elif url == f"{BASE_URL}/api/servers/{DEVICE_ID}/queues":
            return MockResponse("test_request_success", status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/upload":
            return MockResponse("test_upload_vulnerability_sync_file", status_code)
    elif method == "PUT":
        if url == f"{BASE_URL}/api/servers/{DEVICE_ID}":
            return MockResponse(None, status_code)
        elif url == f"{BASE_URL}/api/servergroups/{GROUP_ID}":
            return MockResponse(None, status_code)
    elif method == "DELETE":
        if url == f"{BASE_URL}/api/servers/{DEVICE_ID}":
            return MockResponse(None, status_code)
        elif url == f"{BASE_URL}/api/servergroups/{GROUP_ID}":
            return MockResponse(None, status_code)
        elif url == f"{BASE_URL}/api/orgs/{ORG_ID}/remediations/action-sets/{ACTION_SET_ID}":
            return MockResponse(None, status_code)

    raise Exception("Response has been not implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200, **kwargs)


def mock_request_201(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201, **kwargs)


def mock_request_post_201(*args, **kwargs) -> MockResponse:
    return mock_conditions("POST", args[0], 201, **kwargs)


def mock_request_202(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 202, **kwargs)


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204, **kwargs)


def mock_request_200_find_device(*args, **kwargs) -> MockResponse:
    kwargs["get_device_by_hostname_or_ip"] = True
    return mock_conditions(args[0], args[1], 200, **kwargs)


def mock_request_200_invalid_json(*args, **kwargs) -> MockResponse:
    kwargs["invalid_json"] = True
    return mock_conditions(args[0], args[1], 200, **kwargs)


def mock_request_post_201_invalid_json(*args, **kwargs) -> MockResponse:
    kwargs["invalid_json"] = True
    return mock_conditions("POST", args[0], 201, **kwargs)


def mock_request_403(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 403, **kwargs)


def mock_request_post_403(*args, **kwargs) -> MockResponse:
    return mock_conditions("POST", args[0], 403, **kwargs)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404, **kwargs)


def mock_request_post_404(*args, **kwargs) -> MockResponse:
    return mock_conditions("POST", args[0], 404, **kwargs)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500, **kwargs)


def mock_request_post_500(*args, **kwargs) -> MockResponse:
    return mock_conditions("POST", args[0], 500, **kwargs)
