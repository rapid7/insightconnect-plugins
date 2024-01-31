import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.get_agent_status import GetAgentStatus
import json
import logging


class TestGetAgentStatus(TestCase):
    def test_get_agent_status(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
