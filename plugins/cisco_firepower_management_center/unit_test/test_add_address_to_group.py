import sys
import os

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.add_address_to_group import AddAddressToGroup
from icon_cisco_firepower_management_center.actions.add_address_to_group.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
class TestAddAddressToGroup(TestCase):
    @parameterized.expand(Util.load_parameters("add_address_to_group").get("parameters"))
    def test_add_address_to_group(
        self, mock_post, mock_request, mock_write, mock_connect, mock_recv, name, address, group, expected
    ):
        action = Util.default_connector(AddAddressToGroup())
        actual = action.run({Input.ADDRESS: address, Input.GROUP: group})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "address_object_not_exists",
                "3.3.3.3",
                "Test_Group",
                "The address 3.3.3.3 or group Test_Group does not exist in Cisco Firepower.",
                "Please enter valid names and try again.",
            ],
            [
                "address_group_not_exists",
                "1.1.1.1",
                "Invalid_Group",
                "The address 1.1.1.1 or group Invalid_Group does not exist in Cisco Firepower.",
                "Please enter valid names and try again.",
            ],
        ]
    )
    def test_add_address_to_group_bad(
        self, mock_post, mock_request, mock_write, mock_connect, mock_recv, name, address, group, cause, assistance
    ):
        action = Util.default_connector(AddAddressToGroup())
        with self.assertRaises(PluginException) as error:
            action.run({Input.ADDRESS: address, Input.GROUP: group})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
