import sys
import os

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.check_if_address_in_group import CheckIfAddressInGroup
from icon_cisco_firepower_management_center.actions.check_if_address_in_group.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
class TestCheckIfAddressInGroup(TestCase):
    @parameterized.expand(Util.load_parameters("check_if_address_in_group").get("parameters"))
    def test_check_if_address_in_group(
        self,
        mock_post,
        mock_request,
        mock_write,
        mock_connect,
        mock_recv,
        name,
        address,
        group,
        enable_search,
        expected,
    ):
        self.maxDiff = None
        action = Util.default_connector(CheckIfAddressInGroup())
        actual = action.run({Input.ADDRESS: address, Input.GROUP: group, Input.ENABLE_SEARCH: enable_search})
        self.assertEqual(actual, expected)
