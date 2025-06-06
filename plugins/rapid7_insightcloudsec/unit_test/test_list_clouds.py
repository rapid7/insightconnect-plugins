import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.connection.connection import Connection
from icon_rapid7_insightcloudsec.actions.list_clouds import ListClouds
import json
import logging


class TestListClouds(TestCase):
    def test_list_clouds(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
