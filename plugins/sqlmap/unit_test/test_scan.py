import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_sqlmap.connection.connection import Connection
from icon_sqlmap.actions.scan import Scan
import json
import logging


class TestScan(TestCase):
    def test_scan(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
