import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.get_user_groups import GetUserGroups
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestGetUserGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserGroups())

    @parameterized.expand(
        [
            [
                "by_id_success",
                Util.read_file_to_dict("inputs/get_user_groups_by_id_success.json.inp"),
                Util.read_file_to_dict("expected/get_user_groups_by_id_success.json.exp"),
            ],
            [
                "by_login_success",
                Util.read_file_to_dict("inputs/get_user_groups_by_login_success.json.inp"),
                Util.read_file_to_dict("expected/get_user_groups_by_login_success.json.exp"),
            ],
            [
                "by_login_success",
                Util.read_file_to_dict("inputs/get_user_groups_empty.json.inp"),
                Util.read_file_to_dict("expected/get_user_groups_empty.json.exp"),
            ],
        ]
    )
    def test_get_user_groups(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "id_not_found",
                Util.read_file_to_dict("inputs/get_user_groups_invalid_id.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "login_not_found",
                Util.read_file_to_dict("inputs/get_user_groups_invalid_login.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_get_user_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
