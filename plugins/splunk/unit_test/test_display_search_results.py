import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.display_search_results import DisplaySearchResults
import json
import logging


class TestDisplaySearchResults(TestCase):
    def test_display_search_results(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
