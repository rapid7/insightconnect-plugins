from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import ListApiKeys
from mock import mock_connection, mock_params


class TestListApiKeys(TestCase):
    def setUp(self):
        self.action = ListApiKeys()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("list_api_keys")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_list_api_keys(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_list_api_keys_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_list_api_keys_failure(self):
        self.action.connection.client.api_key.consume = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
