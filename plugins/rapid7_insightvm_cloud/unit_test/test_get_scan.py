import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.connection.connection import Connection
from icon_rapid7_insightvm_cloud.actions.get_scan import GetScan
import json
import logging


class TestGetScan(TestCase):
    def test_get_scan(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")