import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.get_vulnerabilities_by_cve import GetVulnerabilitiesByCve
import json
import logging


class TestGetVulnerabilitiesByCve(TestCase):
    def test_get_vulnerabilities_by_cve(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
