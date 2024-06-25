import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightidr.connection.connection import Connection
from komand_rapid7_insightidr.actions.update_alert import UpdateAlert
import json
import logging


class TestUpdateAlert(TestCase):
    def test_update_alert(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
