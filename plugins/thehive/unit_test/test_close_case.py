import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_thehive.connection.connection import Connection
from komand_thehive.actions.close_case import CloseCase
import json
import logging
from parameterized import parameterized


class TestCloseCase(TestCase):
    def test_close_case(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
