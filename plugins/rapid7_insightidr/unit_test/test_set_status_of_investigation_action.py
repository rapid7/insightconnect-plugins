import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightidr.connection.connection import Connection
from icon_rapid7_insightidr.actions.set_status_of_investigation_action import SetStatusOfInvestigationAction
import json
import logging


class TestSetStatusOfInvestigationAction(TestCase):
    def test_integration_set_status_of_investigation_action(self):
        """
        TODO: Implement assertions at the end of this test case

        This is an integration test that will connect to the services your plugin uses. It should be used
        as the basis for tests below that can run independent of a "live" connection.

        This test assumes a normal plugin structure with a /tests directory. In that /tests directory should
        be json samples that contain all the data needed to run this test. To generate samples run:

        icon-plugin generate samples

        """

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = SetStatusOfInvestigationAction()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/set_status_of_investigation_action.json") as file:
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

        # TODO: Remove this line
        self.fail("Unimplemented test case")

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        self.assertEquals({}, results)

    def test_set_status_of_investigation_action(self):
        """
        TODO: Implement test cases here

        Here you can mock the connection with data returned from the above integration test.
        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing

        You can either create a formal Mock for this, or you can create a fake connection class to pass to your
        action for testing.
        """
        self.fail("Unimplemented Test Case")
