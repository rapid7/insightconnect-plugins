import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from icon_zscaler.actions.delete_user import DeleteUser
from icon_zscaler.util.constants import Assistance, Cause


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteUser())

    @parameterized.expand(
        [
            [
                "existing_user",
                Util.read_file_to_dict("inputs/delete_user.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
        ]
    )
    def test_delete_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/delete_user_not_found.json.inp"),
                Cause.RESOURCE_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_delete_user_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
