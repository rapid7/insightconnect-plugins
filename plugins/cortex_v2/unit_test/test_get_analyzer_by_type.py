import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_cortex_v2.connection.connection import Connection
from icon_cortex_v2.actions.get_analyzer_by_type import GetAnalyzerByType
import json
import logging
from unittest.mock import patch


class TestGetAnalyzerByType(TestCase):
    def test_get_analyzer_by_type(self):
        self.fail("Unimplemented Test Case")
