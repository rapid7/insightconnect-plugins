import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_sentinelone.connection.connection import Connection
from komand_sentinelone.actions.agents_action import AgentsAction
import json
import logging
from insightconnect_plugin_runtime.exceptions import PluginException


class TestAgentsAction(TestCase):
    def setup(self) -> None:
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AgentsAction()
        test_conn.logger = log
        test_action.logger = log
        try:
            with open("../tests/agents_action.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            self.fail("Likely could not find tests in test directory. Generate and fill out samples to fix this.")
        return action_params, connection_params, test_action, test_conn, log

    def test_agents_action_abort_scan(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "abort-scan"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

    def test_all_agents_action_connect(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "connect"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

    def test_all_agents_action_decommission(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "decommission"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

        action_params["filter"] = {}
        self.assertRaises(PluginException, test_action.run, action_params)

    def test_all_agents_action_disconnect(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "disconnect"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

        action_params["filter"] = {}
        self.assertRaises(PluginException, test_action.run, action_params)

    def test_all_agents_action_fetch_logs(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "fetch-logs"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

    def test_all_agents_action_initiate_scan(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "initiate-scan"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

    def test_all_agents_action_restart_machine(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "restart-machine"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

        action_params["filter"] = {}
        self.assertRaises(PluginException, test_action.run, action_params)

    def test_all_agents_action_shutdown(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "shutdown"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

        action_params["filter"] = {}
        self.assertRaises(PluginException, test_action.run, action_params)

    def test_all_agents_action_uninstall(self):
        action_params, connection_params, test_action, test_conn, log = self.setup()
        test_conn.connect(connection_params)
        test_action.connection = test_conn
        action_params["action"] = "uninstall"

        results = test_action.run(action_params)
        self.assertTrue("affected" in results.keys())

        action_params["filter"] = {}
        self.assertRaises(PluginException, test_action.run, action_params)
