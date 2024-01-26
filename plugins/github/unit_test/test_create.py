import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.create.action import Create
from komand_github.actions.create.schema import CreateInput, CreateOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestCreateIssue(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(Create())

    @parameterized.expand(
        [
            [
                "valid_create_issue_all_fields",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"},
            ],
            [
                "valid_create_issue_min_fields_org",
                {
                    "organization": "test_organization",
                    "repository": "test_repository",
                    "title": "test_title",
                    "body": "test_body",
                },
                {"url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"},
            ],
            [
                "valid_create_issue_min_fields_reop",
                {"repository": "test_repository", "title": "test_title", "body": "test_body"},
                {"url": "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"},
            ],
        ]
    )
    def test_create_issue_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, CreateInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, CreateOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_create_in_org_403",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_403",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github",
                "Account may need org permissions added",
                "",
            ],
            [
                "invalid_create_in_org_404",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_404",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github",
                "The org or repo could not be found",
                "",
            ],
            [
                "invalid_create_in_org_error",
                {
                    "organization": "test_organization",
                    "repository": "test_repository_error",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured when trying to add label to get repo information",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_create_in_repo_403",
                {
                    "repository": "test_repository_403",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github",
                "Account may need org permissions added",
                "",
            ],
            [
                "invalid_create_in_repo_404",
                {
                    "repository": "test_repository_404",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github",
                "The repo could not be found",
                "",
            ],
            [
                "invalid_create_in_repo_error",
                {
                    "repository": "test_repository_error",
                    "title": "test_title",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured when trying to add label to get repo information",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_create_error",
                {
                    "repository": "test_repository_error",
                    "title": "error",
                    "body": "test_body",
                    "assignee": "test_assignee",
                    "milestone": 1,
                    "labels": "test_label",
                },
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured when trying to add label to get repo information",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
        ]
    )
    def test_create_invalid(
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
        validate(input_params, CreateInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(Create(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
