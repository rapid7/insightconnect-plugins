import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_user_status import GetUserStatus
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestGetUserStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserStatus())

    @parameterized.expand(
        [
            [
                "user_found",
                Util.read_file_to_dict("inputs/get_user_status.json.inp"),
                Util.read_file_to_dict("expected/get_user_status.json.exp"),
            ],
        ]
    )
    def test_get_user_status(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/get_user_status_invalid_username.json.inp"),
                Cause.USER_NOT_FOUND,
                Assistance.USER_NOT_FOUND,
            ]
        ]
    )
    def test_get_user_status_raise_plugin_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
