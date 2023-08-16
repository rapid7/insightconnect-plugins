from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import GetSandboxSubmissionStatus
from mock import mock_connection, mock_params


class TestGetSandboxSubmissionStatus(TestCase):
    def setUp(self):
        self.action = GetSandboxSubmissionStatus()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("get_sandbox_submission_status")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_get_sandbox_submission_status(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_get_sandbox_submission_status_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_get_sandbox_submission_status_failure(self):
        self.action.connection.client.get_sandbox_submission_status = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
