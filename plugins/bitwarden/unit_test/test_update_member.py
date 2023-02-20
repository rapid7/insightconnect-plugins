import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_bitwarden.actions.updateMember import UpdateMember

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateMember(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateMember())

    @parameterized.expand(
        [
            [
                "member_data_1",
                Util.read_file_to_dict("inputs/update_member.json.inp"),
                Util.read_file_to_dict("expected/update_member.json.exp"),
            ],
            [
                "member_data_2",
                Util.read_file_to_dict("inputs/update_member_no_collections.json.inp"),
                Util.read_file_to_dict("expected/update_member_no_collections.json.exp"),
            ],
        ]
    )
    def test_update_member(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "member_not_found",
                Util.read_file_to_dict("inputs/update_member_not_found.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_collections",
                Util.read_file_to_dict("inputs/update_member_bad.json.inp"),
                "Invalid details provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_update_member_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
