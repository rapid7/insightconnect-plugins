from unittest import TestCase, skip
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_trendmicro_visionone.actions import SignOutAccount
from .tmv1_mock import mock_connection, mock_params


class TestSignOutAccount(TestCase):
    def setUp(self):
        self.action = SignOutAccount()
        self.connection = mock_connection()
        self.action.connection = self.connection
        self.mock_params = mock_params("sign_out_account")

    @skip("Integration test - we don't want to run this, and it is getting 500 from endpoint causing a failure.")
    def test_integration_sign_out_account(self):
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(self.mock_params["output"].keys()))

    def test_sign_out_account_success(self):
        expected_result = self.mock_params["output"]
        self.action.connection.client = MagicMock(return_value=expected_result)
        response = self.action.run(self.mock_params["input"])
        for key in response.keys():
            self.assertIn(key, str(expected_result.keys()))

    def test_sign_out_account_failure(self):
        self.action.connection.client.sign_out_account = MagicMock(
            side_effect=PluginException
        )
        with self.assertRaises(PluginException):
            self.action.run(self.mock_params["input"])
