import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.get_host import GetHost
from icon_infoblox.actions.get_host.schema import Input

from unit_test.mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestGetHost(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(GetHost())

        self.params = {Input.REF: ""}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_get_host(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected_response = {}
        self.assertEqual(response, expected_response)
