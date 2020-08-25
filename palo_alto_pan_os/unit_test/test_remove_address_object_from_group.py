import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_palo_alto_pan_os.connection.connection import Connection
from komand_palo_alto_pan_os.actions.remove_address_object_from_group import RemoveAddressObjectFromGroup
import json
import logging


class TestRemoveAddressObjectFromGroup(TestCase):
    def test_integration_remove_address_object_from_group(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = RemoveAddressObjectFromGroup()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/remove_address_object_from_group.json") as file:
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

        # For example: self.assertEquals({"success": True}, results)
        self.assertEquals({"success": True}, results)
