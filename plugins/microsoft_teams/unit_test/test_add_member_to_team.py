import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.add_member_to_team import AddMemberToTeam
from icon_microsoft_teams.actions.add_member_to_team.schema import Input

from util import Util


class TestAddMemberToTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddMemberToTeam())
        self.action.connection.client.get_user_info.return_value = {"id": "user-123", "displayName": "Test User"}
        self.action.connection.client.get_teams.return_value = [{"id": "group-456", "displayName": "Example Team"}]
        self.action.connection.client.add_member_to_group.return_value = True

    def test_add_member_to_team(self) -> None:
        test_input = {Input.TEAM_NAME: "Example Team", Input.MEMBER_LOGIN: "user@example.com"}
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        self.action.connection.client.get_user_info.assert_called_with("user@example.com")
        self.action.connection.client.get_teams.assert_called_with("Example Team")
        self.action.connection.client.add_member_to_group.assert_called_with("group-456", "user-123")
