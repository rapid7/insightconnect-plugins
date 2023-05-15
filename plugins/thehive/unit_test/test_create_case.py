import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_thehive.connection.connection import Connection
from komand_thehive.actions.create_case import CreateCase
import json
import logging


class TestCreateCase(TestCase):
    def test_create_case(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
