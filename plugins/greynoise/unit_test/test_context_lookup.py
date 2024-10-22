import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.context_lookup import ContextLookup
import json
import logging


class TestContextLookup(TestCase):
    def test_context_lookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
