import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.reset_password import ResetPassword
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


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
                "success_with_send_email",
                Util.read_file_to_dict("inputs/reset_password_with_send_email.json.inp"),
                Util.read_file_to_dict("expected/reset_password_with_send_email.json.exp"),
            ],
            [
                "success_with_revoke_sessions",
                Util.read_file_to_dict("inputs/reset_password_with_revoke_sessions.json.inp"),
                Util.read_file_to_dict("expected/reset_password_with_revoke_sessions.json.exp"),
            ],
        ]
    )
    def test_reset_password(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
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
    def test_reset_password_bad(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
