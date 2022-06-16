import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.run_analyzer import RunAnalyzer
import json
import logging
from unittest.mock import patch


class TestRunAnalyzer(TestCase):
    def test_run_analyzer(self):
        self.fail("Unimplemented Test Case")
