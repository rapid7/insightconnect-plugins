import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.check_server_status import CheckServerStatus
from icon_joe_sandbox.actions.check_server_status.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestCheckServerStatus(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(CheckServerStatus())

    @patch("requests.request", side_effect=mock_request_200)
    def test_check_server_status(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()

        expected = {Output.ONLINE: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
