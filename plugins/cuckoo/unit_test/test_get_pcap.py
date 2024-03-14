import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_cuckoo.connection.connection import Connection
from komand_cuckoo.actions.get_pcap import GetPcap
import json
import logging


class TestGetPcap(TestCase):
    def test_get_pcap(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
