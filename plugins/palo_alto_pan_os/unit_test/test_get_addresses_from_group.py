import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.get_addresses_from_group import GetAddressesFromGroup
from komand_palo_alto_pan_os.actions.get_addresses_from_group.schema import (
    GetAddressesFromGroupInput,
    GetAddressesFromGroupOutput,
    Input,
)
from parameterized import parameterized

from util import Util


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
            ],
            [
                "single_member_group_with_attributes",
                "Single Dirty Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "fqdn_addresses": ["test.com"],
                    "ipv4_addresses": [],
                    "ipv6_addresses": [],
                    "all_addresses": ["test.com"],
                },
            ],
            [
                "single_member_group",
                "Single Bare Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "fqdn_addresses": ["test.com"],
                    "ipv4_addresses": [],
                    "ipv6_addresses": [],
                    "all_addresses": ["test.com"],
                },
            ],
            [
                "several_member_group_without_attributes",
                "Multi Bare Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "fqdn_addresses": ["test.com"],
                    "ipv4_addresses": ["1.1.1.1"],
                    "ipv6_addresses": ["abcd:123::1"],
                    "all_addresses": ["1.1.1.1", "test.com", "abcd:123::1"],
                },
            ],
            [
                "group_with_no_members",
                "Empty Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "fqdn_addresses": [],
                    "ipv4_addresses": [],
                    "ipv6_addresses": [],
                    "all_addresses": [],
                },
            ],
        ]
    )
    def test_get_addresses_from_group(
        self,
        mock_get: MagicMock,
        name: str,
        group: str,
        device_name: str,
        virtual_system: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(GetAddressesFromGroup())
        input_data = {Input.GROUP: group, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system}
        validate(input_data, GetAddressesFromGroupInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, GetAddressesFromGroupOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_group",
                "Invalid Group",
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find group 'Invalid Group', or group was empty. Check the name, virtual system name, and device name.\nDevice name: localhost.localdomain\nVirtual system: vsys1\n",
            ],
            [
                "dynamic_group",
                "Dynamic Group",
                "localhost.localdomain",
                "vsys1",
                "The address group 'Dynamic Group' is not a static address group.",
                "This action can only read and change the members of a static address group. The members of a "
                "dynamic address group are selected by its tag filter and cannot be changed directly.",
            ],
        ]
    )
    def test_get_addresses_from_group_bad(
        self,
        mock_get: MagicMock,
        name: str,
        group: str,
        device_name: str,
        virtual_system: str,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(GetAddressesFromGroup())
        input_data = {Input.GROUP: group, Input.DEVICE_NAME: device_name, Input.VIRTUAL_SYSTEM: virtual_system}
        validate(input_data, GetAddressesFromGroupInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
