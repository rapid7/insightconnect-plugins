import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_pagerduty.actions.create_user import CreateUser
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestCreateUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateUser())

    @parameterized.expand(
        [
            [
                "minimum_valid",
                Util.read_file_to_dict("inputs/create_user_minimum_fields.json.inp"),
                Util.read_file_to_dict("expected/create_user_minimum_fields.json.exp"),
            ],
            [
                "additional_fields_valid",
                Util.read_file_to_dict("inputs/create_user_additional_fields.json.inp"),
                Util.read_file_to_dict("expected/create_user_additional_fields.json.exp"),
            ],
        ]
    )
    def test_create_user_valid(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "missing_params_invalid",
                {},
                "Missing required paramaters",
                "Please ensure a valid 'from_email', 'new_users_email' and 'name' is provided",
            ]
        ]
    )
    def test_missing_params_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "api_error_invalid",
                Util.read_file_to_dict("inputs/create_user_api_error_fields.json.inp"),
                "Server error occurred",
                "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_api_error_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
