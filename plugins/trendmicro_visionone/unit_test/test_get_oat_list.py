import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_oat_list import GetOatList
import json
import logging


class TestGetOatList(TestCase):
    def test_get_oat_list(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
