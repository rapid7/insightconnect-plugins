import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_bitwarden.actions.retrieveMembersGroupIds import RetrieveMembersGroupIds
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestRetrieveMembersGroupIds(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RetrieveMembersGroupIds())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/retrieve_members_group_ids.json.inp"),
                Util.read_file_to_dict("expected/retrieve_members_group_ids.json.exp"),
            ]
        ]
    )
    def test_retrieve_members_group_ids(self, mock_request, test_name, inputs, expected):
        actual = self.action.run(inputs)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "member_not_found",
                Util.read_file_to_dict("inputs/retrieve_members_group_ids_bad.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_retrieve_members_group_ids_bad(self, mock_request, test_name, inputs, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(inputs)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
