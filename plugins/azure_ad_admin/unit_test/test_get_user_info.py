import logging
import os
import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from icon_azure_ad_admin.actions.get_user_info import GetUserInfo
from icon_azure_ad_admin.connection.connection import Connection
from icon_azure_ad_admin.util.get_user_info import get_user_info

from mocks import MockRequest


class TestGetUserInfo(TestCase):
    @mock.patch("icon_azure_ad_admin.util.get_user_info", return_value={"some": "some"})
    def setUp(self, mock_connection: MagicMock) -> None:
        self.connection = mock.create_autospec(Connection())
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.tenant = "tenant_id"

        self.action = GetUserInfo()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action loger")

        self.app_id = "application_id"
        self.app_secret = {"application_secret": {"secretKey": "secret_key"}}
        self.params = {"user_id": "user@example.com"}

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_get_user_info(self, mocked: MagicMock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            "user_information": {
                "accountEnabled": True,
                "manager": {
                    "@odata.type": "#microsoft.graph.user",
                },
            }
        }

        self.assertEqual(response, expected_response)


class TestUtilGetUserInfo(TestCase):
    def setUp(self) -> None:
        self.connection = mock.create_autospec(Connection())
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.tenant = "tenant_id"
        self.logger = logging.getLogger("get user info logger")

        self.app_id = "application_id"
        self.app_secret = {"application_secret": {"secretKey": "secret_key"}}
        self.params = {"user_id": "user@example.com"}

    @mock.patch("requests.get", return_value=MockRequest(400))
    def test_util_get_user_info_failed_with_plugin_exception(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            get_user_info(self.connection, "user_id", self.logger)
        self.assertEqual(
            context.exception.cause,
            "Get User Info failed.",
        )

    @mock.patch("requests.get", return_value=MockRequest(400))
    def test_util_get_user_info_failed(self, mock_request: MagicMock) -> None:
        mock_request.side_effect = Exception()
        result = get_user_info(self.connection, "user_id", self.logger)
        self.assertEqual(result, None)
