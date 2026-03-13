import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.actions.close_alert import CloseAlert
import json
import logging


class TestCloseAlert(TestCase):
    def test_close_alert(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
