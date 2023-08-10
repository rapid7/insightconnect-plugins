import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_datetime.connection.connection import Connection
from icon_datetime.actions.to_localtime import ToLocaltime
import json
import logging


class TestToLocaltime(TestCase):
    def test_to_localtime(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
