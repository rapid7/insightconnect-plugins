import sys
import os
from unittest import TestCase
from komand_palo_alto_pan_os.actions.check_if_address_object_in_group import CheckIfAddressObjectInGroup
from komand_palo_alto_pan_os.actions.check_if_address_object_in_group.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestCheckIfAddressObjectInGroup(TestCase):
    @parameterized.expand(
        [
            [
                "success",
                "test.com",
                "Test Group",
                False,
                "localhost.localdomain",
                "vsys1",
                {"found": True, "address_objects": ["test.com"]},
            ],
            [
                "not_found",
                "example.com",
                "Test Group",
                False,
                "localhost.localdomain",
                "vsys1",
                {"found": False, "address_objects": []},
            ],
            [
                "enable_search_domain",
                "test.com",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": True, "address_objects": ["test.com"]},
            ],
            [
                "enable_search_ipv4",
                "1.1.1.1",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": True, "address_objects": ["1.1.1.1"]},
            ],
            [
                "enable_search_ipv6",
                "abcd:123::1",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": True, "address_objects": ["IPv6"]},
            ],
            [
                "enable_search_domain_not_found",
                "example.com",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": False, "address_objects": []},
            ],
            [
                "enable_search_ipv4_not_found",
                "2.2.2.2",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": False, "address_objects": []},
            ],
            [
                "enable_search_ipv6_not_found",
                "abcd:321::1",
                "Test Group",
                True,
                "localhost.localdomain",
                "vsys1",
                {"found": False, "address_objects": []},
            ],
        ]
    )
    def test_check_if_address_object_in_group(
        self, mock_get, name, address, group, enable_search, device_name, virtual_system, expected
    ):
        action = Util.default_connector(CheckIfAddressObjectInGroup())
        actual = action.run(
            {
                Input.ADDRESS: address,
                Input.GROUP: group,
                Input.ENABLE_SEARCH: enable_search,
                Input.DEVICE_NAME: device_name,
                Input.VIRTUAL_SYSTEM: virtual_system,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_group",
                ["example.com"],
                "Invalid Group",
                False,
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find group 'Invalid Group', or group was empty. Check the name, virtual system name, and device name.\ndevice name: localhost.localdomain\nvirtual system: vsys1",
            ]
        ]
    )
    def test_check_if_address_object_in_group_bad(
        self, mock_get, name, address, group, enable_search, device_name, virtual_system, cause, assistance
    ):
        action = Util.default_connector(CheckIfAddressObjectInGroup())
        with self.assertRaises(PluginException) as e:
            action.run(
                {
                    Input.ADDRESS: address,
                    Input.GROUP: group,
                    Input.ENABLE_SEARCH: enable_search,
                    Input.DEVICE_NAME: device_name,
                    Input.VIRTUAL_SYSTEM: virtual_system,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
