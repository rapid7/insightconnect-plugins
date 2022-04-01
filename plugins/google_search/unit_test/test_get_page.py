import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_google_search.connection.connection import Connection
from komand_google_search.actions.get_page import GetPage
import json
import logging


class TestGetPage(TestCase):
    def test_get_page(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")