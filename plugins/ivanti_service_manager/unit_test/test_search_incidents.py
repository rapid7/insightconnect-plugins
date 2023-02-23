import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_ivanti_service_manager.connection.connection import Connection
from icon_ivanti_service_manager.actions.search_incidents import SearchIncidents
import json
import logging


class TestSearchIncidents(TestCase):
    def test_search_incidents(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")