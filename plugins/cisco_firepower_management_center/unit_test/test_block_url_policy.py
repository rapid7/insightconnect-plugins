import sys
import os

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.block_url_policy import BlockUrlPolicy
from icon_cisco_firepower_management_center.actions.block_url_policy.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
class TestBlockUrlPolicy(TestCase):
    def test_block_url_policy(self, mock_post, mock_request, request_get, mock_write, mock_connect, mock_recv):
        action = Util.default_connector(BlockUrlPolicy())
        actual = action.run(
            {
                Input.URL_OBJECTS: [{"name": "example.com", "url": "https://example.com"}],
                Input.ACCESS_POLICY: "Test_Policy",
                Input.RULE_NAME: "Test_Rule",
            }
        )
        expected = {"success": True}
        self.assertEqual(actual, expected)
