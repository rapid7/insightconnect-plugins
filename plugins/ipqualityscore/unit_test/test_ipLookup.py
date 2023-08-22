import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_ipqualityscore.connection.connection import Connection
from icon_ipqualityscore.actions.ipLookup import Iplookup
import json
import logging


class TestIplookup(TestCase):
    def test_ipLookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
