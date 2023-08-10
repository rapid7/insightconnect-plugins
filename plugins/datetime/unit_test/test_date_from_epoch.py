import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_datetime.connection.connection import Connection
from icon_datetime.actions.date_from_epoch import DateFromEpoch
import json
import logging


class TestDateFromEpoch(TestCase):
    def test_date_from_epoch(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
