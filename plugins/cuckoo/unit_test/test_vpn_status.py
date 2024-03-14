import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_cuckoo.connection.connection import Connection
from komand_cuckoo.actions.vpn_status import VpnStatus
import json
import logging


class TestVpnStatus(TestCase):
    def test_vpn_status(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
