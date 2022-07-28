import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.connection.connection import Connection
from icon_rapid7_insightvm_cloud.actions.asset_search import AssetSearch
import json
import logging


class TestAssetSearch(TestCase):
    def test_asset_search(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.assertEqual(True, True)