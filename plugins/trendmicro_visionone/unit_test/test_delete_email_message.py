from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import DeleteEmailMessage
from mock import mock_connection, mock_params


class TestDeleteEmailMessage(TestCase):
    def setUp(self):
        self.action = DeleteEmailMessage()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("delete_email_message")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_delete_email_message(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_delete_email_message_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_delete_email_message_failure(self):
        self.action.connection.client.delete_email_message = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
