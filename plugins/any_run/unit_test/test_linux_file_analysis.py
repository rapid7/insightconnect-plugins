import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate

from icon_any_run.actions.linux_file_analysis import LinuxFileAnalysis
from icon_any_run.actions.linux_file_analysis.schema import Input, Output

from util import Util


@patch("icon_any_run.actions.linux_file_analysis.action.SandboxConnector.linux")
class TestLinuxFileAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LinuxFileAnalysis())

    def test_linux_file_analysis(self, mock_linux: MagicMock) -> None:
        mock_connector = MagicMock()
        mock_linux.return_value.__enter__.return_value = mock_connector
        mock_linux.return_value.__exit__.return_value = None
        analysis_uuid = "c3d4e5f6-a7b8-9012-cdef-123456789012"
        mock_connector.run_file_analysis.return_value = analysis_uuid

        file_b64 = base64.b64encode(b"elf-bytes").decode()
        params = {Input.FILENAME: "sample.elf", Input.FILE_CONTENT: file_b64}
        actual = self.action.run(params)

        validate(actual, self.action.output.schema)
        self.assertEqual(
            actual,
            {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            },
        )
        mock_connector.run_file_analysis.assert_called_once_with(file_b64, "sample.elf")
