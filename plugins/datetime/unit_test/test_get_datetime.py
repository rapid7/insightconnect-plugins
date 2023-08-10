import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_datetime.connection.connection import Connection
from icon_datetime.actions.get_datetime import GetDatetime
import json
import logging


class TestGetDatetime(TestCase):
    def test_get_datetime(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
