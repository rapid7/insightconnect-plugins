import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.remove_from_block_list import RemoveFromBlockList
import json
import logging


class TestRemoveFromBlockList(TestCase):
    def test_remove_from_block_list(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")