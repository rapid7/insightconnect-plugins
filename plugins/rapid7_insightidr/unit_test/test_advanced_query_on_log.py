import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightidr.connection.connection import Connection
from icon_rapid7_insightidr.actions.advanced_query_on_log import AdvancedQueryOnLog
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import logging


class TestAdvancedQueryOnLog(TestCase):
    def setup(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AdvancedQueryOnLog()
        test_conn.logger = log
        test_action.logger = log
        try:
            with open("../tests/advanced_query_on_log.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            self.fail("Likely could not find tests in test directory. Generate and fill out samples to fix this.")
        return action_params, connection_params, test_action, test_conn

    def test_integration_advanced_query(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertTrue("results" in results.keys())
        self.assertTrue(len(results.get("results")) > 0)
        self.assertTrue("count" in results.keys())
        self.assertTrue(results.get("count") > 0)

    def test_integration_advanced_query_blank_log(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["query"] = "where(dontfindthisxyzabc)"
        results = test_action.run(action_params)

        self.assertTrue("results" in results.keys())
        self.assertTrue(len(results.get("results")) == 0)
        self.assertTrue("count" in results.keys())
        self.assertTrue(results.get("count") == 0)

    def test_get_log(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        result = test_action.get_log_id("Web Access Log")

        self.assertIsNotNone(result)  # Best we can do here, the log ID will change based on the instance used.

    def test_get_log_fails(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        with self.assertRaises(PluginException):
            test_action.get_log_id("Do not find this log")
