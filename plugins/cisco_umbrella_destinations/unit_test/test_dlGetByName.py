import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlGetByName import Dlgetbyname
import json
import logging


class TestDlgetbyname(TestCase):
    def test_dlGetByName(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")