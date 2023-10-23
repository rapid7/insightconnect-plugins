import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_pagerduty.actions.get_user_by_email import GetUserByEmail
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException

@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGetUserByEmail(TestCase):
   
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserByEmail())

    @parameterized.expand(
        [
            [
                "get_user_valid",
                {"user_email": "valid_email"},
                Util.read_file_to_dict("expected/get_user_by_email_valid.json.exp"),
            ]
        ]
    )
    def test_get_user_by_email_valid(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "no_users_found",
                {"user_email": "invalid_email"},
                "No user found for email invalid_email"
            ]
        ]
    )
    def test_get_user_by_email_invalid(
        self, _mock_request: MagicMock, _test_name: str, input_params: dict, cause: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)