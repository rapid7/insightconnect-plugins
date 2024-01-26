import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.add_issue_label.action import AddIssueLabel
from komand_github.actions.add_issue_label.schema import AddIssueLabelInput, AddIssueLabelOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestAddIssueLabel(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(AddIssueLabel())

    @parameterized.expand(
        [
            [
                "valid_add_issue_label_both",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "issue_number": 1,
                    "label": "test_label",
                },
                {"success": True},
            ],
            [
                "valid_add_issue_label_repo",
                {"repository": "test_repository", "issue_number": 1, "label": "test_label"},
                {"success": True},
            ],
        ]
    )
    def test_add_issue_label_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, AddIssueLabelOutput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, AddIssueLabelOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_add_issue_label_403",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "issue_number": 403,
                    "label": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github",
                "Account may need org permissions added",
                "",
            ],
            [
                "invalid_add_issue_label_404",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "issue_number": 404,
                    "label": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github",
                "The issue, org or repo could not be found",
                "",
            ],
            [
                "invalid_add_issue_label_error",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "issue_number": 500,
                    "label": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured when trying to add label to get issue information",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
        ]
    )
    def test_add_issue_label_invalid(
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
        validate(input_params, AddIssueLabelInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(AddIssueLabel(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
