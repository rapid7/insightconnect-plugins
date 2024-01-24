import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.delete_saved_search import DeleteSavedSearch
import json
import logging


class TestDeleteSavedSearch(TestCase):
    def test_delete_saved_search(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
