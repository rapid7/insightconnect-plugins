import sys
import os

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insight_agent.connection.connection import Connection
from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
import json
import logging


class TestConnection(TestCase):
    def test_integration_connection_test(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetAgentDetails()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_agent_details.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory

            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        connection_params["api_key"] = {"secretKey": None}
        test_conn.connect(connection_params)

        try:
            test_conn.test()
        except:
            self.fail("Exception was thrown")



