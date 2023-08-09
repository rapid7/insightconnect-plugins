import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.reset_password import ResetPassword
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestResetPassword(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ResetPassword())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/reset_password.json.inp"),
                Util.read_file_to_dict("expected/reset_password.json.exp"),
            ],
            [
                "success_with_temp_password",
                Util.read_file_to_dict("inputs/reset_password_with_temp_password.json.inp"),
                Util.read_file_to_dict("expected/reset_password_with_temp_password.json.exp"),
            ],
        ]
    )
    def test_reset_password(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_user_id",
                Util.read_file_to_dict("inputs/reset_password_invalid_user_id.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_reset_password_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
