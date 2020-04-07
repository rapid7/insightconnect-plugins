import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.add_file_to_udso_list import AddFileToUdsoList
import json
import logging


class TestAddFileToUdsoList(TestCase):
    def test_integration_add_file_to_udso_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddFileToUdsoList()

        test_conn.logger = log
        test_action.logger = log

        try:
            filename = "../tests/test_add_file_to_udso_list.json"
            with open(filename) as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = "Could not find or read: " + filename
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertEqual({"success": True}, results)

