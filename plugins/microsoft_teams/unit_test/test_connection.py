from unittest import TestCase
from icon_microsoft_teams.connection import Connection
import json
import logging


class TestConnection(TestCase):
    def test_connection(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_conn.logger = log

        with open("../tests/send_message.json") as file:
            data = json.load(file)
            connection_params = data.get("body").get("connection")

        test_conn.connect(connection_params)

        self.assertIsNotNone(test_conn.api_token)
