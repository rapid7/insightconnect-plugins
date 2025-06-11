import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_matrix42.connection.connection import Connection
from icon_matrix42.actions.create_ticket import CreateTicket
import json
import logging


class TestCreateTicket(TestCase):
    def test_create_ticket(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
