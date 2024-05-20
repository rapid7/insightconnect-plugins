import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.search_by_ip import SearchByIp
from icon_infoblox.actions.search_by_ip.schema import Input


from unit_test.mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestSearchByIp(TestCase):
    @mock.patch("icon_infoblox.util.infoblox.InfobloxConnection._validate_connection", return_value=True)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(SearchByIp())
        self.params = {Input.IP: "192.168.0.1"}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_search_by_ip(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected_response = {}
        self.assertEqual(response, expected_response)
