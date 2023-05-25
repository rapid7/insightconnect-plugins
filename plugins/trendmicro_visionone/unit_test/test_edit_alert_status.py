from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException


class TestEditAlertStatus(TestCase):
    def setUp(self):
        self.action_name = "EditAlertStatus"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("edit_alert_status")

    def test_integration_edit_alert_status(self):
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(self.mock_params["output"].keys()))

    def test_edit_alert_status_success(self):
        expected_result = self.mock_params["output"]
        mock_response = MagicMock()
        mock_response.result_code = "mock result code"
        self.action.connection.client.edit_alert_status = MagicMock(
            return_value=mock_response
        )
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(expected_result.keys()))

    def test_edit_alert_status_failure(self):
        self.action.connection.client.edit_alert_status = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
