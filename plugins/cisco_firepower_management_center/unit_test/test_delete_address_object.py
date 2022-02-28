import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.delete_address_object import DeleteAddressObject
from icon_cisco_firepower_management_center.actions.delete_address_object.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
class TestDeleteAddressObject(TestCase):
    @parameterized.expand(Util.load_parameters("delete_address_object").get("parameters"))
    def test_delete_address_object(
        self, mock_post, mock_request, mock_write, mock_connect, mock_recv, name, address_object, expected
    ):
        action = Util.default_connector(DeleteAddressObject())
        actual = action.run({Input.ADDRESS_OBJECT: address_object})
        self.assertEqual(actual, expected)
