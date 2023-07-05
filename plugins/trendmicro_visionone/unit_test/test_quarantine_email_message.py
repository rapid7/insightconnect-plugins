from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import QuarantineEmailMessage
from mock import mock_connection, mock_params


class TestQuarantineEmailMessage(TestCase):
    def setUp(self):
        self.action = QuarantineEmailMessage()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("quarantine_email_message")

    def test_integration_quarantine_email_message(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_quarantine_email_message_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_quarantine_email_message_failure(self):
        self.action.connection.client.quarantine_email_message = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
