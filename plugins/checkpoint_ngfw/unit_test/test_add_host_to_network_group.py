import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_checkpoint_ngfw.connection.connection import Connection
from icon_checkpoint_ngfw.actions.add_host_to_network_group import AddHostToNetworkGroup
import json
import logging


class TestAddHostToNetworkGroup(TestCase):
    def test_integration_add_host_to_network_group(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddHostToNetworkGroup()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/add_host_to_network_group.json") as file:
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

        self.assertEquals({"success": True}, results)
