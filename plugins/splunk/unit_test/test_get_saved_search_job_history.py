import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.get_saved_search_job_history import GetSavedSearchJobHistory
import json
import logging


class TestGetSavedSearchJobHistory(TestCase):
    def test_get_saved_search_job_history(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
