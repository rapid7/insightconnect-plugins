import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.get_addresses_from_group import GetAddressesFromGroup
from komand_palo_alto_pan_os.actions.get_addresses_from_group.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetAddressesFromGroup(TestCase):
    @parameterized.expand(
        [
            [
                "success",
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "fqdn_addresses": ["test.com"],
                    "ipv4_addresses": ["1.1.1.1"],
                    "ipv6_addresses": ["abcd:123::1"],
                    "all_addresses": ["1.1.1.1", "test.com", "abcd:123::1"],
                },
            ]
        ]
    )
    def test_get_addresses_from_group(self, mock_get, name, group, device_name, virtual_system, expected):
        action = Util.default_connector(GetAddressesFromGroup())
        actual = action.run({Input.GROUP: group, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_group",
                "Invalid Group",
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find group 'Invalid Group', or group was empty. Check the name, virtual system name, and device name.\nDevice name: localhost.localdomain\nVirtual system: vsys1\n",
            ]
        ]
    )
    def test_get_addresses_from_group_bad(self, mock_get, name, group, device_name, virtual_system, cause, assistance):
        action = Util.default_connector(GetAddressesFromGroup())
        with self.assertRaises(PluginException) as e:
            action.run({Input.GROUP: group, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
