import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.add_address_object_to_group import AddAddressObjectToGroup
from komand_palo_alto_pan_os.actions.add_address_object_to_group.schema import (
    AddAddressObjectToGroupInput,
    AddAddressObjectToGroupOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestAddAddressObjectToGroup(TestCase):
    @parameterized.expand(
        [
            [
                "single_object",
                ["example.com"],
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["1.1.1.1", "test.com", "IPv6", "example.com"]},
            ],
            [
                "several_objects",
                ["example.com", "2.2.2.2", "New IPv6 Address"],
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {
                    "success": True,
                    "address_objects": ["1.1.1.1", "test.com", "IPv6", "example.com", "2.2.2.2", "New IPv6 Address"],
                },
            ],
            [
                "empty_list",
                [],
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["1.1.1.1", "test.com", "IPv6"]},
            ],
            [
                "already_added",
                ["test.com"],
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["1.1.1.1", "test.com", "IPv6"]},
            ],
        ]
    )
    def test_add_address_object_to_group(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: list[str],
        group: str,
        device_name: str,
        virtual_system: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(AddAddressObjectToGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, AddAddressObjectToGroupInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, AddAddressObjectToGroupOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_group",
                ["example.com"],
                "Invalid Group",
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find group 'Invalid Group', or group was empty. Check the name, virtual system name, and device name.\nDevice name: localhost.localdomain\nVirtual system: vsys1\n",
            ],
        ]
    )
    def test_add_address_object_to_group_bad(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: list[str],
        group: str,
        device_name: str,
        virtual_system: str,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(AddAddressObjectToGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, AddAddressObjectToGroupInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
