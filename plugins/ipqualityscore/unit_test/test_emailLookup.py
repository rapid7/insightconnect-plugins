import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_ipqualityscore.connection.connection import Connection
from icon_ipqualityscore.actions.emailLookup import EmailLookup
import json
import logging


class TestEmaillookup(TestCase):
    def test_emailLookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
