import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath("../"))
from icon_cisco_firepower_management_center.actions.block_url_policy import BlockUrlPolicy
from icon_cisco_firepower_management_center.actions.block_url_policy.schema import Input
from jsonschema import validate

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestBlockUrlPolicy(TestCase):
    def test_block_url_policy(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_request_get: MagicMock,
        mock_create: MagicMock,
    ) -> None:
        action = Util.default_connector(BlockUrlPolicy())
        actual = action.run(
            {
                Input.URL_OBJECTS: [{"name": "example.com", "url": "https://example.com"}],
                Input.ACCESS_POLICY: "Test_Policy",
                Input.RULE_NAME: "Test_Rule",
            }
        )
        validate(actual, action.output.schema)
        expected = {"success": True}
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request_get.assert_called()
        # mock_request.assert_called()
        mock_create.assert_called()
