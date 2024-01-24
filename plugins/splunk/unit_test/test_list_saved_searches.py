import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.list_saved_searches import ListSavedSearches
import json
import logging


class TestListSavedSearches(TestCase):
    def test_list_saved_searches(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
