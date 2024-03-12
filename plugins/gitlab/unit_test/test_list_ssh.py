import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.list_ssh import ListSsh
from icon_gitlab.actions.list_ssh.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestListSsh(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListSsh())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_list_ssh(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {Output.SSH_KEYS: []}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
