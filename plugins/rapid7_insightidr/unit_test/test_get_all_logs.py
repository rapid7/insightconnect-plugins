import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightidr.connection.connection import Connection
from icon_rapid7_insightidr.actions.get_all_logs import GetAllLogs
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import logging


class TestGetAllLogs(TestCase):
    def setup(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetAllLogs()
        test_conn.logger = log
        test_action.logger = log
        try:
            with open("../tests/get_all_logs.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            self.fail("Likely could not find tests in test directory. Generate and fill out samples to fix this.")
        return action_params, connection_params, test_action, test_conn

    def test_integration_advanced_query_log_set(self):
        action_params, connection_params, test_action, test_conn = self.setup()

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIsNotNone(results)
