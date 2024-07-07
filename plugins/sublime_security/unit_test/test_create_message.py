import sys
import os
sys.path.append(os.path.abspath('../sublime_security/'))

from unittest import TestCase
from icon_sublime_security.connection.connection import Connection
from icon_sublime_security.actions.create_message import CreateMessage
import json
import logging


class TestCreateMessage(TestCase):
    def test_create_message(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
