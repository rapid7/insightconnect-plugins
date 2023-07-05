from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import CollectFile
from mock import mock_connection, mock_params


class TestCollectFile(TestCase):
    def setUp(self):
        self.action = CollectFile()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("collect_file")

    def test_integration_collect_file(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_collect_file_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_collect_file_failure(self):
        self.action.connection.client.collect_file = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
