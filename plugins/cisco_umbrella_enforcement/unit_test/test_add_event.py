import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cisco_umbrella_enforcement.connection.connection import Connection
from komand_cisco_umbrella_enforcement.actions.add_event import AddEvent
import json
import logging


class TestAddEvent(TestCase):
    def test_add_event(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")
