import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.android_url_analysis import AndroidUrlAnalysis
from icon_any_run.actions.android_url_analysis.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("icon_any_run.actions.android_url_analysis.action.SandboxConnector.android")
class TestAndroidUrlAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AndroidUrlAnalysis())

    def test_android_url_analysis(self, mock_android: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_android.return_value.__enter__.return_value = mock_connector
        mock_android.return_value.__exit__.return_value = None
        analysis_uuid = "f6a7b8c9-d0e1-2345-f012-456789012345"
        mock_connector.run_url_analysis.return_value = analysis_uuid

        params = {Input.OBJ_URL: "https://example.com/android-target"}
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

    def test_android_url_analysis_raises_plugin_exception(self, mock_android: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_android.return_value.__enter__.return_value = mock_connector
        mock_android.return_value.__exit__.return_value = None
        mock_connector.run_url_analysis.side_effect = RunTimeException("analysis start error", 400)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.OBJ_URL: "https://example.com/android-target"})

        self.assertEqual(error.exception.cause, "Failed to start analysis.")
        self.assertEqual(error.exception.assistance, "analysis start error")
        self.assertEqual(error.exception.data, "{'description': 'analysis start error', 'code': 400}")
