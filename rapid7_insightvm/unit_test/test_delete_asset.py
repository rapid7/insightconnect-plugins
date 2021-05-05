import sys
import os
from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.delete_asset import DeleteAsset
import json
import logging

sys.path.append(os.path.abspath("../"))


class TestDeleteAsset(TestCase):
    def test_integration_delete_asset(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DeleteAsset()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/delete_asset.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception:
            message = """
            Could not find or read sample tests from /tests directory
            An exception here likely means you didn't fill out your samples correctly in the /tests directory
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        self.assertEquals({}, results)
