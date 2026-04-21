import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from anyrun import RunTimeException
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_any_run.actions.get_analysis_verdict import GetAnalysisVerdict
from icon_any_run.actions.get_analysis_verdict.schema import Input, Output

from util import Util


@patch("icon_any_run.actions.get_analysis_verdict.action.BaseSandboxConnector")
class TestGetAnalysisVerdict(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAnalysisVerdict())

    def test_get_analysis_verdict(self, mock_connector_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_analysis_verdict.return_value = "Malicious"

        analysis_uuid = "44d88612-fea8-a8f3-6de8-2e1278abb02f"
        actual = self.action.run({Input.ANALYSIS_UUID: analysis_uuid})

        validate(actual, self.action.output.schema)
        self.assertEqual(actual, {Output.VERDICT: "Malicious"})
        mock_cm.get_analysis_verdict.assert_called_once_with(analysis_uuid)

    def test_get_analysis_verdict_raises_plugin_exception(self, mock_connector_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_analysis_verdict.side_effect = RunTimeException("verdict error", 403)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ANALYSIS_UUID: "44d88612-fea8-a8f3-6de8-2e1278abb02f"})

        self.assertEqual(error.exception.cause, "Failed to fetch analysis verdict.")
        self.assertEqual(error.exception.assistance, "verdict error")
        self.assertEqual(error.exception.data, "{'description': 'verdict error', 'code': 403}")
