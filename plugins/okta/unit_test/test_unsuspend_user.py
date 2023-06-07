import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.unsuspend_user import UnsuspendUser
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestUnsuspendUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UnsuspendUser())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/unsuspend_user_success.json.inp"),
                Util.read_file_to_dict("expected/unsuspend_user_success.json.exp"),
            ],
        ]
    )
    def test_unsuspend_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/unsuspend_user_not_found.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "user_already_unsuspended",
                Util.read_file_to_dict("inputs/unsuspend_user_already_unsuspended.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_unsuspend_user_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
