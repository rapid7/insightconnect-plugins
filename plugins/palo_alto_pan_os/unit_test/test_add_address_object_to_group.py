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
            [
                "duplicates_in_input",
                ["example.com", "example.com"],
                "Test Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["1.1.1.1", "test.com", "IPv6", "example.com"]},
            ],
            [
                "single_member_group_with_attributes",
                ["example.com"],
                "Single Dirty Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["test.com", "example.com"]},
            ],
            [
                "single_member_group",
                ["example.com"],
                "Single Bare Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["test.com", "example.com"]},
            ],
            [
                "several_member_group_without_attributes",
                ["example.com"],
                "Multi Bare Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["1.1.1.1", "test.com", "IPv6", "example.com"]},
            ],
            [
                "group_with_no_members",
                ["example.com"],
                "Empty Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True, "address_objects": ["example.com"]},
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
            [
                "dynamic_group",
                ["example.com"],
                "Dynamic Group",
                "localhost.localdomain",
                "vsys1",
                "The address group 'Dynamic Group' is not a static address group.",
                "This action can only read and change the members of a static address group. The members of a "
                "dynamic address group are selected by its tag filter and cannot be changed directly.",
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
        # A group that could not be read is never written to
        self.assertEqual([call for call in Util.calls if call.get("action") != "get"], [])

    @parameterized.expand(
        [
            [
                "single_member_group_with_attributes",
                ["example.com"],
                "Single Dirty Group",
                "<static><member>example.com</member></static>",
            ],
            [
                "several_member_group_without_attributes",
                ["example.com", "2.2.2.2"],
                "Multi Bare Group",
                "<static><member>example.com</member><member>2.2.2.2</member></static>",
            ],
            [
                "group_with_no_members",
                ["example.com"],
                "Empty Group",
                "<static><member>example.com</member></static>",
            ],
        ]
    )
    def test_add_address_object_to_group_sends_only_new_members(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: list[str],
        group: str,
        expected_element: str,
    ) -> None:
        action = Util.default_connector(AddAddressObjectToGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: "localhost.localdomain",
            Input.VIRTUAL_SYSTEM: "vsys1",
        }
        validate(input_data, AddAddressObjectToGroupInput.schema)
        action.run(input_data)

        # The members already in the group are never resent, so a concurrent change to the group
        # cannot be undone by this action
        writes = [call for call in Util.calls if call.get("action") != "get"]
        self.assertEqual(len(writes), 1)
        self.assertEqual(writes[0].get("action"), "set")
        self.assertEqual(
            writes[0].get("xpath"),
            f"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']"
            f"/address-group/entry[@name='{group}']",
        )
        self.assertEqual(writes[0].get("element"), expected_element)

    @parameterized.expand(
        [
            ["already_added", ["test.com"], "Test Group"],
            ["empty_list", [], "Test Group"],
        ]
    )
    def test_add_address_object_to_group_writes_nothing(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: list[str],
        group: str,
    ) -> None:
        action = Util.default_connector(AddAddressObjectToGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: "localhost.localdomain",
            Input.VIRTUAL_SYSTEM: "vsys1",
        }
        validate(input_data, AddAddressObjectToGroupInput.schema)
        action.run(input_data)

        self.assertEqual([call for call in Util.calls if call.get("action") != "get"], [])
