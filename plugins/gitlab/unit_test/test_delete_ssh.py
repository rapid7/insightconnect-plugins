import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_gitlab.connection.connection import Connection
from komand_gitlab.actions.delete_ssh import DeleteSsh
import json
import logging


class TestDeleteSsh(TestCase):
    def test_delete_ssh(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
