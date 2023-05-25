from unittest import TestCase
from unittest.mock import MagicMock
from .mock import mock_connection, mock_action, mock_params
from insightconnect_plugin_runtime.exceptions import PluginException


class TestGetTaskResult(TestCase):
    def setUp(self):
        self.action_name = "GetTaskResult"
        self.connection = mock_connection()
        self.action = mock_action(self.connection, self.action_name)
        self.mock_params = mock_params("get_task_result")

    def test_integration_get_task_result(self):
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(self.mock_params["output"].keys()))

    def test_get_task_result_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for i in response.keys():
            self.assertIn(i, str(expected_result.keys()))

    def test_get_task_result_failure(self):
        self.action.connection.client.get_base_task_result = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
