import os
import sys

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_firepower_management_center.actions.remove_address_from_group import RemoveAddressFromGroup
from icon_cisco_firepower_management_center.actions.remove_address_from_group.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestRemoveAddressFromGroup(TestCase):
    @parameterized.expand(Util.load_parameters("remove_address_from_group").get("parameters"))
    def test_remove_address_from_group(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address: str,
        group: str,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(RemoveAddressFromGroup())
        actual = action.run({Input.ADDRESS: address, Input.GROUP: group})
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()

    @parameterized.expand(
        [
            [
                "address_object_not_exists",
                "3.3.3.3",
                "Test_Group_1",
                "The address 3.3.3.3 or group Test_Group_1 does not exist in Cisco Firepower.",
                "Please enter valid names and try again.",
            ],
            [
                "address_group_not_exists",
                "1.1.1.1",
                "Invalid_Group",
                "The address 1.1.1.1 or group Invalid_Group does not exist in Cisco Firepower.",
                "Please enter valid names and try again.",
            ],
            [
                "object_not_in_group",
                "test.com",
                "Test_Group_1",
                "The address test.com does not exist in the address group.",
                "Please enter valid name and try again.",
            ],
        ]
    )
    def test_remove_address_from_group_bad(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address: str,
        group: str,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(RemoveAddressFromGroup())
        with self.assertRaises(PluginException) as error:
            action.run({Input.ADDRESS: address, Input.GROUP: group})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()
