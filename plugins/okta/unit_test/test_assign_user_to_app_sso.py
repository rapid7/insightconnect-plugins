import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.assign_user_to_app_sso import AssignUserToAppSso
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestAssignUserToAppSso(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AssignUserToAppSso())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/assign_user_to_app_sso.json.inp"),
                Util.read_file_to_dict("expected/assign_user_to_app_sso.json.exp"),
            ]
        ]
    )
    def test_assign_user_to_app_sso(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "app_not_found",
                Util.read_file_to_dict("inputs/assign_user_to_app_sso_invalid_app_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/assign_user_to_app_sso_invalid_user_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_assign_user_to_app_sso_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
