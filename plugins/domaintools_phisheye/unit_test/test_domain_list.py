import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_domaintools_phisheye.connection.connection import Connection
from icon_domaintools_phisheye.actions.domain_list import DomainList
import json
from unit_test.mock import Util


class TestDomainList(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DomainList())

    def test_domain_list(self):
        response = self.action.run()
        expected_response = {
            "date": "2016-11-01",
            "domains": [
                {
                    "Created Date": {},
                    "Domain": "appeltypoexample.com",
                    "IP Addresses": [{"Country Code": {}, "IPv4": {}}],
                    "Name Servers": "ns57.domaincontrol.com",
                    "Registrant Email": {},
                    "Registrar Name": {},
                    "Risk Score": 24,
                    "TLD": {},
                }
            ],
            "term": "apple",
        }
        self.assertEqual(response, expected_response)
