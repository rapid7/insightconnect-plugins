import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_palo_alto_pan_os.connection.connection import Connection
from komand_palo_alto_pan_os.actions.get_policy import GetPolicy
import json
import logging


class TestGetPolicy(TestCase):
    def test_integration_get_policy(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetPolicy()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_policy.json") as file:
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

        keys = ['to', 'from', 'source', 'destination', 'source_user', 'category', 'application', 'service', 'hip_profiles', 'action']

        self.assertEquals(list(results.keys()), keys)

    def test_get_policy(self):
        """
        TODO: Implement test cases here

        Here you can mock the connection with data returned from the above integration test.
        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing

        You can either create a formal Mock for this, or you can create a fake connection class to pass to your
        action for testing.
        """
        self.fail("Unimplemented Test Case")
