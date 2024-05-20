import sys
import os

sys.path.append(os.path.abspath("../"))
from unittest import TestCase, mock
from unittest.mock import Mock
from icon_infoblox.actions.delete_host import DeleteHost
from icon_infoblox.actions.delete_host.schema import Input


from unit_test.mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestDeleteHost(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DeleteHost())

        self.params = {Input.REF: ""}

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_delete_host(self, mock_delete):
        mocked_request(mock_delete)
        response = self.action.run(self.params)
        expected_response = {}
        self.assertEqual(response, expected_response)
