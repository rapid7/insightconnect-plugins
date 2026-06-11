import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_aws_securityhub.connection.connection import Connection
from icon_aws_securityhub.actions.batch_update_findings import BatchUpdateFindings
import json
import logging


class TestBatchUpdateFindings(TestCase):
    def test_batch_update_findings(self):
        """
        DO NOT USE PRODUCTION/SENSITIVE DATA FOR UNIT TESTS

        TODO: Implement test cases here
        """

        self.fail("Unimplemented Test Case")
