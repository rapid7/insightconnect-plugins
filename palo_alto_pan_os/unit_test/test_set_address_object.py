import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_palo_alto_pan_os.connection.connection import Connection
from komand_palo_alto_pan_os.actions.set_address_object import SetAddressObject
import json
import logging


class TestSetAddressObject(TestCase):


    def test_integration_set_address_object(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = SetAddressObject()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/set_address_object.json") as file:
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

        self.assertIsNotNone(results)
        self.assertEquals({'code': '20', 'message': 'command succeeded', 'status': 'success'}, results)



    def test_in_whitelist(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1/32"], "ip-netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1/32", ["1.1.1.1/32"], "ip-netmask"))
        self.assertFalse(test_action.match_whitelist("1.1.1.2", ["1.1.1.1/32"], "ip-netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "ip-netmask"))
        self.assertTrue(
            test_action.match_whitelist("www.google.com", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn"))
        self.assertFalse(
            test_action.match_whitelist("aadroid.net", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1"], "ip-range"))
        self.assertFalse(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1"], "ip-range"))

    def test_cidr_vs_cidr_in_whitelis(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertTrue(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1","1.1.1.1/24"], "ip-netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1/24"], "ip-netmask"))
        self.assertFalse(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1", "1.1.1.1/32"], "ip-netmask"))

    def test_get_address_type(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertEquals(test_action.determine_address_type("1.1.1.1"), "ip-netmask")
        self.assertEquals(test_action.determine_address_type("1.1.1.1/32"), "ip-netmask")
        self.assertEquals(test_action.determine_address_type("www.google.com"), "fqdn")
        self.assertEquals(test_action.determine_address_type("10.1.1.1-10.1.1.255"), "ip-range")

    def test_check_if_private(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertTrue(test_action.check_if_private("192.168.1.1"))
        self.assertTrue(test_action.check_if_private("192.168.1.1/32"))
        self.assertTrue(test_action.check_if_private("FE80::903A:1C1A:E802:11E4"))
        self.assertFalse(test_action.check_if_private("www.google.com"))
        self.assertFalse(test_action.check_if_private("1.1.1.1"))
        self.assertFalse(test_action.check_if_private("192.168.1.1-192.168.1.100"))

