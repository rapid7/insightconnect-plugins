import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_surface_command.connection.connection import Connection
from icon_rapid7_surface_command.actions.run_query import RunQuery
import json
import logging


class TestRunQuery(TestCase):
    def test_run_query(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
