import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_haveibeenpwned.connection.connection import Connection
from icon_haveibeenpwned.actions.lookup_password import LookupPassword
import json
import logging


class TestLookupPassword(TestCase):
    def test_lookup_password(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
