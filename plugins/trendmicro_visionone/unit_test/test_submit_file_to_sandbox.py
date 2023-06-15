from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException
import base64


class TestSubmitFileToSandbox(TestCase):
    def setUp(self):
        self.action_name = "SubmitFileToSandbox"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("submit_file_to_sandbox")
        # Ensure 'file' is a dictionary with 'content' and 'filename' keys
        self.mock_params["input"]["file"] = {
            "content": base64.b64encode(b"mock file content").decode(),
            "filename": "mock_filename.txt",
        }

    def test_integration_submit_file_to_sandbox(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_submit_file_to_sandbox_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_submit_file_to_sandbox_failure(self):
        self.action.connection.client.submit_file_to_sandbox = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
