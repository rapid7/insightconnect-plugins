import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_whois.actions.address import Address
import logging


class TestAddress(TestCase):
    def test_address(self):
        log = logging.getLogger("Test")
        test_action = Address()
        test_action.logger = log

        working_params = {"address": "142.250.80.100", "registrar": "Autodetect"}
        results = test_action.run(working_params)
        expected = {
            "netrange": "142.250.0.0 - 142.251.255.255",
            "cidr": "142.250.0.0/15",
            "netname": "GOOGLE",
            "nettype": "Direct Allocation",
            "organization": "Google LLC (GOGL)",
            "regdate": "2000-03-30",
            "update": "2019-10-31",
            "orgname": "Google LLC",
            "address": "1600 Amphitheatre Parkway",
            "city": "Mountain View",
            "state": "CA",
            "postal": "94043",
            "country": "US",
            "org_tech_phone": "+1-650-253-0000",
            "org_tech_email": "arin-contact@google.com",
            "org_abuse_phone": "+1-650-253-0000",
            "org_abuse_email": "network-abuse@google.com",
        }
        self.assertNotEqual({}, results, "returns non - empty results")
        self.assertEqual(expected, results)
