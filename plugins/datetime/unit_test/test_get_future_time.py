import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_datetime.connection.connection import Connection
from icon_datetime.actions.get_future_time import GetFutureTime
import json
import logging


class TestGetFutureTime(TestCase):
    def test_get_future_time(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
