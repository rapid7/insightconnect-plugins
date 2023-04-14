import os
import sys

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from unit_test.util import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
    ORG_ID,
)
from icon_automox.actions.get_device_by_ip import GetDeviceByIp
from icon_automox.actions.get_device_by_ip.schema import Input, Output


class TestGetDeviceByIp(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetDeviceByIp())
        self.params = {Input.ORG_ID: ORG_ID, Input.IP_ADDRESS: "192.168.0.1"}

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_get_device_by_ip_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.DEVICE: {
                "id": 123,
                "agent_version": "1.0-0",
                "compliant": True,
                "create_time": "2023-03-1T12:00:00+0000",
                "custom_name": "CustomName",
                "display_name": "WinName",
                "ip_addrs": ["127.0.0.1"],
                "ip_addrs_private": ["192.168.0.1", "fe11::f1d1:af1a:c1a1:11b1"],
                "is_compatible": True,
                "last_disconnect_time": "2023-03-01T12:00:00+0000",
                "last_logged_in_user": "WIN\\Example",
                "last_refresh_time": "2023-03-01T12:00:00+0000",
                "last_update_time": "2023-03-01T12:00:00+0000",
                "name": "WinHostName",
                "needs_attention": True,
                "needs_reboot": True,
                "organization_id": 1234,
                "os_family": "Windows",
                "os_name": "10 Enterprise",
                "os_version": "10.0.0",
                "os_version_id": 1234,
                "patches": 1,
                "policy_status": [
                    {
                        "id": 1234,
                        "organization_id": 1234,
                        "policy_id": 1234,
                        "server_id": 1234,
                        "policy_name": "Apply Critical Patches",
                        "policy_type_name": "patch",
                        "status": 1,
                        "result": "{}",
                        "create_time": "2023-03-01T12:00:00+0000",
                    }
                ],
                "refresh_interval": 1440,
                "serial_number": "VMware-1234",
                "server_group_id": 1234,
                "status": {
                    "device_status": "not-ready",
                    "agent_status": "disconnected",
                    "policy_status": "compliant",
                    "policy_statuses": [{"id": 1234, "compliant": True}],
                },
                "timezone": "UTC-0700",
                "total_count": 1,
                "uuid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
            },
        }

        self.assertEqual(response, expected_response)

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_get_device_by_ip_existing(self, mock: Mock) -> None:
        self.params[Input.IP_ADDRESS] = "Non.Existing.IP.Address"
        response = self.action.run(self.params)
        expected_response = {Output.DEVICE: {}}

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_200_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
        ],
    )
    def test_get_device_by_ip_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
