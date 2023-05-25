from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException


class TestDeleteEmailMessage(TestCase):
    def setUp(self):
        self.action_name = "DeleteEmailMessage"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("delete_email_message")

    def test_integration_delete_email_message(self):
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(self.mock_params["output"].keys()))

    def test_delete_email_message_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(expected_result.keys()))

    def test_delete_email_message_failure(self):
        self.action.connection.client.delete_email_message = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
