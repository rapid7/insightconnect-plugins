import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.get_server_info import GetServerInfo
from icon_joe_sandbox.actions.get_server_info.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestGetServerInfo(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetServerInfo())

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_server_info(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()

        expected = {Output.QUEUESIZE: 3}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
