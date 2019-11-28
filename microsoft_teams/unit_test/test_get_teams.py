from unittest import TestCase
from icon_microsoft_teams.actions import GetTeams
from icon_microsoft_teams.connection import Connection
import logging
import json


class TestGetTeams(TestCase):
    def test_get_teams(self):
        log = logging.getLogger("Test")

        test_action = GetTeams()
        test_connection = Connection()

        test_action.logger = log
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)
        test_action.connection = test_connection

        run_params = {
            "team_name": "Dream Team"
        }

        result = test_action.run(run_params)
        self.assertIsNotNone(result)
        self.assertEqual(result.get('teams')[0].get('displayName'), 'Dream Team')

    def test_get_teams_with_regex(self):
        log = logging.getLogger("Test")

        test_action = GetTeams()
        test_connection = Connection()

        test_action.logger = log
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)
        test_action.connection = test_connection

        run_params = {
            "team_name": "Team"
        }

        result = test_action.run(run_params)
        self.assertIsNotNone(result)
        self.assertEqual(result.get('teams')[0].get('displayName'), 'Dream Team')
