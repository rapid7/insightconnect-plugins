import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from unittest.mock import patch
from icon_azure_ad_admin.connection.connection import Connection
from icon_azure_ad_admin.triggers.risk_detection import RiskDetection
import logging
import json
import timeout_decorator


# This will catch timeout errors and return None. This tells the test framework our test passed.
# This is needed because the run function in a trigger is an endless loop.
def timeout_pass(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except timeout_decorator.timeout_decorator.TimeoutError as e:
            print(f"Test timed out as expected: {e}")
            return None

    return func_wrapper

# This mocks komand.Trigger.send
# We need this to fake out the plugin into thinking it's sending output in the trigger's run function
class fakeSender():
    def send(params):
        print(params)

# Test class
class TestRiskDetection(TestCase):

    @timeout_pass
    @timeout_decorator.timeout(30)
    @patch("komand.Trigger.send", side_effect=fakeSender.send)
    def test_integration_risk_detection(self, mockSend):
        """
        TODO: Manually validate results

        Because the send function is essentially an endless loop, there's no way to validate the output from
        that in an elegant way. Really this test is just making sure no exceptions are thrown.

        The bulk of your logic for your trigger should not be in the run loop and should be tested with subsequent
        tests.
        """
        log = logging.getLogger("Test")

        try:
            with open("../tests/risk_detection.json") as f:
                data = json.load(f)
                connection_params = data.get("body").get("connection")
                trigger_params = data.get("body").get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_connection = Connection()
        test_connection.logger = log
        test_connection.connect(connection_params)

        test_email_received = RiskDetection()
        test_email_received.connection = test_connection
        test_email_received.logger = log

        test_email_received.run(trigger_params)

        self.fail() # If we made it this far, the run loop failed somehow

    def test_risk_detection_some_function_to_test(self):
        """
        TODO: Test your trigger logic

        Here and in following tests you should test everything you can in your trigger that's not in the run loop.
        """
        self.fail("Unimplemented Test")