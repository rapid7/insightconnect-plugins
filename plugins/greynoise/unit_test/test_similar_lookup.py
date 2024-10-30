import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.similar_lookup import SimilarLookup
import json
import logging


class TestSimilarLookup(TestCase):
    def test_similar_lookup(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
