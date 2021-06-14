from unittest import TestCase
from icon_microsoft_teams.actions import GetChannelsForTeam
from icon_microsoft_teams.connection import Connection
import logging
import json


class TestGetChannels(TestCase):
    def test_get_channels(self):
        log = logging.getLogger("Test")

        test_action = GetChannelsForTeam()
        test_connection = Connection()

        test_action.logger = log
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)
        test_action.connection = test_connection

        run_params = {"team_name": "Komand-Test-Everyone", "channel_name": "29_test_channel_2"}

        result = test_action.run(run_params)
        self.assertIsNotNone(result)
        self.assertEqual(result.get("channels")[0].get("displayName"), "29_test_channel_2")
