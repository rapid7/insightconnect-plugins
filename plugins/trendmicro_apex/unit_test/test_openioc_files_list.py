import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.openioc_files_list import OpeniocFilesList
import json
import logging


class TestOpeniocFilesList(TestCase):
    def test_openioc_files_list(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
