import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_gitlab.connection.connection import Connection
from komand_gitlab.actions.block_user import BlockUser
import json
import logging


class TestBlockUser(TestCase):
    def test_block_user(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
