import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_ipqualityscore.connection.connection import Connection
from icon_ipqualityscore.actions.phoneLookup import Phonelookup
import json
import logging


class TestPhonelookup(TestCase):
    def test_phoneLookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")