import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.unblock_user.action import UnblockUser
from komand_github.actions.unblock_user.schema import UnblockUserInput, UnblockUserOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.delete", side_effect=Util.mock_delete_request)
class TestUnBlockUser(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(UnblockUser())

    @parameterized.expand(
        [
            [
                "valid_unblock_user",
                {"username": "test_name"},
                {"success": True},
            ],
            [
                "valid_unblock_user_with_symbols",
                {"username": "!@£$%^&**()"},
                {"success": True},
            ],
        ]
    )
    def test_unblock_user_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, UnblockUserInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, UnblockUserOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_unblock_user_404",
                {"username": "error_404"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_unblock_user_500",
                {"username": "error_500"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_500"}}},
                "Error occoured.",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_unblock_user",
                {"username": "error"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error"}}},
                "An error has occurred while trying to unblock a user.",
                "Please check that the provided inputs are correct and try again.",
                "this is an error",
            ],
        ]
    )
    def test_unblock_user_invalid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        input_connection: dict,
        cause: str,
        assistance: str,
        data: list,
    ):
        validate(input_params, UnblockUserInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(UnblockUser(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
