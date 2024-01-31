import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.get_rca_object import GetRcaObject
import json
import logging


class TestGetRcaObject(TestCase):
    def test_get_rca_object(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
