import sys
import os
sys.path.append(os.path.abspath('../sublime_security/'))

from unittest import TestCase
from icon_sublime_security.connection.connection import Connection
from icon_sublime_security.actions.analyze_message_by_id import AnalyzeMessageById
import json
import logging


class TestAnalyzeMessageById(TestCase):
    def test_analyze_message_by_id(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
