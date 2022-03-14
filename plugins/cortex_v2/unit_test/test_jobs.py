import sys
import os
from unittest import TestCase
from icon_cortex_v2.actions.bulk_analyze import BulkAnalyze
from icon_cortex_v2.actions.bulk_analyze.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util


sys.path.append(os.path.abspath("../"))


class TestJobs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(BulkAnalyze())

    def test_bulk_analyze(self, ):
