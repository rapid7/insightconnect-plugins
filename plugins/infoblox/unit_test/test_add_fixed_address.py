import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.add_fixed_address import AddFixedAddress
from icon_infoblox.actions.add_fixed_address.schema import Input

from unit_test.mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestAddFixedAddress(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(AddFixedAddress())

        self.params = {Input.ADDRESS: ""}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_add_fixed_address(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected_response = {}
        self.assertEqual(response, expected_response)
