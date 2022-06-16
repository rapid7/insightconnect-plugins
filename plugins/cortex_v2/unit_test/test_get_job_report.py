import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.get_job_report import GetJobReport
import json
import logging
from unittest.mock import patch


class TestGetJobReport(TestCase):
    def test_get_job_report(self):
        self.fail("Unimplemented Test Case")
