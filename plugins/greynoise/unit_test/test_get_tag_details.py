import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_greynoise.connection.connection import Connection
from icon_greynoise.actions.get_tag_details import GetTagDetails
import json
import logging


class TestGetTagDetails(TestCase):
    def test_get_tag_details(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
