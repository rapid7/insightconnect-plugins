from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import DownloadSandboxAnalysisResult
from .tmv1_mock import mock_connection, mock_params


class TestDownloadSandboxAnalysisResult(TestCase):
    def setUp(self):
        self.action = DownloadSandboxAnalysisResult()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("download_sandbox_analysis_result")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_download_sandbox_analysis_result(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_download_sandbox_analysis_result_success(self):
        expected_result = self.mock_params["output"]
        mock_response = MagicMock()
        mock_response.response.content = b"mock content"
        self.action.connection.client.download_sandbox_analysis_result = MagicMock(
            return_value=mock_response
        )
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_download_sandbox_analysis_result_failure(self):
        self.action.connection.client.download_sandbox_analysis_result = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
