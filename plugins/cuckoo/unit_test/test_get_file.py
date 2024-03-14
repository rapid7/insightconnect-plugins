import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_cuckoo.connection.connection import Connection
from komand_cuckoo.actions.get_file import GetFile
import json
import logging


class TestGetFile(TestCase):
    def test_get_file(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
