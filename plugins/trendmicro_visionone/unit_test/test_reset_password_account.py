from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import ResetPasswordAccount
from mock import mock_connection, mock_params


class TestResetPasswordAccount(TestCase):
    def setUp(self):
        self.action = ResetPasswordAccount()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("reset_password_account")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_reset_password_account(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_reset_password_account_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_reset_password_account_failure(self):
        self.action.connection.client.reset_password_account = MagicMock(side_effect=PluginException)
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
