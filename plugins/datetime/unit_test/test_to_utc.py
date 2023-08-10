import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_datetime.connection.connection import Connection
from icon_datetime.actions.to_utc import ToUtc
import json
import logging


class TestToUtc(TestCase):
    def test_to_utc(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
