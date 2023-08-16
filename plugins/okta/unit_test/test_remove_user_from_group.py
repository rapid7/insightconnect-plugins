import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.remove_user_from_group import RemoveUserFromGroup
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestRemoveUserFromGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RemoveUserFromGroup())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/remove_user_from_group.json.inp"),
                Util.read_file_to_dict("expected/remove_user_from_group.json.exp"),
            ]
        ]
    )
    def test_remove_user_from_group(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_user",
                Util.read_file_to_dict("inputs/remove_user_from_group_invalid_user.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_group",
                Util.read_file_to_dict("inputs/remove_user_from_group_invalid_group.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_remove_user_from_group_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
