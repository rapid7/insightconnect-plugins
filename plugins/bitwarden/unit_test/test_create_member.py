import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_bitwarden.actions.createMember import CreateMember

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateMember(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateMember())

    @parameterized.expand(
        [
            [
                "valid_member_data",
                Util.read_file_to_dict("inputs/create_member.json.inp"),
                Util.read_file_to_dict("expected/create_member.json.exp"),
            ],
            [
                "member_with_collections",
                Util.read_file_to_dict("inputs/create_member_with_collections.json.inp"),
                Util.read_file_to_dict("expected/create_member_with_collections.json.exp"),
            ],
        ]
    )
    def test_create_member(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_collections",
                Util.read_file_to_dict("inputs/create_member_bad.json.inp"),
                "Invalid details provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_create_member_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
