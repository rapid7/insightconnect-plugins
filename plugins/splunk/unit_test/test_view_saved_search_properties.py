import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.view_saved_search_properties import ViewSavedSearchProperties
import json
import logging


class TestViewSavedSearchProperties(TestCase):
    def test_view_saved_search_properties(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
