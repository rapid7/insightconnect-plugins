import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.block_user.action import BlockUser
from komand_github.actions.block_user.schema import BlockUserInput, BlockUserOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.put", side_effect=Util.mock_put_request)
class TestBlockUser(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(BlockUser())

    @parameterized.expand(
        [
            [
                "valid_block_user",
                {"username": "test_name"},
                {"success": True},
            ],
            [
                "valid_block_user_with_symbols",
                {"username": "!@£$%^&**()"},
                {"success": True},
            ],
        ]
    )
    def test_block_user_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, BlockUserInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, BlockUserOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_block_user_404",
                {"username": "error_404"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_404"}}},
                "The user: error_404, could not be found",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_block_user_422",
                {"username": "error_422"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_422"}}},
                "The user: error_422, has already been blocked",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_block_user_500",
                {"username": "error_500"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_500"}}},
                "An error has occurred while trying to block a user",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_block_user",
                {"username": "error"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error"}}},
                "An error has occurred while trying to block a user",
                "Please check that the provided inputs are correct and try again.",
                "this is an error",
            ],
        ]
    )
    def test_block_user_invalid(
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
        validate(input_params, BlockUserInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(BlockUser(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
