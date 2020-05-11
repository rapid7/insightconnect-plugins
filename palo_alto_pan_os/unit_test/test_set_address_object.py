import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_palo_alto_pan_os.connection.connection import Connection
from komand_palo_alto_pan_os.actions.set_address_object import SetAddressObject
import json
import logging


class TestSetAddressObject(TestCase):
    def test_in_whitelist(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1/32"], "ip_netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1/32", ["1.1.1.1/32"], "ip_netmask"))
        self.assertFalse(test_action.match_whitelist("1.1.1.2", ["1.1.1.1/32"], "ip_netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "ip_netmask"))
        self.assertTrue(
            test_action.match_whitelist("www.google.com", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn"))
        self.assertFalse(
            test_action.match_whitelist("aadroid.net", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1"], "ip_range"))
        self.assertFalse(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1"], "ip_range"))


    def test_get_address_type(self):
        test_action = SetAddressObject()
        test_action.logger = logging.getLogger("test")

        self.assertEquals(test_action.determine_address_type("1.1.1.1"), "ip_netmask")
        self.assertEquals(test_action.determine_address_type("1.1.1.1/32"), "ip_netmask")
        self.assertEquals(test_action.determine_address_type("www.google.com"), "fqdn")
        self.assertEquals(test_action.determine_address_type("10.1.1.1-10.1.1.255"), "ip_range")

