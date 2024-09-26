import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.add_user_to_group import AddUserToGroup
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestAddUserToGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddUserToGroup())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/add_user_to_group_success.json.inp"),
                Util.read_file_to_dict("expected/add_user_to_group_success.json.exp"),
            ],
            [
                "user_already_in_group",
                Util.read_file_to_dict("inputs/add_user_to_group_user_already_in_group.json.inp"),
                Util.read_file_to_dict("expected/add_user_to_group_success.json.exp"),
            ],
        ]
    )
    def test_add_user_to_group(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "group_not_found",
                Util.read_file_to_dict("inputs/add_user_to_group_group_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/add_user_to_group_user_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_add_user_to_group_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
