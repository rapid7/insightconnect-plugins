from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import DownloadCustomScript
from mock import mock_connection, mock_params


class TestDownloadCustomScript(TestCase):
    def setUp(self):
        self.action = DownloadCustomScript()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("download_custom_script")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_download_custom_script(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_download_custom_script_success(self):
        expected_result = self.mock_params["output"]
        mock_content = "mock content"
        mock_response = MagicMock()
        mock_response.response.content = mock_content.encode("utf-8")
        mock_response.response.text = mock_content
        self.action.connection.client.script.download = MagicMock(return_value=mock_response)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_download_custom_script_result_failure(self):
        self.action.connection.client.script.download = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
