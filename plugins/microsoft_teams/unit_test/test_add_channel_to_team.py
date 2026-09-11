import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.add_channel_to_team.action import AddChannelToTeam
from icon_microsoft_teams.actions.add_channel_to_team.schema import AddChannelToTeamInput, AddChannelToTeamOutput, Input
from jsonschema import validate
from parameterized import parameterized

from util import Util


class TestAddChannelToTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddChannelToTeam())
        self.action.connection.client.get_teams.return_value = [{"id": "12345", "displayName": "Example Team"}]
        self.action.connection.client.create_channel.return_value = True

    @parameterized.expand([("Standard",), ("Private",)])
    def test_add_channel_to_team(self, channel_type: str) -> None:
        test_input = {
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "ExampleName",
            Input.CHANNEL_DESCRIPTION: "Example Channel Description",
            Input.CHANNEL_TYPE: channel_type,
        }
        validate(test_input, AddChannelToTeamInput.schema)
        response = self.action.run(test_input)
        self.assertEqual(response, {"success": True})
        validate(response, AddChannelToTeamOutput.schema)
        self.action.connection.client.create_channel.assert_called_with(
            "12345", "ExampleName", "Example Channel Description", channel_type
        )
