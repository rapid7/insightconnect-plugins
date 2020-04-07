import sys
import os

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_fortinet_fortigate.connection.connection import Connection
from komand.exceptions import PluginException
import json
import logging



class TestCreateAddressObject(TestCase):


    def test_integration_connection_get_address_group(self):
        log = logging.getLogger("Test")
        test_conn = Connection()

        test_conn.logger = log

        try:
            with open("../tests/create_address_object.json") as file:
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
        result = test_conn.get_address_group("G Suite")

        self.assertIsNotNone(result)
        self.assertEqual(result.get("name"), "G Suite")

    def test_integration_connection_get_address_group(self):
        log = logging.getLogger("Test")
        test_conn = Connection()

        test_conn.logger = log

        try:
            with open("../tests/create_address_object.json") as file:
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
        with self.assertRaises(PluginException):
            test_conn.get_address_group("DONT FIND ME")

