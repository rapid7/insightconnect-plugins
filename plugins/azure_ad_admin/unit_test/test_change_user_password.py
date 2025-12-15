import logging
import os
import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from icon_azure_ad_admin.actions.change_user_password import ChangeUserPassword
from icon_azure_ad_admin.connection.connection import Connection

from mocks import MockRequest


class TestChangeUserPassword(TestCase):
    def setUp(self) -> None:
        self.connection = mock.create_autospec(Connection())
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.tenant = "tenant_id"
        self.app_id = "application_id"
        self.app_secret = {"application_secret": {"secretKey": "secret_key"}}

        self.action = ChangeUserPassword()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action loger")

        self.params = {
            "user_id": "user@example.com",
            "password": "newPassword",
        }

    @mock.patch("requests.patch", return_value=MockRequest(204))
    def test_change_user_password(self, mock_request: MagicMock) -> None:
        change_user_password = self.action.run(self.params)

        expected_result = {"success": True}
        self.assertEqual(change_user_password, expected_result)

    @mock.patch("requests.patch", return_value=MockRequest(400))
    def test_change_user_password_failed(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException):
            self.action.run(self.params)
