import json
import os
from unittest import TestCase, mock

from cbapi.errors import ServerError, ObjectNotFoundError
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_carbon_black_response.actions.uninstall_sensor import UninstallSensor
import logging

post_uninstall = {
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
    "computer_sid": "S-1-5-21-3466203702-4096304019-2269081035",
    "next_checkin_time": "2022-02-08 14:02:17.330174-08:00",
    "node_id": 0,
    "cookie": 342432840,
    "emet_exploit_action": " (Locally configured)",
    "computer_name": "MSEDGEWIN10",
    "license_expiration": "1990-01-01 00:00:00-08:00",
    "supports_isolation": True,
    "parity_host_id": "0",
    "supports_2nd_gen_modloads": False,
    "network_adapters": "10.0.2.15,080147347cfb|",
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
    "uninstall": True,
}


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = "This is some error text"


def read_file_to_string(filename, put_request_sent):
    with open(filename) as my_file:
        data = my_file.read()
    if put_request_sent is True:
        return json.loads(data)["post_uninstall"]
    else:
        return json.loads(data)["pre_uninstall"]


class MockCbEnterpriseResponseAPI:
    def get_object(self, uri, query_parameters=None, default=None):
        actual_path = os.path.dirname(os.path.realpath(__file__))
        actual_joined_path = os.path.join(actual_path, "payloads/uninstall_sensors_get.json")
        get_messages_from_user_payload = read_file_to_string(actual_joined_path, False)
        if uri == "/api/v1/sensor/1":
            return MockResponse(get_messages_from_user_payload, 200)
        elif uri == "/api/v1/sensor/150":
            raise ObjectNotFoundError(uri)
        elif uri == "/api/v1/sensor/bad":
            raise ServerError(400, "Bad Request")

    def put_object(self, uri, body, **kwargs):
        actual_path = os.path.dirname(os.path.realpath(__file__))
        actual_joined_path = os.path.join(actual_path, "payloads/uninstall_sensors_get.json")
        get_messages_from_user_payload = read_file_to_string(actual_joined_path, True)
        if uri == "/api/v1/sensor/1" and body == get_messages_from_user_payload:
            return MockResponse(get_messages_from_user_payload, 204)
        elif uri == "/api/v1/sensor/150":
            raise ServerError(404, "Invalid Sensor")
        elif uri == "/api/v1/sensor/bad":
            raise ServerError(400, "Bad Request")


class MockConnection:
    def __init__(self):
        self.carbon_black = MockCbEnterpriseResponseAPI()
        self.connection_test_passed = False


class TestUninstallSensors(TestCase):
    @mock.patch("cbapi.CbEnterpriseResponseAPI", side_effect=MockCbEnterpriseResponseAPI)
    def test_uninstall_sensor_success(self, mockCbEnterpriseResponseAPI):
        log = logging.getLogger("Test")
        test_action = UninstallSensor()
        test_action.connection = MockConnection()
        test_action.logger = log

        working_params = {"id": "1"}
        results = test_action.run(working_params)

        expected = {"success": True}
        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)

    @mock.patch("cbapi.CbEnterpriseResponseAPI", side_effect=MockCbEnterpriseResponseAPI)
    def test_uninstall_sensor_failure(self, mockCbEnterpriseResponseAPI):
        log = logging.getLogger("Test")
        test_action = UninstallSensor()
        test_action.connection = MockConnection()
        test_action.logger = log

        working_params = {"id": "bad"}

        self.assertRaises(PluginException, test_action.run, working_params)

    @mock.patch("cbapi.CbEnterpriseResponseAPI", side_effect=MockCbEnterpriseResponseAPI)
    def test_uninstall_sensor_invalid_id(self, mockCbEnterpriseResponseAPI):
        log = logging.getLogger("Test")
        test_action = UninstallSensor()
        test_action.connection = MockConnection()
        test_action.logger = log

        working_params = {"id": "150"}

        self.assertRaises(PluginException, test_action.run, working_params)
