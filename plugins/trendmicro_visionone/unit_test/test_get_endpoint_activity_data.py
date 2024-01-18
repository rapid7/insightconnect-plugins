from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import GetEndpointActivityData
from mock import mock_connection, mock_params


class TestGetEndpointActivityData(TestCase):
    def setUp(self):
        self.action = GetEndpointActivityData()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("get_endpoint_activity_data")

    def test_1_integration_get_endpoint_activity_data(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_2_get_endpoint_activity_data_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_3_get_endpoint_activity_data_failure(self):
        self.action.connection.client.consume_endpoint_activity_data = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
