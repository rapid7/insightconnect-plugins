import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.modify_host import ModifyHost
from icon_infoblox.actions.modify_host.schema import Input

from unit_test.mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestModifyHost(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(ModifyHost())

        self.params = {Input.REF: "", Input.UPDATED_HOST: ""}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_modify_host(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run(self.params)
        expected_response = {}
        self.assertEqual(response, expected_response)
