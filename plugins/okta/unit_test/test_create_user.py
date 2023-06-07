import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.create_user import CreateUser
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


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
    def test_create_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
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
    def test_create_user_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
