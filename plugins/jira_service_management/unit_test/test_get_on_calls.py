import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.actions.get_on_calls import GetOnCalls
import json
import logging


class TestGetOnCalls(TestCase):
    def test_get_on_calls(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
