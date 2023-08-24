import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_ipqualityscore.connection.connection import Connection
from icon_ipqualityscore.actions.urlLookup import UrlLookup
import json
import logging


class TestUrllookup(TestCase):
    def test_urlLookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
