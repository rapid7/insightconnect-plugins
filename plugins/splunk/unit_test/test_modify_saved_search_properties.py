import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_splunk.connection.connection import Connection
from komand_splunk.actions.modify_saved_search_properties import ModifySavedSearchProperties
import json
import logging


class TestModifySavedSearchProperties(TestCase):
    def test_modify_saved_search_properties(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
