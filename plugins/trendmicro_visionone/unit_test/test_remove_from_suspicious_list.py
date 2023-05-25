from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException


class TestRemoveFromSuspiciousList(TestCase):
    def setUp(self):
        self.action_name = "RemoveFromSuspiciousList"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("remove_from_suspicious_list")

    def test_integration_remove_from_suspicious_list(self):
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(self.mock_params["output"].keys()))

    def test_remove_from_suspicious_list_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(expected_result.keys()))

    def test_remove_from_suspicious_list_failure(self):
        self.action.connection.client.remove_from_suspicious_list = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
