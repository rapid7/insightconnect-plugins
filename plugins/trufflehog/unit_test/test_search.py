import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_trufflehog.connection.connection import Connection
from komand_trufflehog.actions.search import Search
import json
import logging


class TestSearch(TestCase):
    def test_search(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
