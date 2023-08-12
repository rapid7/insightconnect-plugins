import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_haveibeenpwned.connection.connection import Connection
from icon_haveibeenpwned.actions.lookup_domain import LookupDomain
import json
import logging


class TestLookupDomain(TestCase):
    def test_lookup_domain(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
