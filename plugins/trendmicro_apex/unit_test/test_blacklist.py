import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.blacklist import Blacklist
from icon_trendmicro_apex.actions.blacklist.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestBlacklist(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(Blacklist())
        self.params = {
            Input.INDICATOR: "https://www.example.com",
            Input.SCAN_ACTION: "BLOCK",
            Input.DESCRIPTION: "EXAMPLE",
            Input.EXPIRY_DATE: 30,
            Input.BLACKLIST_STATE: True,
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_blacklist(self, mock_post, mock_token):
        mocked_request(mock_post)
        response = self.action.run(self.params)

        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
