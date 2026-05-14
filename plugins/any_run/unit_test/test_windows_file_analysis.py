import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.windows_file_analysis import WindowsFileAnalysis
from icon_any_run.actions.windows_file_analysis.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("icon_any_run.actions.windows_file_analysis.action.SandboxConnector.windows")
class TestWindowsFileAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(WindowsFileAnalysis())

    def test_windows_file_analysis(self, mock_windows: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_windows.return_value.__enter__.return_value = mock_connector
        mock_windows.return_value.__exit__.return_value = None
        analysis_uuid = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        mock_connector.run_file_analysis.return_value = analysis_uuid

        file_b64 = base64.b64encode(b"fake-pe-content").decode()
        params = {Input.FILENAME: "sample.exe", Input.FILE_CONTENT: file_b64}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            },
        )
        mock_connector.run_file_analysis.assert_called_once()
        call_kwargs = mock_connector.run_file_analysis.call_args[1]
        self.assertEqual(call_kwargs["file_content"], file_b64)
        self.assertEqual(call_kwargs["filename"], "sample.exe")

    def test_windows_file_analysis_raises_plugin_exception(self, mock_windows: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_windows.return_value.__enter__.return_value = mock_connector
        mock_windows.return_value.__exit__.return_value = None
        mock_connector.run_file_analysis.side_effect = RunTimeException("analysis start error", 400)

        file_b64 = base64.b64encode(b"fake-pe-content").decode()
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.FILENAME: "sample.exe", Input.FILE_CONTENT: file_b64})

        self.assertEqual(error.exception.cause, "Failed to start analysis.")
        self.assertEqual(error.exception.assistance, "analysis start error")
        self.assertEqual(error.exception.data, "{'description': 'analysis start error', 'code': 400}")
