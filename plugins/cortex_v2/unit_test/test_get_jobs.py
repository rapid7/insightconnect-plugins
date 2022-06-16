import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.get_jobs import GetJobs
import json
import logging
from unittest.mock import patch


class TestGetJobs(TestCase):
    def test_get_jobs(self):
        self.fail("Unimplemented Test Case")
