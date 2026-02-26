import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.actions.get_alert import GetAlert
import json
import logging


class TestGetAlert(TestCase):
    def test_get_alert(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
