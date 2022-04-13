import sys
import os
from unittest import TestCase
from unittest.mock import patch
from icon_cortex_v2.actions.run_file_analyzer import RunFileAnalyzer
from icon_cortex_v2.actions.run_file_analyzer.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.mock import Mock

sys.path.append(os.path.abspath("../"))


class TestRunFileAnalyzer(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Mock.default_connector(RunFileAnalyzer())
        cls.params = {
            Input.ANALYZER_ID: "",
            Input.FILE: None,
            Input.ATTRIBUTES: {"filename": "test.txt", "tlp": 1}
        }

    @patch("requests.request", side_effect=Mock.mocked_request)
    def test_run_file_analyzer(self, _mock_request):
        actual = self.action.run(self.params)
        expected = ""
        self.assertEqual(expected, actual)
