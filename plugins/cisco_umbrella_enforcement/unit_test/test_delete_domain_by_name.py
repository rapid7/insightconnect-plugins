import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cisco_umbrella_enforcement.connection.connection import Connection
from komand_cisco_umbrella_enforcement.actions.delete_domain_by_name import DeleteDomainByName
import json
import logging


class TestDeleteDomainByName(TestCase):
    def test_delete_domain_by_name(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here

        For information on mocking and unit testing please go here:

        https://docs.google.com/document/d/1PifePDG1-mBcmNYE8dULwGxJimiRBrax5BIDG_0TFQI/edit?usp=sharing
        """

        self.fail("Unimplemented Test Case")
