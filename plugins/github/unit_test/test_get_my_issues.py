import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.get_my_issues.action import GetMyIssues
from komand_github.actions.get_my_issues.schema import GetMyIssuesInput, GetMyIssuesOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestGetMyIssues(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector((GetMyIssues()))

    @parameterized.expand(
        [["valid_get_my_issues", {}, Util.read_file_to_dict("expected/get_my_issues_valid.json.exp")]]
    )
    def test_get_my_issues_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, GetMyIssuesInput.schema)
        actual = self.action.run()
        self.assertDictEqual(actual, expected)
        validate(actual, GetMyIssuesOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_get_my_issues_403",
                {},
                {"credentials": {"username": "integrationalliance", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_get_my_issues_500",
                {},
                {"credentials": {"username": "integrationalliance", "personal_token": {"secretKey": "error_500"}}},
                "Error occoured.",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_get_my_issues_bad_json",
                {},
                {"credentials": {"username": "integrationalliance", "personal_token": {"secretKey": "error_bad_json"}}},
                "Error occoured when trying to get my issues.",
                "Please check that the provided inputs are correct and try again.",
                "Expecting value: line 1 column 1 (char 0)",
            ],
        ]
    )
    def test_get_my_issues_invalid(
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
        validate(input_params, GetMyIssuesInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(GetMyIssues(), input_connection).run()
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
