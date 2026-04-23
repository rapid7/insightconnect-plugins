import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from anyrun import RunTimeException
from icon_any_run.actions.get_analysis_report import GetAnalysisReport
from icon_any_run.actions.get_analysis_report.schema import Input, Output
from icon_any_run.util.tools import prepare_file_payload
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util

ANALYSIS_UUID = "44d88612-fea8-a8f3-6de8-2e1278abb02f"


@patch("icon_any_run.util.tools.datetime")
@patch("icon_any_run.actions.get_analysis_report.action.BaseSandboxConnector")
class TestGetAnalysisReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAnalysisReport())

    def _freeze_time(self, mock_datetime: MagicMock) -> None:
        frozen = MagicMock()
        frozen.strftime.return_value = "2024-01-01_00-00-00"
        mock_datetime.now.return_value = frozen

    def test_get_analysis_report_json(self, mock_connector_cls: MagicMock, mock_datetime: MagicMock) -> None:
        self._freeze_time(mock_datetime)
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_task_status.return_value = []
        report_body = {"threat": True}
        mock_cm.get_analysis_report.return_value = report_body

        params = {Input.ANALYSIS_UUID: ANALYSIS_UUID, Input.FORMAT: "json"}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        expected_report = prepare_file_payload(ANALYSIS_UUID, "json", report_body)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: ANALYSIS_UUID,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{ANALYSIS_UUID}",
                Output.REPORT: expected_report,
            },
        )

    def test_get_analysis_report_html(self, mock_connector_cls: MagicMock, mock_datetime: MagicMock) -> None:
        self._freeze_time(mock_datetime)
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_task_status.return_value = ["completed"]
        html = "<html><body>report</body></html>"
        mock_cm.get_analysis_report.return_value = html

        params = {Input.ANALYSIS_UUID: ANALYSIS_UUID, Input.FORMAT: "html"}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        expected_report = prepare_file_payload(ANALYSIS_UUID, "html", html)
        self.assertEqual(actual[Output.REPORT]["filename"], expected_report["filename"])
        self.assertEqual(actual[Output.REPORT]["content"], expected_report["content"])

    def test_get_analysis_report_raises_plugin_exception(
        self, mock_connector_cls: MagicMock, mock_datetime: MagicMock
    ) -> None:
        self._freeze_time(mock_datetime)
        mock_cm = MagicMock()
        mock_connector_cls.return_value.__enter__.return_value = mock_cm
        mock_connector_cls.return_value.__exit__.return_value = None
        mock_cm.get_task_status.return_value = []
        mock_cm.get_analysis_report.side_effect = RunTimeException("report error", 404)

        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ANALYSIS_UUID: ANALYSIS_UUID, Input.FORMAT: "json"})

        self.assertEqual(error.exception.cause, "Failed to download analysis report.")
        self.assertEqual(error.exception.assistance, "report error")
        self.assertEqual(error.exception.data, "{'description': 'report error', 'code': 404}")
