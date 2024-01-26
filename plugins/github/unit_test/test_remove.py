import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.remove.action import Remove
from komand_github.actions.remove.schema import RemoveInput, RemoveOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.get", side_effect=Util.mock_get_request)
class TestRemove(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(Remove())

    @parameterized.expand(
        [
            [
                "valid_remove_from_repo_in_org",
                {"organization": "test_organization", "repository": "test_repository", "username": "test_user"},
                {"status": "Successfully removed test_user from the repo test_repository in test_organization"},
            ],
            [
                "valid_remove_from_repo",
                {"repository": "test_repository", "username": "test_user"},
                {"status": "Successfully removed test_user from the repo test_repository"},
            ],
            [
                "valid_remove_from_org",
                {"organization": "test_organization", "username": "test_user"},
                {"status": "Successfully removed test_user from the Organization test_organization"},
            ],
        ]
    )
    def test_remove_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, RemoveInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, RemoveOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_remove_from_repo_in_org_403",
                {"organization": "test_organization", "repository": "test_repository", "username": "test_user_403"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_remove_from_repo_in_org_404",
                {"organization": "test_organization", "repository": "test_repository", "username": "test_user_404"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_remove_from_repo_in_org_error",
                {"organization": "test_organization", "repository": "test_repository", "username": "test_user_error"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_remove_from_repo__403",
                {"repository": "test_repository", "username": "test_user_403"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_remove_from_repo_404",
                {"repository": "test_repository", "username": "test_user_404"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_remove_from_repo_error",
                {"repository": "test_repository", "username": "test_user_error"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_remove_from_org_403",
                {"organization": "test_organization", "username": "test_user_403"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_remove_from_repo_in_org_404",
                {"organization": "test_organization", "username": "test_user_404"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error_404"}}},
                "Not Found response returned from Github.",
                "The requested resource could not be found.",
                "404",
            ],
            [
                "invalid_remove_from_repo_in_org_error",
                {"organization": "test_organization", "username": "test_user_error"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Error occoured",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_username",
                {"organization": "test_organization", "username": "test_user"},
                {"credentials": {"username": "test_user", "personal_token": {"secretKey": "error"}}},
                "Cannot remove your own username.",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
        ]
    )
    def test_remove_invalid(
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
        validate(input_params, RemoveInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(Remove(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
