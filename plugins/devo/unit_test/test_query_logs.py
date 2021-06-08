import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_devo.connection.connection import Connection
from icon_devo.actions.query_logs import QueryLogs
import json
import logging


class TestQueryLogs(TestCase):
    def test_integration_query_logs(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = QueryLogs()

        test_conn.logger = log
        test_action.logger = log

        with open("../tests/query_logs.json") as file:
            test_json = json.loads(file.read()).get("body")
            connection_params = test_json.get("connection")
            action_params = test_json.get("input")

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIsNotNone(results)
