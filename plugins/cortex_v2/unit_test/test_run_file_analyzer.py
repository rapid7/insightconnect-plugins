import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.run_file_analyzer import RunFileAnalyzer
import json
import logging
from unittest.mock import patch


class TestRunFileAnalyzer(TestCase):
    def test_run_file_analyzer(self):
        self.fail("Unimplemented Test Case")
