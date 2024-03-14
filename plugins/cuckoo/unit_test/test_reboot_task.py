import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_cuckoo.connection.connection import Connection
from komand_cuckoo.actions.reboot_task import RebootTask
import json
import logging


class TestRebootTask(TestCase):
    def test_reboot_task(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
