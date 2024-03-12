import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.delete_ssh import DeleteSsh
from icon_gitlab.actions.delete_ssh.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestDeleteSsh(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DeleteSsh())
        self.params = {Input.ID: "123", Input.KEY_ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_delete_ssh(self, mock_delete: MagicMock) -> None:
        mocked_request(mock_delete)
        response = self.action.run(self.params)

        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
