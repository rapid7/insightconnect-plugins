import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.get_account_info import GetAccountInfo
from icon_joe_sandbox.actions.get_account_info.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestGetAccountInfo(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(GetAccountInfo())

    @patch("requests.request", side_effect=mock_request_200)
    def test_get_account_info(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run()

        expected = {
            Output.TYPE: "desktop",
            Output.QUOTA: {
                "daily": {"current": 0, "limit": 30, "remaining": 30},
                "monthly": {"current": 0, "limit": 30, "remaining": 30},
            },
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
