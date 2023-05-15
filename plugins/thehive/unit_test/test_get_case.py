import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_thehive.connection.connection import Connection
from komand_thehive.actions.get_case import GetCase
import json
import logging


class TestGetCase(TestCase):
    def test_get_case(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
