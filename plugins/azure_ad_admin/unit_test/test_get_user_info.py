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

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_get_user_info_with_select_includes_account_enabled(self, mocked: MagicMock) -> None:
        params = {"user_id": "user@example.com", "select": ["accountEnabled", "city", "department"]}
        response = self.action.run(params)
        expected_response = {
            "user_information": {
                "accountEnabled": True,
                "manager": {
                    "@odata.type": "#microsoft.graph.user",
                },
            }
        }

        self.assertEqual(response, expected_response)
        # With accountEnabled in select, only 1 call should be made (no second call for accountEnabled)
        self.assertEqual(mocked.call_count, 1)

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_get_user_info_with_select_without_account_enabled(self, mocked: MagicMock) -> None:
        params = {"user_id": "user@example.com", "select": ["city", "department"]}
        response = self.action.run(params)
        expected_response = {
            "user_information": {
                "accountEnabled": True,
                "manager": {
                    "@odata.type": "#microsoft.graph.user",
                },
            }
        }

        self.assertEqual(response, expected_response)
        # Without accountEnabled in select, 2 calls should be made
        self.assertEqual(mocked.call_count, 2)


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

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_util_get_user_info_with_select(self, mock_request: MagicMock) -> None:
        get_user_info(self.connection, "user_id", self.logger, select=["city", "department", "accountEnabled"])
        called_url = mock_request.call_args[0][0]
        # Should include both default properties and the user-specified ones
        self.assertIn("city", called_url)
        self.assertIn("department", called_url)
        self.assertIn("accountEnabled", called_url)
        self.assertIn("displayName", called_url)
        self.assertIn("id", called_url)
        self.assertIn("$expand=manager", called_url)

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_util_get_user_info_with_select_filters_manager(self, mock_request: MagicMock) -> None:
        get_user_info(self.connection, "user_id", self.logger, select=["city", "manager", "department"])
        called_url = mock_request.call_args[0][0]
        self.assertIn("city", called_url)
        self.assertIn("department", called_url)
        # manager should not be in the $select portion since it's handled by $expand
        select_part = called_url.split("$select=")[1]
        self.assertNotIn("manager", select_part)
        self.assertIn("$expand=manager", called_url)

    @mock.patch("requests.get")
    def test_util_get_user_info_resolves_upn_for_sign_in_activity(self, mock_request: MagicMock) -> None:
        # Setup connection mocks for auth
        self.connection.get_auth_token.return_value = "test_token"
        self.connection.get_headers.return_value = {"Authorization": "Bearer test_token"}

        resolve_response = MagicMock()
        resolve_response.status_code = 200
        resolve_response.json.return_value = {"id": "08290005-23ba-46b4-a377-b381d651a2fb"}

        user_info_response = MockRequest(200)

        mock_request.side_effect = [resolve_response, user_info_response]

        get_user_info(self.connection, "user@example.com", self.logger, select=["signInActivity"])

        # First call should be the GUID resolution
        first_call_url = mock_request.call_args_list[0][0][0]
        self.assertIn("user@example.com", first_call_url)
        self.assertIn("$select=id", first_call_url)

        # Second call should use the resolved GUID and include signInActivity in select
        second_call_url = mock_request.call_args_list[1][0][0]
        self.assertIn("08290005-23ba-46b4-a377-b381d651a2fb", second_call_url)
        self.assertIn("signInActivity", second_call_url)
        self.assertIn("displayName", second_call_url)

    @mock.patch("requests.get", return_value=MockRequest(200))
    def test_util_get_user_info_skips_resolve_when_guid_provided(self, mock_request: MagicMock) -> None:
        get_user_info(self.connection, "08290005-23ba-46b4-a377-b381d651a2fb", self.logger, select=["signInActivity"])
        # Only 1 call should be made (no resolution needed since user_id is already a GUID)
        self.assertEqual(mock_request.call_count, 1)
        called_url = mock_request.call_args[0][0]
        self.assertIn("08290005-23ba-46b4-a377-b381d651a2fb", called_url)
