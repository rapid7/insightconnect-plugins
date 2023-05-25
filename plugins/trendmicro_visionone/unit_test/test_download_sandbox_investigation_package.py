from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException


class TestDownloadSandboxInvestigationPackage(TestCase):
    def setUp(self):
        self.action_name = "DownloadSandboxInvestigationPackage"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("download_sandbox_investigation_package")

    def test_integration_download_sandbox_investigation_package(self):
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(self.mock_params["output"].keys()))

    def test_download_sandbox_investigation_package_success(self):
        expected_result = self.mock_params["output"]
        mock_response = MagicMock()
        mock_response.response.content = b"mock content"
        self.action.connection.client.download_sandbox_investigation_package = (
            MagicMock(return_value=mock_response)
        )
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(expected_result.keys()))

    def test_download_sandbox_investigation_package_failure(self):
        self.action.connection.client.download_sandbox_investigation_package = (
            MagicMock(side_effect=PluginException)
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
