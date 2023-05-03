import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_thehive.connection.connection import Connection
from icon_thehive.actions.get_cases import GetCases
import json
import logging


class TestGetCases(TestCase):
    def test_get_cases(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")