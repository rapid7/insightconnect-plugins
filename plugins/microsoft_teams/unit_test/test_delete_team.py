import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.delete_team import DeleteTeam
from icon_microsoft_teams.actions.delete_team.schema import Input

from util import Util


class TestDeleteTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteTeam())
        self.action.connection.client.get_group_id_from_name.return_value = "group-123"
        self.action.connection.client.delete_group.return_value = True

    def test_delete_team(self) -> None:
        test_input = {Input.TEAM_NAME: "Test Team"}
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        self.action.connection.client.get_group_id_from_name.assert_called_with("Test Team")
        self.action.connection.client.delete_group.assert_called_with("group-123")
