import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_aws_securityhub.connection.connection import Connection
from icon_aws_securityhub.actions.get_findings import GetFindings
import json
import logging


class TestGetFindings(TestCase):
    def test_get_findings(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
