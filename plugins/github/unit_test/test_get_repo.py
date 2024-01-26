import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.get_repo.action import GetRepo
from komand_github.actions.get_repo.schema import GetRepoInput, GetRepoOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestGetRepo(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(GetRepo())

    @parameterized.expand(
        [
            [
                "valid_get_repo",
                {"title": "test_repo_valid", "owner": "test_owner"},
                Util.read_file_to_dict("expected/get_repo_valid.json.exp"),
            ],
            [
                "valid_get_repo_with_symbols",
                {"title": "test_repo_valid", "owner": "!@£$%^&**()"},
                Util.read_file_to_dict("expected/get_repo_valid.json.exp"),
            ],
        ]
    )
    def test_get_repo_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, GetRepoInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, GetRepoOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_get_repo_403",
                {
                    "title": "test_repo_invalid",
                    "owner": "test_owner",
                },
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github",
                "Account may need org permissions added",
                "",
            ],
            [
                "invalid_get_repo_500",
                {"title": "test_repo_invalid", "owner": "test_owner"},
                {"credentials": {"username": "integrationalliance", "personal_token": {"secretKey": "error_500"}}},
                "A status code of 500 was returned from Github",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_get_repo_bad_json",
                {"title": "test_repo_invalid", "owner": "test_owner"},
                {"credentials": {"username": "integrationalliance", "personal_token": {"secretKey": "error_bad_json"}}},
                "Error occoured when trying to get repo",
                "Please check that the provided inputs are correct and try again.",
                "Expecting value: line 1 column 1 (char 0)",
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
        validate(input_params, GetRepoInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(GetRepo(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
