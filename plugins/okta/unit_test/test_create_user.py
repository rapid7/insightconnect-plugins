import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_okta.actions.create_user import CreateUser
from komand_okta.connection.schema import Input as ConnectionInput
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateUser())

    @parameterized.expand(
        [
            [
                "user_with_password",
                Util.read_file_to_dict("inputs/create_user_with_password.json.inp"),
                Util.read_file_to_dict("expected/create_user_with_password.json.exp"),
            ],
            [
                "user_with_provider",
                Util.read_file_to_dict("inputs/create_user_with_provider.json.inp"),
                Util.read_file_to_dict("expected/create_user_with_provider.json.exp"),
            ],
            [
                "user_with_groups",
                Util.read_file_to_dict("inputs/create_user_with_groups.json.inp"),
                Util.read_file_to_dict("expected/create_user_with_provider.json.exp"),
            ],
        ]
    )
    def test_create_user(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "bad_profile",
                Util.read_file_to_dict("inputs/create_user_profile_bad.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_create_user_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "bad_domain",
                Util.read_file_to_dict("inputs/create_user_profile_bad.json.inp"),
                "Invalid domain entered for input 'Okta Domain'.",
                "Please include a valid subdomain, e.g. 'example.okta.com', if using 'okta.com'.",
                "Provided Okta Domain: okta.com",
            ],
        ]
    )
    def test_create_user_raise_domain_exception(
        self,
        mock_request: MagicMock,
        test_name: str,
        input_parameters: Dict[str, Any],
        cause: str,
        assistance: str,
        data: Dict[str, Any],
    ) -> None:
        with self.assertRaises(PluginException) as error:
            action = Util.default_connector(CreateUser(), {ConnectionInput.OKTAURL: "okta.com"})
            action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
