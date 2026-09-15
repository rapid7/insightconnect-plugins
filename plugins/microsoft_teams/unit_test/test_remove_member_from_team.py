import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.remove_member_from_team import RemoveMemberFromTeam
from icon_microsoft_teams.actions.remove_member_from_team.schema import Input

from util import Util


class TestRemoveMemberFromTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(RemoveMemberFromTeam())
        self.action.connection.client.get_user_info.return_value = {"id": "user-123", "displayName": "Test User"}
        self.action.connection.client.get_teams.return_value = [{"id": "group-456", "displayName": "Example Team"}]
        self.action.connection.client.remove_member_from_group.return_value = True

    def test_remove_member_from_team(self) -> None:
        test_input = {Input.TEAM_NAME: "Example Team", Input.MEMBER_LOGIN: "user@example.com"}
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        self.action.connection.client.get_user_info.assert_called_with("user@example.com")
        self.action.connection.client.remove_member_from_group.assert_called_with("group-456", "user-123")
