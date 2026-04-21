import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from anyrun import RunTimeException
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_any_run.actions.get_analysis_history import GetAnalysisHistory
from icon_any_run.actions.get_analysis_history.schema import Input, Output

from util import Util


SAMPLE_ANALYSES = [
    {
        "verdict": "Malicious",
        "name": "sample.bin",
        "related": "https://related.example",
        "pcap": "https://pcap.example",
        "file": "https://file.example",
        "json": "https://json.example",
        "misp": "https://misp.example",
        "tags": ["tag1"],
        "date": "2024-01-01T00:00:00",
        "hashes": {
            "md5": "d41d8cd98f00b204e9800998ecf8427e",
            "sha1": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
            "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "ssdeep": "",
            "head_hash": "",
        },
        "uuid": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    }
]


@patch("icon_any_run.actions.get_analysis_history.action.BaseSandboxConnector")
class TestGetAnalysisHistory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAnalysisHistory())

    def test_get_analysis_history(self, mock_connector_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_analysis_history.return_value = SAMPLE_ANALYSES

        params = {Input.TEAM: False, Input.SKIP: 0, Input.LIMIT: 25}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(actual, {Output.ANALYSES: SAMPLE_ANALYSES})
        mock_cm.get_analysis_history.assert_called_once_with(**params)

    def test_get_analysis_history_raises_plugin_exception(self, mock_connector_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_analysis_history.side_effect = RunTimeException("history error", 400)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.TEAM: False, Input.SKIP: 0, Input.LIMIT: 25})

        self.assertEqual(error.exception.cause, "Failed to fetch analysis history.")
        self.assertEqual(error.exception.assistance, "history error")
        self.assertEqual(error.exception.data, "{'description': 'history error', 'code': 400}")
