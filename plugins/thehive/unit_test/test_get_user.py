import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_thehive.connection.connection import Connection
from icon_thehive.actions.get_user import GetUser
import json
import logging


class TestGetUser(TestCase):
    def test_get_user(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")