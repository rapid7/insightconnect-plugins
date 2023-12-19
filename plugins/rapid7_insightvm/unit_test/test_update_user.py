import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.update_user import UpdateUser
import json
import logging


class TestUpdateUser(TestCase):
    def test_update_user(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
