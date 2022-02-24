import json
import os
from unittest import mock
from typing import Callable
from icon_carbon_black_response.connection.schema import Input

import requests

BASE_URL = f"https://cb-response-dev.vuln.lax.rapid7.com"
SENSOR_URI = f"/api/v1/sensor/"
STUB_SENSOR_ID = "12"

STUB_API_KEY = "6de82826ec6f6fc760a15a933db4fff3958d7422"
STUB_CONNECTION = {
    Input.API_KEY: {"secretKey": STUB_API_KEY},
    Input.SSL_VERIFY: False,
    Input.URL: BASE_URL
}

STUB_SENSOR_RESPONSE = {
    "systemvolume_total_size": "42947571712",
    "emet_telemetry_path": "",
    "os_environment_display_string": "Windows 10 Server Enterprise (Evaluation), 64-bit",
    "emet_version": "",
    "emet_dump_flags": "",
    "clock_delta": "0",
    "supports_cblr": True,
    "sensor_uptime": "10567",
    "last_update": "2022-02-08 14:01:57.859204-08:00",
    "physical_memory_size": "2147012608",
    "build_id": 2,
    "uptime": "11680",
    "is_isolating": False,
    "event_log_flush_time": None,
    "computer_dns_name": "MSEDGEWIN10",
    "emet_report_setting": " (GPO configured)",
    "id": 12,
    "emet_process_count": 0,
    "emet_is_gpo": False,
    "power_state": 0,
    "network_isolation_enabled": False,
    "uninstalled": None,
    "systemvolume_free_size": "19801292800",
    "status": "Offline",
    "num_eventlog_bytes": "0",
    "sensor_health_message": "Elevated HANDLE count",
    "build_version_string": "006.001.002.71109",
    "computer_sid": "S-1-5-21-3461203602-4096304019-2269080069",
    "next_checkin_time": "2022-02-08 14:02:17.330174-08:00",
    "node_id": 0,
    "cookie": 342432837,
    "emet_exploit_action": " (Locally configured)",
    "computer_name": "MSEDGEWIN10",
    "license_expiration": "1990-01-01 00:00:00-08:00",
    "supports_isolation": True,
    "parity_host_id": "0",
    "supports_2nd_gen_modloads": False,
    "network_adapters": "10.0.2.15,080027347cfb|",
    "sensor_health_status": 95,
    "registration_time": "2022-02-08 11:05:41.849645-08:00",
    "restart_queued": False,
    "notes": None,
    "num_storefiles_bytes": "0",
    "os_environment_id": 3,
    "shard_id": 0,
    "boot_id": "0",
    "last_checkin_time": "2022-02-08 14:01:48.333571-08:00",
    "os_type": 1,
    "group_id": 1,
    "display": True,
    "uninstall": False
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


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
        if method == "GET":
            return MockResponse("dlGetAll", status_code)
        if method == "POST":
            return MockResponse("dlCreate", status_code)
    if url == BASE_URL + SENSOR_URI + STUB_SENSOR_ID:
        if method == "GET":
            return MockResponse("dlGet", status_code)
        if method == "PUT":
            return MockResponse("dlPatch", status_code)
# Add other test cases for other actions


def mock_conditions_connection(url: str, status_code: int) -> MockResponse:
    if url == BASE_URL:
        if status_code == 200 or status_code == 204:
            return MockResponse("test_connection_ok", status_code)
        elif status_code >= 400:
            return MockResponse("test_connection_bad", status_code)

    raise Exception("Response has not been implemented")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_204(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 204)


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


def mock_request_200_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 200)


def mock_request_403_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 403)


def mock_request_500_connection(*args, **kwargs) -> MockResponse:
    return mock_conditions_connection(args[1], 500)
