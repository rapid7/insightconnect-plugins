import json
import os
from typing import Any, Callable, Dict
from unittest import mock

import requests

STUB_TENANT_NAME = "exampletenant"
STUB_API_KEY = "j5740ps1cbukyk3t8kib3wa36aq2v3da"
STUB_ID = 1
STUB_ACTION = "replace"
STUB_CONNECTION = {
    "api_key_v1": {"secretKey": STUB_API_KEY},
    "api_key_v2": {"secretKey": STUB_API_KEY},
    "tenant": STUB_TENANT_NAME,
}


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


def mock_conditions_actions_api_v1(url: str, status_code: int, params: Dict[str, Any] = None) -> MockResponse:
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v1/updateFileHashList":
        if status_code == 409:
            return MockResponse("test_create_new_url_list_bad_json_response", 200)
        if not all((params.get("name", False), params.get("list", False))):
            return MockResponse("test_update_file_hash_list_bad", status_code)
        return MockResponse("test_update_file_hash_list_ok", status_code)
    raise Exception("Response has been not implemented")


def mock_conditions_actions_api_v2(
    method: str, url: str, status_code: int, params: Dict[str, Any] = None
) -> MockResponse:
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist":
        if method == "GET":
            if params and params.get("pending") == 1:
                return MockResponse("test_get_all_url_list_ok_pending", status_code)
            return MockResponse("test_get_all_url_list_ok", status_code)
        if method == "POST":
            if status_code == 409:
                return MockResponse("test_create_new_url_list_bad_json_response", 200)
            return MockResponse("test_create_new_url_list_ok", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist/file":
        if method == "POST":
            return MockResponse("test_upload_json_config_ok", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist/{STUB_ID}":
        if method in ("GET", "PUT", "DELETE"):
            return MockResponse("test_get_url_list_by_id_ok", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist/{STUB_ID}/{STUB_ACTION}":
        if method == "PATCH":
            return MockResponse("test_get_url_list_by_id_ok", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist/deploy":
        if method == "POST":
            return MockResponse("test_apply_pending_url_list_changes_ok", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/ubadatasvc/user/uci":
        if method == "POST":
            return MockResponse("test_get_single_user_confidence_index_ok", status_code)
    raise Exception("Response has been not implemented")


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v1/updateFileHashList/":
        if status_code in (200, 201):
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)
    if url == f"https://{STUB_TENANT_NAME}.goskope.com/api/v2/policy/urllist":
        return MockResponse("test_get_all_url_list_ok_pending", status_code)
    raise Exception("Response has been not implemented")


def mock_request_200_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 200, kwargs.get("params"))


def mock_request_201_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 201, kwargs.get("params"))


def mock_request_400_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 400, kwargs.get("params"))


def mock_request_403_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 403, kwargs.get("params"))


def mock_request_404_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 404, kwargs.get("params"))


def mock_request_429_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 429, kwargs.get("params"))


def mock_request_bad_json_response_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 409)


def mock_request_500_api_v1(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v1(args[1], 500, kwargs.get("params"))


def mock_request_200_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 200, kwargs.get("params"))


def mock_request_201_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 201)


def mock_request_400_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 400)


def mock_request_401_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 401)


def mock_request_403_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 403)


def mock_request_404_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 404)


def mock_request_429_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 429)


def mock_request_bad_json_response_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 409)


def mock_request_500_api_v2(*args, **kwargs) -> MockResponse:
    return mock_conditions_actions_api_v2(args[0], args[1], 500)


def mock_request_200_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 200)


def mock_request_401_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 401)


def mock_request_403_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 403)


def mock_request_429_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 429)


def mock_request_500_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 500)


def mock_request_503_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 503)


def mock_request_512_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 512)
