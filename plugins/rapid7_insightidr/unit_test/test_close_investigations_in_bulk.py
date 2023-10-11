import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.connection.connection import Connection
from komand_rapid7_insightidr.actions.close_investigations_in_bulk import CloseInvestigationsInBulk
import json
import logging


class TestCloseInvestigationsInBulk(TestCase):
    def test_close_investigations_in_bulk(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
