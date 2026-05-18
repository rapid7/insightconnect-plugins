import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.android_file_analysis import AndroidFileAnalysis
from icon_any_run.actions.android_file_analysis.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("icon_any_run.actions.android_file_analysis.action.SandboxConnector.android")
class TestAndroidFileAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AndroidFileAnalysis())

    def test_android_file_analysis(self, mock_android: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_android.return_value.__enter__.return_value = mock_connector
        mock_android.return_value.__exit__.return_value = None
        analysis_uuid = "e5f6a7b8-c9d0-1234-ef01-345678901234"
        mock_connector.run_file_analysis.return_value = analysis_uuid

        file_b64 = base64.b64encode(b"apk-bytes").decode()
        params = {Input.FILENAME: "sample.apk", Input.FILE_CONTENT: file_b64}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            },
        )
        mock_connector.run_file_analysis.assert_called_once_with(file_content=file_b64, filename="sample.apk")

    def test_android_file_analysis_raises_plugin_exception(self, mock_android: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_android.return_value.__enter__.return_value = mock_connector
        mock_android.return_value.__exit__.return_value = None
        mock_connector.run_file_analysis.side_effect = RunTimeException("analysis start error", 400)

        file_b64 = base64.b64encode(b"apk-bytes").decode()
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.FILENAME: "sample.apk", Input.FILE_CONTENT: file_b64})

        self.assertEqual(error.exception.cause, "Failed to start analysis.")
        self.assertEqual(error.exception.assistance, "analysis start error")
        self.assertEqual(error.exception.data, "{'description': 'analysis start error', 'code': 400}")
