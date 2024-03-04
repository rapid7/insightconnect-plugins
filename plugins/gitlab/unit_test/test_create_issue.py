import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_gitlab.connection.connection import Connection
from komand_gitlab.actions.create_issue import CreateIssue
import json
import logging


class TestCreateIssue(TestCase):
    def test_create_issue(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
