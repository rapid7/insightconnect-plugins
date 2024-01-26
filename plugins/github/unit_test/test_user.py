import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.user.action import User
from komand_github.actions.user.schema import UserInput, UserOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestUser(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(User())

    @parameterized.expand(
        [
            [
                "valid_user",
                {"username": "test_fetch_user"},
                {
                    "name": "test user",
                    "bio": "this is a bio",
                    "email": "test@test.com",
                    "avatar": "https://avatars.githubusercontent.com/u/144030336?v=4",
                    "url": "https://github.com/test_fetch_user",
                },
            ],
        ]
    )
    def test_search_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, UserInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, UserOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_user_404",
                {"username": "test_user_invalid_404"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github",
                "The user: test_user_invalid_404 could not be found",
                "",
            ],
        ]
    )
    def test_get_repo_invalid(
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
        validate(input_params, UserInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(User(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
