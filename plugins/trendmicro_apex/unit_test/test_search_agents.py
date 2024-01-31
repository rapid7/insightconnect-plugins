import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.search_agents import SearchAgents
import json
import logging


class TestSearchAgents(TestCase):
    def test_search_agents(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
