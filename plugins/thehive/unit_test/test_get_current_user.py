import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_thehive.connection.connection import Connection
from komand_thehive.actions.get_current_user import GetCurrentUser
import json
import logging
from parameterized import parameterized


class TestGetCurrentUser(TestCase):
    def test_get_current_user(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
