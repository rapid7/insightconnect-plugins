import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.actions.create_alert import CreateAlert
import json
import logging


class TestCreateAlert(TestCase):
    def test_create_alert(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
