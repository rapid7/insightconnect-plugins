import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.remove_channel_from_team import RemoveChannelFromTeam
from icon_microsoft_teams.actions.remove_channel_from_team.schema import Input

from util import Util


class TestRemoveChannelFromTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(RemoveChannelFromTeam())
        self.action.connection.client.get_teams.return_value = [{"id": "team-123", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [{"id": "channel-456", "displayName": "Old Channel"}]
        self.action.connection.client.delete_channel.return_value = True

    def test_remove_channel_from_team(self) -> None:
        test_input = {Input.TEAM_NAME: "Example Team", Input.CHANNEL_NAME: "Old Channel"}
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        self.action.connection.client.delete_channel.assert_called_with("team-123", "channel-456")
