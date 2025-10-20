import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.expire_password import ExpirePassword
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestExpirePassword(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ExpirePassword())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/expire_password.json.inp"),
                Util.read_file_to_dict("expected/expire_password.json.exp"),
            ],
            [
                "success_with_temp_password",
                Util.read_file_to_dict("inputs/expire_password_with_temp_password.json.inp"),
                Util.read_file_to_dict("expected/expire_password_with_temp_password.json.exp"),
            ],
        ]
    )
    def test_expire_password(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    def test_expire_password_with_invalid_user_id(self, mock_request: MagicMock) -> None:
        input_parameters = Util.read_file_to_dict("inputs/expire_password_invalid_user_id.json.inp")
        cause = "Invalid or unreachable endpoint provided."
        assistance = "Verify your input is correct and not malformed and try again. If the issue persists, please contact support."

        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
