import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.run_saved_search import RunSavedSearch
import json
import logging


class TestRunSavedSearch(TestCase):
    def test_run_saved_search(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
