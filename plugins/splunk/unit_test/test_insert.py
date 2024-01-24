import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.insert import Insert
import json
import logging


class TestInsert(TestCase):
    def test_insert(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
