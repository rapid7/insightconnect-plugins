import sys
import os
sys.path.append(os.path.abspath('../sublime_security/'))

from unittest import TestCase
from icon_sublime_security.connection.connection import Connection
from icon_sublime_security.actions.retrieve_message import RetrieveMessage
import json
import logging


class TestRetrieveMessage(TestCase):
    def test_retrieve_message(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
