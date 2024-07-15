from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import RunCustomScript
from mock import mock_connection, mock_params


class TestRunCustomScript(TestCase):
    def setUp(self):
        self.action = RunCustomScript()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("run_custom_script")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_1_integration_run_custom_script(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_2_run_custom_script_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_3_run_custom_script_failure(self):
        self.action.connection.client.script.run = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
