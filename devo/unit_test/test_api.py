import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_devo.connection.connection import Connection
import json
import logging


class TestQueryLogs(TestCase):
    def test_integration_query_logs(self):
        try:
            with open("../tests/query_logs.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
        except Exception as e:
            self.fail()

        test_connection = Connection()
        test_connection.logger = logging.getLogger("Test")
        test_connection.connect(connection_params)
        test_api = test_connection.api

        test_api.test_connection()

