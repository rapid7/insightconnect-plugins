import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.linux_url_analysis import LinuxUrlAnalysis
from icon_any_run.actions.linux_url_analysis.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("icon_any_run.actions.linux_url_analysis.action.SandboxConnector.linux")
class TestLinuxUrlAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LinuxUrlAnalysis())

    def test_linux_url_analysis(self, mock_linux: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_linux.return_value.__enter__.return_value = mock_connector
        mock_linux.return_value.__exit__.return_value = None
        analysis_uuid = "d4e5f6a7-b8c9-0123-def0-234567890123"
        mock_connector.run_url_analysis.return_value = analysis_uuid

        params = {Input.OBJ_URL: "https://example.com/linux-target"}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            },
        )
        mock_connector.run_url_analysis.assert_called_once()

    def test_linux_url_analysis_raises_plugin_exception(self, mock_linux: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_linux.return_value.__enter__.return_value = mock_connector
        mock_linux.return_value.__exit__.return_value = None
        mock_connector.run_url_analysis.side_effect = RunTimeException("analysis start error", 400)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.OBJ_URL: "https://example.com/linux-target"})

        self.assertEqual(error.exception.cause, "Failed to start analysis.")
        self.assertEqual(error.exception.assistance, "analysis start error")
        self.assertEqual(error.exception.data, "{'description': 'analysis start error', 'code': 400}")
