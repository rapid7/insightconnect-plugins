import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.add_scan_engine_pool_engine import AddScanEnginePoolEngine
import json
import logging


class TestAddScanEnginePoolEngine(TestCase):
    def test_add_scan_engine_pool_engine(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
