import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.remove_address_object_from_group import RemoveAddressObjectFromGroup
from komand_palo_alto_pan_os.actions.remove_address_object_from_group.schema import (
    Input,
    RemoveAddressObjectFromGroupInput,
    RemoveAddressObjectFromGroupOutput,
)
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestRemoveAddressObjectFromGroup(TestCase):
    @parameterized.expand(
        [
            ["success", "test.com", "Test Group", "localhost.localdomain", "vsys1", {"success": True}],
            ["not_found", "example.com", "Test Group", "localhost.localdomain", "vsys1", {"success": False}],
            [
                "several_member_group_without_attributes",
                "test.com",
                "Multi Bare Group",
                "localhost.localdomain",
                "vsys1",
                {"success": True},
            ],
            [
                "not_in_single_member_group",
                "example.com",
                "Single Bare Group",
                "localhost.localdomain",
                "vsys1",
                {"success": False},
            ],
            [
                "group_with_no_members",
                "example.com",
                "Empty Group",
                "localhost.localdomain",
                "vsys1",
                {"success": False},
            ],
            # A member name that is only a prefix of a real member is not a member
            ["partial_name", "test", "Multi Bare Group", "localhost.localdomain", "vsys1", {"success": False}],
        ]
    )
    def test_remove_address_object_from_group(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: str,
        group: str,
        device_name: str,
        virtual_system: str,
        expected: dict,
    ) -> None:
        action = Util.default_connector(RemoveAddressObjectFromGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, RemoveAddressObjectFromGroupInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, RemoveAddressObjectFromGroupOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_group",
                "example.com",
                "Invalid Group",
                "localhost.localdomain",
                "vsys1",
                "PAN OS returned an unexpected response.",
                "Could not find group 'Invalid Group', or group was empty. Check the name, virtual system name, and device name.\ndevice name: localhost.localdomain\nvirtual system: vsys1",
            ],
            [
                "dynamic_group",
                "test.com",
                "Dynamic Group",
                "localhost.localdomain",
                "vsys1",
                "The address group 'Dynamic Group' is not a static address group.",
                "This action can only read and change the members of a static address group. The members of a "
                "dynamic address group are selected by its tag filter and cannot be changed directly.",
            ],
        ]
    )
    def test_remove_address_object_from_group_bad(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: str,
        group: str,
        device_name: str,
        virtual_system: str,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(RemoveAddressObjectFromGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: device_name,
            Input.VIRTUAL_SYSTEM: virtual_system,
        }
        validate(input_data, RemoveAddressObjectFromGroupInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        # Nothing is written when the removal cannot be carried out
        self.assertEqual([call for call in Util.calls if call.get("action") != "get"], [])

    @parameterized.expand(
        [
            ["several_member_group_with_attributes", "test.com", "Test Group"],
            ["several_member_group_without_attributes", "IPv6", "Multi Bare Group"],
            # Removing the only member of a group leaves the group with no members, which PAN-OS is
            # likely to reject. That is pre-existing behaviour and deciding what the plugin should do
            # instead is a product question, so these rows pin it rather than change it.
            ["last_member", "test.com", "Single Bare Group"],
            ["last_member_with_attributes", "test.com", "Single Dirty Group"],
        ]
    )
    def test_remove_address_object_from_group_deletes_only_that_member(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: str,
        group: str,
    ) -> None:
        action = Util.default_connector(RemoveAddressObjectFromGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: "localhost.localdomain",
            Input.VIRTUAL_SYSTEM: "vsys1",
        }
        validate(input_data, RemoveAddressObjectFromGroupInput.schema)
        action.run(input_data)

        # The one member is deleted where it sits, so the rest of the group is never rewritten and a
        # concurrent change to it cannot be lost
        writes = [call for call in Util.calls if call.get("action") != "get"]
        self.assertEqual(len(writes), 1)
        self.assertEqual(writes[0].get("action"), "delete")
        self.assertEqual(
            writes[0].get("xpath"),
            f"/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']"
            f"/address-group/entry[@name='{group}']/static/member[text()='{address_object}']",
        )
        self.assertIsNone(writes[0].get("element"))

    @parameterized.expand(
        [
            ["not_found", "example.com", "Test Group"],
            ["group_with_no_members", "example.com", "Empty Group"],
            ["partial_name", "test", "Multi Bare Group"],
        ]
    )
    def test_remove_address_object_from_group_writes_nothing(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address_object: str,
        group: str,
    ) -> None:
        action = Util.default_connector(RemoveAddressObjectFromGroup())
        input_data = {
            Input.ADDRESS_OBJECT: address_object,
            Input.GROUP: group,
            Input.DEVICE_NAME: "localhost.localdomain",
            Input.VIRTUAL_SYSTEM: "vsys1",
        }
        validate(input_data, RemoveAddressObjectFromGroupInput.schema)
        action.run(input_data)

        self.assertEqual([call for call in Util.calls if call.get("action") != "get"], [])
