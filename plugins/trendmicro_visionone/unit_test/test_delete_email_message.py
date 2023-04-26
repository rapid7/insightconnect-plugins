import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.delete_email_message import DeleteEmailMessage
import json
import logging


class TestDeleteEmailMessage(TestCase):
    def test_delete_email_message(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")