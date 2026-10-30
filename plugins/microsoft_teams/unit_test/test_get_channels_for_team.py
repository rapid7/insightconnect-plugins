import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.get_channels_for_team import GetChannelsForTeam
from icon_microsoft_teams.actions.get_channels_for_team.schema import Input

from util import Util


class TestGetChannelsForTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetChannelsForTeam())
        self.action.connection.client.get_teams.return_value = [{"id": "team-123", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [
            {"id": "channel-1", "displayName": "General", "description": "Default channel"},
            {"id": "channel-2", "displayName": "Alerts", "description": "Alert channel"},
        ]

    def test_get_channels_for_team(self) -> None:
        test_input = {Input.TEAM_NAME: "Example Team"}
        response = self.action.run(test_input)
        self.assertEqual(len(response["channels"]), 2)
        self.assertEqual(response["channels"][0]["displayName"], "General")
        self.action.connection.client.get_teams.assert_called_with("Example Team")
        self.action.connection.client.get_channels.assert_called_with("team-123", None)
