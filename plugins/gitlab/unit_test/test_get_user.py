import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_gitlab.actions.get_user import GetUser
from icon_gitlab.actions.get_user.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestGetUser(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetUser())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_user(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {Output.USER: response}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
