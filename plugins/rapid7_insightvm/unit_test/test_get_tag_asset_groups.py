import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.get_tag_asset_groups import GetTagAssetGroups
import json
import logging


class TestGetTagAssetGroups(TestCase):
    def test_get_tag_asset_groups(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
