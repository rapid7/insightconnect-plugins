import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_gitlab.actions.block_user import BlockUser
from icon_gitlab.actions.block_user.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestBlockUser(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(BlockUser())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_block_user(self, mock_post: MagicMock) -> None:
        mocked_request(mock_post)
        response = self.action.run(self.params)

        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
