import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.get_teams import GetTeams
from icon_microsoft_teams.actions.get_teams.schema import Input, GetTeamsInput, GetTeamsOutput
from jsonschema import validate

from util import Util


class TestGetTeams(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTeams())

    def test_get_teams(self) -> None:
        self.action.connection.client.get_teams.reset_mock()
        self.action.connection.client.get_teams.return_value = [
            {"id": "12345", "displayName": "Example Team", "description": "A test team"}
        ]

        test_input = {Input.TEAM_NAME: "Example"}
        validate(test_input, GetTeamsInput.schema)
        actual = self.action.run(test_input)

        self.action.connection.client.get_teams.assert_called_once_with("Example", explicit=False)
        self.assertEqual(len(actual["teams"]), 1)
        self.assertEqual(actual["teams"][0]["displayName"], "Example Team")
        validate(actual, GetTeamsOutput.schema)

    def test_get_all_teams(self) -> None:
        self.action.connection.client.get_teams.return_value = [
            {"id": "12345", "displayName": "Team A", "description": "First team"},
            {"id": "67890", "displayName": "Team B", "description": "Second team"},
        ]

        test_input = {Input.TEAM_NAME: ""}
        validate(test_input, GetTeamsInput.schema)
        actual = self.action.run(test_input)

        self.assertEqual(len(actual["teams"]), 2)
        validate(actual, GetTeamsOutput.schema)
