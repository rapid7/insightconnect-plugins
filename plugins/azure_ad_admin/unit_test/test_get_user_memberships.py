import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_ad_admin.actions.get_user_memberships import GetUserMemberships
from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetUserMemberships(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(GetUserMemberships())

    def test_get_user_memberships(self, mock_request: MagicMock) -> None:
        actual = self.action.run({"user_id": "user@example.com"})
        expected = Util.read_file_to_dict("expected/get_user_memberships.json.exp")
        self.assertEqual(actual, expected)

    def test_get_user_memberships_with_next_link(self, mock_request: MagicMock) -> None:
        actual = self.action.run(
            {
                "user_id": "user@example.com",
                "next_link": "https://graph.microsoft.com/v1.0/azure_tenant/users/user@example.com/memberOf?$skiptoken=page2",
            }
        )
        self.assertEqual(actual["count"], 1)
        self.assertEqual(actual["memberships"][0]["displayName"], "Another Group")
        self.assertNotIn("next_link", actual)

    def test_get_user_memberships_invalid_user(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({"user_id": "invalid-user"})
        self.assertEqual(error.exception.cause, "Resource not found.")
        self.assertEqual(error.exception.assistance, "Please provide valid inputs and try again.")
