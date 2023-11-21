import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_joe_sandbox.connection.connection import Connection
from icon_joe_sandbox.actions.get_server_info import GetServerInfo
import json
import logging


class TestGetServerInfo(TestCase):
    def test_get_server_info(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
