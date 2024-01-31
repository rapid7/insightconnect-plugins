import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_trendmicro_apex.connection.connection import Connection
from icon_trendmicro_apex.actions.download_rca_csv_file import DownloadRcaCsvFile
import json
import logging


class TestDownloadRcaCsvFile(TestCase):
    def test_download_rca_csv_file(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
