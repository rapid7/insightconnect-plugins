import sys
import os
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.util import Util
from icon_bitwarden.actions.retrieveMember import RetrieveMember

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mock_request)
class TestRetrieveMember(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RetrieveMember())

    @parameterized.expand(
        [
            [
                "existing_member_without_collections",
                Util.read_file_to_dict("inputs/member_id_valid.json.inp"),
                Util.read_file_to_dict("expected/retrieve_member.json.exp"),
            ],
            [
                "existing_member_with_collections",
                Util.read_file_to_dict("inputs/member_id_with_collections.json.inp"),
                Util.read_file_to_dict("expected/retrieve_member_with_collections.json.exp"),
            ],
        ]
    )
    def test_retrieve_member(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "member_not_found",
                Util.read_file_to_dict("inputs/member_id_not_found.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_member_id",
                Util.read_file_to_dict("inputs/member_id_bad.json.inp"),
                "Invalid details provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_retrieve_member_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
