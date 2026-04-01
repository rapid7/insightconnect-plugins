import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate

from icon_any_run.actions.windows_url_analysis import WindowsUrlAnalysis
from icon_any_run.actions.windows_url_analysis.schema import Input, Output

from util import Util


@patch("icon_any_run.actions.windows_url_analysis.action.SandboxConnector.windows")
class TestWindowsUrlAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(WindowsUrlAnalysis())

    def test_windows_url_analysis(self, mock_windows: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_windows.return_value.__enter__.return_value = mock_connector
        mock_windows.return_value.__exit__.return_value = None
        analysis_uuid = "b2c3d4e5-f6a7-8901-bcde-f12345678901"
        mock_connector.run_url_analysis.return_value = analysis_uuid

        params = {Input.OBJ_URL: "https://example.com/suspicious"}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            },
        )
        mock_connector.run_url_analysis.assert_called_once_with(**params)
