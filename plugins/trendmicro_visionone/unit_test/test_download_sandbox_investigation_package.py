from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import DownloadSandboxInvestigationPackage
from mock import mock_connection, mock_params


class TestDownloadSandboxInvestigationPackage(TestCase):
    def setUp(self):
        self.action = DownloadSandboxInvestigationPackage()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("download_sandbox_investigation_package")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_download_sandbox_investigation_package(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_download_sandbox_investigation_package_success(self):
        expected_result = self.mock_params["output"]
        mock_response = MagicMock()
        mock_response.response.content = b"mock content"
        self.action.connection.client.download_sandbox_investigation_package = MagicMock(return_value=mock_response)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_download_sandbox_investigation_package_failure(self):
        self.action.connection.client.download_sandbox_investigation_package = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
