import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insight_agent.connection.connection import Connection
from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
import json
import logging


class TestGetAgentDetails(TestCase):
    def test_integration_get_agent_details(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetAgentDetails()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_agent_details.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)


        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertTrue("agent" in results.keys())
        self.assertTrue(len(results), 1)
        self.assertEqual(results.get("agent").get("id"), "15eec979a15f75ad70567d58ad8a0aef")
