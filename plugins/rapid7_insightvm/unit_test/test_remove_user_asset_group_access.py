import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_rapid7_insightvm.connection.connection import Connection
from komand_rapid7_insightvm.actions.remove_user_asset_group_access import RemoveUserAssetGroupAccess
import json
import logging


class TestRemoveUserAssetGroupAccess(TestCase):
    def test_remove_user_asset_group_access(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
