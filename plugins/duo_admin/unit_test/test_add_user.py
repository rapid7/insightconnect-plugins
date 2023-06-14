import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.add_user.action import AddUser
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestAddUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddUser())

    @parameterized.expand(
        [
            [
                "success_1",
                Util.read_file_to_dict("inputs/add_user_success_1.json.inp"),
                Util.read_file_to_dict("expected/add_user_success_1.json.exp"),
            ],
            [
                "success_2",
                Util.read_file_to_dict("inputs/add_user_success_2.json.inp"),
                Util.read_file_to_dict("expected/add_user_success_2.json.exp"),
            ],
        ]
    )
    def test_add_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "duplicated_username",
                Util.read_file_to_dict("inputs/add_user_duplicated_username.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
            [
                "duplicated_alias",
                Util.read_file_to_dict("inputs/add_user_duplicated_alias.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_add_user_raise_api_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "aliases_number_exceeded",
                Util.read_file_to_dict("inputs/add_user_aliases_number_excedeed.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.ALIASES_NUMBER_EXCEEDED,
            ]
        ]
    )
    def test_add_user_raise_plugin_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
