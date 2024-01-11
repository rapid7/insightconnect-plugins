import os
import sys

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from util import (
    Util,
    mock_request_200_find_device,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
    ORG_ID,
)
from icon_automox.actions.get_device_by_hostname import GetDeviceByHostname
from icon_automox.actions.get_device_by_hostname.schema import Input, Output


class TestGetDeviceByIp(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetDeviceByHostname())
        self.params = {Input.ORG_ID: ORG_ID, Input.HOSTNAME: "apple"}

    @patch("requests.Session.request", side_effect=mock_request_200_find_device)
    def test_get_device_by_hostname_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.DEVICE: {
                "id": 1234,
                "agent_version": "1.42.13",
                "compliant": True,
                "create_time": "2023-04-13T19:45:45+0000",
                "detail": {
                    "RAM": "8589934592",
                    "CPU": "Intel(R) Core(TM) i7-8700B CPU @ 3.20GHz",
                    "MDM_SERVER": "none",
                    "VERSION": "MacBookPro16,1",
                    "NICS": [
                        {
                            "CONNECTED": True,
                            "VENDOR": "Apple",
                            "DEVICE": "en0",
                            "TYPE": "enet",
                            "MAC": "00:00:00:00:00:00",
                            "IPS": ["192.168.1.1"],
                        }
                    ],
                    "VOLUME": [
                        {
                            "FSTYPE": "APFS",
                            "LABEL": "macOS",
                            "AVAIL": "62704803840",
                            "FREE": "21316517888",
                            "IS_SYSTEM_DISK": "true",
                            "VOLUME": "/dev/disk1s5s1",
                        },
                        {
                            "VOLUME": "/dev/disk1s3",
                            "FSTYPE": "APFS",
                            "LABEL": "Recovery",
                            "AVAIL": "62704803840",
                            "FREE": "21316517888",
                            "IS_SYSTEM_DISK": "false",
                        },
                    ],
                    "VENDOR": "Apple",
                    "MDM_PROFILE_INSTALLED": "false",
                    "LAST_USER_LOGON": {"SRC": "console", "USER": "root", "TIME": "2023-04-14 16:05"},
                    "UPDATE_SOURCE_CHECK": {"CONNECTED": "true", "ERROR": "Succeded"},
                    "SERIAL": "C00000000001",
                    "DISKS": [{"TYPE": "VMware Virtual NVMe Disk", "SIZE": "62914560000"}],
                    "IPS": ["192.168.1.1"],
                    "MODEL": "MacBook Pro",
                    "AUTO_UPDATE_OPTIONS": {
                        "OPTIONS": "Automatic Check for Updates, Install system data updates, Install system security updates",
                        "ENABLED": "0",
                    },
                },
                "display_name": "apple",
                "ip_addrs": ["0.0.0.0"],
                "ip_addrs_private": ["192.168.1.1"],
                "is_compatible": True,
                "last_disconnect_time": "2023-04-14T23:07:04+0000",
                "last_logged_in_user": "root",
                "last_process_time": "2023-04-14T22:40:56+0000",
                "last_refresh_time": "2023-04-14T23:06:27+0000",
                "last_update_time": "2023-04-14T22:51:10+0000",
                "name": "apple",
                "needs_attention": True,
                "organization_id": 1234,
                "os_family": "Mac",
                "os_name": "OS X",
                "os_version": "12.6.6",
                "os_version_id": 1234,
                "refresh_interval": 1440,
                "serial_number": "C00000000001",
                "server_group_id": 1234,
                "status": {"device_status": "not-ready", "agent_status": "disconnected", "policy_status": "unmanaged"},
                "timezone": "UTC-0700",
                "total_count": 5,
                "uptime": "88632",
                "uuid": "00000000-0000-0000-0000-000000000000",
            },
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_200_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
        ],
    )
    def test_get_device_by_hostname_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
