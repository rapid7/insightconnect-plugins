from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import EditAlertStatus
from mock import mock_connection, mock_params


class TestEditAlertStatus(TestCase):
    def setUp(self):
        self.action = EditAlertStatus()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("edit_alert_status")

    def test_integration_edit_alert_status(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_edit_alert_status_success(self):
        expected_result = self.mock_params["output"]
        mock_response = MagicMock()
        mock_response.result_code = "mock result code"
        self.action.connection.client.edit_alert_status = MagicMock(return_value=mock_response)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_edit_alert_status_failure(self):
        self.action.connection.client.edit_alert_status = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
