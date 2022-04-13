import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cortex_v2.actions.bulk_analyze import BulkAnalyze
from icon_cortex_v2.actions.bulk_analyze.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.mock import Mock


sys.path.append(os.path.abspath("../"))


class TestJobs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Mock.default_connector(BulkAnalyze())
        cls.params = {
            Input.ANALYZER_IDS: "",
            Input.ANALYZE_ALL: False,
            Input.OBSERVABLE: "rapid7.com",
            Input.ATTRIBUTES: {"dataType": "domain", "tlp": 1}
        }

    @patch("requests.request", side_effect=Mock.mocked_request)
    def test_bulk_analyze(self, params):
        actual = self.action.run()
        expected = ""
        self.assertEqual(expected, actual)
