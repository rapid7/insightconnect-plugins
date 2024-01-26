import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_github.actions.add_membership.action import AddMembership
from komand_github.actions.add_membership.schema import AddMembershipInput, AddMembershipOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
@patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
@patch("requests.put", side_effect=Util.mock_put_request)
class TestAddMembership(TestCase):
    @classmethod
    @patch("komand_github.connection.connection.github.Auth.Token", side_effect=Util.mock_github_auth_token)
    @patch("komand_github.connection.connection.github.Github", side_effect=Util.mock_github)
    def setUpClass(cls, _mock_github: MagicMock, _mock_github_auth_token: MagicMock) -> None:
        cls.action = Util.default_connector(AddMembership())

    @parameterized.expand(
        [
            [
                "valid_add_membership",
                {"role": "admin", "username": "test_username", "organization": "test_org"},
                Util.read_file_to_dict("expected/add_membership_valid.json.exp"),
            ],
        ]
    )
    def test_add_membership_valid(
        self,
        _mock_request: MagicMock,
        _mock_github: MagicMock,
        _mock_github_auth_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, AddMembershipInput.schema)
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)
        validate(actual, AddMembershipOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_add_membership_403",
                {"role": "admin", "username": "test_username", "organization": "test_org"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_403"}}},
                "Forbidden response returned from Github",
                "Account may need org permissions added",
                "",
            ],
            [
                "invalid_add_membership_500",
                {"role": "admin", "username": "test_username", "organization": "test_org"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error_500"}}},
                "A status code of 500 was returned from Github",
                "Please check that the provided inputs are correct and try again.",
                "",
            ],
            [
                "invalid_add_membership",
                {"role": "admin", "username": "test_username", "organization": "test_org"},
                {"credentials": {"username": "usename", "personal_token": {"secretKey": "error"}}},
                "An error has occurred while adding a membership",
                "Please check that the provided inputs are correct and try again.",
                "this is an error",
            ],
        ]
    )
    def test_add_membership_invalid(
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
        validate(input_params, AddMembershipInput.schema)
        with self.assertRaises(PluginException) as error:
            Util.default_connector(AddMembership(), input_connection).run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
