import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.actions.get_user_status import GetUserStatus
from komand_duo_admin.util.constants import Assistance, Cause
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
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
    def test_get_user_status(self, mock_request, mock_request_instance, test_name, input_params, expected) -> None:
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
    def test_get_user_status_raise_plugin_exception(
        self, mock_request, mock_request_instance, test_name, input_parameters, cause, assistance
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
