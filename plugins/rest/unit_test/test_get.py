import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unit_test.mockconnection import MockConnection
from komand_rest.actions.get import Get


class TestGet(TestCase):
    def test_integration_get(self):
        """
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Get()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message =
            Could not find or read sample tests from /tests directory

            An exception here likely means you didn't fill out your samples correctly in the /tests directory
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory

            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIsNotNone(results)
        """

    def test_get_unit(self):
        test_conn = MockConnection()
        test_action = Get()

        test_action.connection = test_conn
        action_params = {"route": "https://www.google.com", "headers": {}}
        results = test_action.run(action_params)

        # only new things to test is that it correctly routes output of results
        self.assertEqual(results["status"], 200)
        # more tests?
        self.assertEqual(results["body_object"], {"SampleSuccessBody": "SampleVal"})
        self.assertEqual(results["body_string"], "SAMPLETEXT for method GET")
        self.assertEqual(results["headers"], {"SampleHeader": "SampleVal"})
