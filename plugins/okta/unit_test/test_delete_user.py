import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.delete_user import DeleteUser
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteUser())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/delete_user_success.json.inp"),
                Util.read_file_to_dict("expected/delete_user_success.json.exp"),
            ],
        ]
    )
    def test_delete_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/delete_user_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_delete_user_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
