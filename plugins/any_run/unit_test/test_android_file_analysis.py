import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate

from icon_any_run.actions.android_file_analysis import AndroidFileAnalysis
from icon_any_run.actions.android_file_analysis.schema import Input, Output

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
        mock_connector.run_file_analysis.assert_called_once_with(file_b64, "sample.apk")
