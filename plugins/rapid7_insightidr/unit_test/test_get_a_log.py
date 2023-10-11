import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightidr.connection.connection import Connection
from komand_rapid7_insightidr.actions.get_a_log import GetALog
import json
import logging


class TestGetALog(TestCase):
    def test_get_a_log(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
