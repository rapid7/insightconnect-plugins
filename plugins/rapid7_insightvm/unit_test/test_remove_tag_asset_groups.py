import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.remove_tag_asset_groups import RemoveTagAssetGroups
import json
import logging


class TestRemoveTagAssetGroups(TestCase):
    def test_remove_tag_asset_groups(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
