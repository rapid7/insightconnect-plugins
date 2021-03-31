import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_base64.connection.connection import Connection
from komand_base64.actions.decode import Decode
import json
import logging


class TestDecode(TestCase):
    def test_integration_decode(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Decode()

        test_conn.logger = log
        test_action.logger = log

        test_json_file = {
            "body": {
                "action": "decode",
                "input": {
                    "base64": "c29tZSBjb250ZW50",
                    "errors": "nothing"
                },
                "meta": {}
            },
            "type": "action_start",
            "version": "v1"
        }


        test_json = test_json_file.get("body")
        connection_params = test_json.get("connection")
        action_params = test_json.get("input")

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        expected = {'data': 'some content'}
        self.assertEqual(expected, results)
