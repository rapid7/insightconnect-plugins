import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.bulk_analyze import BulkAnalyze
import json
import logging
from unittest.mock import patch


class TestBulkAnalyze(TestCase):
    def test_bulk_analyze(self):
        self.fail("Unimplemented Test Case")
