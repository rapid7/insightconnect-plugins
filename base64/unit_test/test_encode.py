import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_base64.connection.connection import Connection
from komand_base64.actions.encode import Encode
import json
import logging


class TestEncode(TestCase):
    def test_integration_encode(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = Encode()

        test_conn.logger = log
        test_action.logger = log

        test_json_file = {
            "body": {
                "action": "encode",
                "input": {
                    "content": "some content"
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

        # TODO: Remove this line
        self.fail("Unimplemented test case")

        # TODO: The following assert should be updated to look for data from your action
        # For example: self.assertEquals({"success": True}, results)
        self.assertEqual({}, results)
