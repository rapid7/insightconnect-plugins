import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.create_issue_comment.action import CreateIssueComment
from komand_github.actions.create_issue_comment.schema import CreateIssueCommentInput, CreateIssueCommentOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestCreateIssueComment(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(CreateIssueComment())

    @parameterized.expand(
        [
            [
                "valid_create_issue_comment_org",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "body": "test_body",
                    "issue_number": 1,
                },
                {"url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"},
            ],
            [
                "valid_create_issue_comment_repo",
                {"repository": "test_repository", "body": "test_body", "issue_number": 1},
                {"url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"},
            ],
        ]
    )
    def test_create_issue_comment_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, CreateIssueCommentInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, CreateIssueCommentOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_create_issue_comment_in_org_403",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_403",
                    "body": "test_body",
                    "issue_number": 1,
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_create_issue_comment_in_org_404",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_404",
                    "body": "test_body",
                    "issue_number": 1,
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_create_issue_comment_in_org_error",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_error",
                    "body": "test_body",
                    "issue_number": 1,
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_create_issue_comment_in_repo_403",
                {"repository": "test_repository_403", "body": "test_body", "issue_number": 1},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_create_issue_comment_in_repo_404",
                {"repository": "test_repository_404", "body": "test_body", "issue_number": 1},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_create_issue_comment_in_repo_error",
                {"repository": "test_repository_error", "body": "test_body", "issue_number": 1},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_create_error",
                {"repository": "test_repository", "body": "error in body", "issue_number": 1},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
        ]
    )
    def test_create_issue_comment_invalid(
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
        validate(input_params, CreateIssueCommentInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(CreateIssueComment(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
