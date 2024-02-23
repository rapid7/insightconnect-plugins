import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_joe_sandbox.connection.connection import Connection
from icon_joe_sandbox.actions.check_server_status import CheckServerStatus
import json
import logging


class TestCheckServerStatus(TestCase):
    def test_check_server_status(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
