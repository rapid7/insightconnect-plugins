from unittest import TestCase
from icon_microsoft_teams.connection.connection import Connection
from icon_microsoft_teams.util.teams_utils import create_channel, delete_channel, get_channels_from_microsoft

import logging
import json
import time

# Globals
TEAM_ID = "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd"  # Komand-Test-Everyone
TEST_CHANNEL_NAME = "test_channel_delete_me_2"


class TestTeamsUtils(TestCase):
    def test_create_channel(self):
        log = logging.getLogger("Test")
        test_connection = Connection()
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)

        result = create_channel(log, test_connection, TEAM_ID, TEST_CHANNEL_NAME, "some really cool test description")

        # This code is used to bulk create channels. Needed to max out a team with channels to test
        # pagination

        # for i in range(200):
        #     channel_name = f"{i}_test_channel"
        #     create_channel(log, test_connection, TEAM_ID, channel_name, "some really cool test description")

        self.assertTrue(result)

    def test_delete_channel(self):
        log = logging.getLogger("Test")
        test_connection = Connection()
        test_connection.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_connection.connect(connection_params)

        channels = get_channels_from_microsoft(log, test_connection, TEAM_ID, TEST_CHANNEL_NAME, True)
        channel_id = channels[0].get("id")

        result = delete_channel(log, test_connection, TEAM_ID, channel_id)

        # Leaving this code here - This can be used for bulk delete if needed

        # for i in range(100):
        #     channel_name = f"{i}_test_channel_3"
        #     channels = get_channels_from_microsoft(log, test_connection, TEAM_ID, channel_name)
        #     channel_id = channels[0].get("id")
        #     delete_channel(log, test_connection, TEAM_ID, channel_id)
        #     time.sleep(1)

        self.assertTrue(result)
