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

        test_conn.logger = log

        try:
            filename = "files/connection.json"
            with open(filename) as file:
                test_json = json.loads(file.read())
                connection_params = test_json.get("connection")
        except Exception as e:
            message = f"Exception opening {filename}. Exception is:\n{e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_results = None
        try:
            test_results = test_conn.test()
        except Exception as err:
            log.error(f"Exception connecting to Apex: {err}")

        self.assertEqual({"success": True}, test_results)

