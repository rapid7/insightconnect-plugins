import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.create_saved_search import CreateSavedSearch
import json
import logging


class TestCreateSavedSearch(TestCase):
    def test_create_saved_search(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
