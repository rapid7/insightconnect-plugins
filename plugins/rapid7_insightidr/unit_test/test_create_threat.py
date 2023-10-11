import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.connection.connection import Connection
from komand_rapid7_insightidr.actions.create_threat import CreateThreat
import json
import logging


class TestCreateThreat(TestCase):
    def test_create_threat(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
