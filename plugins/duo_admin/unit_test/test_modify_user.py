import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.modify_user import ModifyUser
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Assistance, Cause


@patch("requests.request", side_effect=Util.mock_request)
class TestModifyUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ModifyUser())

    @parameterized.expand(
        [
            [
                "modify_user",
                Util.read_file_to_dict("inputs/modify_user.json.inp"),
                Util.read_file_to_dict("expected/modify_user.json.exp"),
            ],
        ]
    )
    def test_modify_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_id_not_found",
                Util.read_file_to_dict("inputs/modify_user_not_found.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "username_exist",
                Util.read_file_to_dict("inputs/modify_user_bad_username.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
            [
                "alias_exist",
                Util.read_file_to_dict("inputs/modify_user_bad_alias.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_modify_user_api_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
