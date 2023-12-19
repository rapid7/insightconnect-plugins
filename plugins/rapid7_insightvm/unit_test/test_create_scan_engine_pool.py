import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.create_scan_engine_pool import CreateScanEnginePool
import json
import logging


class TestCreateScanEnginePool(TestCase):
    def test_create_scan_engine_pool(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
