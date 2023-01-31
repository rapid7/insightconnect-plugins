import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_bitwarden.actions.updateMembersGroups import UpdateMembersGroups
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateMembersGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateMembersGroups())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/update_members_groups.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ]
        ]
    )
    def test_update_members_groups(self, mock_request, test_name, inputs, expected):
        actual = self.action.run(inputs)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "member_not_found",
                Util.read_file_to_dict("inputs/update_members_groups_bad.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_update_members_groups_bad(self, mock_request, test_name, inputs, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(inputs)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
