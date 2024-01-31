import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.add_collaborator.action import AddCollaborator
from komand_github.actions.add_collaborator.schema import AddCollaboratorInput, AddCollaboratorOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.put", side_effect=Util.mock_put_request)
class TestAddCollaborator(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(AddCollaborator())

    @parameterized.expand(
        [
            [
                "valid_add_collaborator",
                {
                    "username": "test_username",
                    "organization": "test_org",
                    "repository": "test_repo",
                    "permission": "admin",
                },
                Util.read_file_to_dict("expected/add_collaborator_valid.json.exp"),
            ],
        ]
    )
    def test_add_collaborator_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, AddCollaboratorInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, AddCollaboratorOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_add_collaborator_204",
                {
                    "username": "test_username",
                    "organization": "test_org",
                    "repository": "test_repo",
                    "permission": "admin",
                },
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_204"}}},
                "test_username is already a collaborator",
                "Please check that the provided inputs are correct and try again.",
                "204",
            ],
            [
                "invalid_add_collaborator_403",
                {
                    "username": "test_username",
                    "organization": "test_org",
                    "repository": "test_repo",
                    "permission": "admin",
                },
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github.",
                "Account may need org permissions added.",
                "403",
            ],
            [
                "invalid_add_collaborator_500",
                {
                    "username": "test_username",
                    "organization": "test_org",
                    "repository": "test_repo",
                    "permission": "admin",
                },
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_500"}}},
                "Error occoured.",
                "Please check that the provided inputs are correct and try again.",
                "500",
            ],
            [
                "invalid_add_collaborator",
                {
                    "username": "test_username",
                    "organization": "test_org",
                    "repository": "test_repo",
                    "permission": "admin",
                },
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error"}}},
                "Error occoured when adding a collaborator.",
                "Please check that the provided inputs are correct and try again.",
                "this is an error",
            ],
        ]
    )
    def test_add_collaborator_invalid(
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
        validate(input_params, AddCollaboratorInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(AddCollaborator(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
