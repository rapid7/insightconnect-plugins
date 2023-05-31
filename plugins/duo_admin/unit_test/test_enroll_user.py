import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.enroll_user.action import EnrollUser
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestEnrollUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(EnrollUser())

    @parameterized.expand(
        [
            [
                "existing_not_enrolled_user",
                Util.read_file_to_dict("inputs/enroll_user_existing_user.json.inp"),
                Util.read_file_to_dict("expected/enroll_user_success.json.exp"),
            ],
            [
                "non_existing_user",
                Util.read_file_to_dict("inputs/enroll_user_non_existing_user.json.inp"),
                Util.read_file_to_dict("expected/enroll_user_success.json.exp"),
            ],
        ]
    )
    def test_enroll_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_already_enrolled",
                Util.read_file_to_dict("inputs/enroll_user_already_enrolled.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_enroll_user_raise_api_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
