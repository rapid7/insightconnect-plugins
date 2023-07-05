from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import AddToExceptionList
from mock import mock_connection, mock_params


class TestAddToExceptionList(TestCase):
    def setUp(self):
        self.action = AddToExceptionList()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("add_to_exception_list")

    def test_integration_add_to_exception_list(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_add_to_exception_list_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_add_to_exception_list_failure(self):
        self.action.connection.client.add_to_exception_list = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
