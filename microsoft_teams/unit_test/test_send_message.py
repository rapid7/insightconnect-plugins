from unittest import TestCase
from icon_microsoft_teams.actions import SendMessage
from icon_microsoft_teams.connection import Connection
import logging
import json


class TestGetTeams(TestCase):
    def test_get_teams(self):
        log = logging.getLogger("Test")

        test_action = SendMessage()
        test_connection = Connection()

        test_action.logger = log
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)
        test_action.connection = test_connection

        run_params = {
            "team_name": "Dream Team",
            "channel_name": "test123",
            "message": "Hello from a Unit Test!"
        }

        result = test_action.run(run_params)
        self.assertIsNotNone(result)
