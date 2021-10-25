import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_anomali_threatstream.connection.connection import Connection
from komand_anomali_threatstream.actions.get_observables import GetObservables
import json
import logging


class TestGetObservables(TestCase):
    def test_integration_get_observables(self):

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetObservables()

        test_conn.logger = log
        test_action.logger = log

        with open("../tests/get_observables.json") as file:
            test_json = json.loads(file.read()).get("body")
            connection_params = test_json.get("connection")
            action_params = test_json.get("input")

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIsNotNone(results)
