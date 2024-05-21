import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.search_by_mac import SearchByMac
from icon_infoblox.actions.search_by_mac.schema import Input

from mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestSearchByMac(TestCase):
    @mock.patch("icon_infoblox.util.infoblox.InfobloxConnection._validate_connection", return_value=True)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(SearchByMac())

        self.params = {Input.MAC: "00-B0-D0-63-C2-26"}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_search_by_mac(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected_response = {"result": []}
        self.assertEqual(response, expected_response)
