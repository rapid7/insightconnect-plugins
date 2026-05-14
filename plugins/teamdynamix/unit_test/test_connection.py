"""Unit tests for the TeamDynamix connection and request helper."""

import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_teamdynamix.util.request_helper import TeamDynamixClient
from icon_teamdynamix.util.constants import TIMEOUT, AUTH_ENDPOINT, HTTP_ERROR_MAP
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
import logging


class TestTeamDynamixClient(TestCase):
    def setUp(self):
        self.logger = logging.getLogger("test")
        self.client = TeamDynamixClient(
            base_url="https://example.teamdynamix.com",
            beid="test-beid",
            web_services_key="test-key",
            app_id=42,
            logger=self.logger,
        )

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_authenticate_success(self, mock_session_class):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '"some-bearer-token"'
        mock_session.post.return_value = mock_response
        self.client._session = mock_session

        token = self.client._authenticate()

        self.assertEqual(token, "some-bearer-token")
        mock_session.post.assert_called_once_with(
            f"https://example.teamdynamix.com{AUTH_ENDPOINT}",
            json={"BEID": "test-beid", "WebServicesKey": "test-key"},
            timeout=TIMEOUT,
        )

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_authenticate_failure(self, mock_session_class):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_session.post.return_value = mock_response
        self.client._session = mock_session

        with self.assertRaises(PluginException):
            self.client._authenticate()

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_authenticate_empty_token(self, mock_session_class):
        mock_session = MagicMock()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = ""
        mock_session.post.return_value = mock_response
        self.client._session = mock_session

        with self.assertRaises(PluginException):
            self.client._authenticate()

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_authenticate_timeout(self, mock_session_class):
        mock_session = MagicMock()
        mock_session.post.side_effect = requests.exceptions.Timeout("Connection timed out")
        self.client._session = mock_session

        with self.assertRaises(PluginException) as context:
            self.client._authenticate()
        self.assertIn("timed out", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_authenticate_connection_error(self, mock_session_class):
        mock_session = MagicMock()
        mock_session.post.side_effect = requests.exceptions.ConnectionError("DNS resolution failed")
        self.client._session = mock_session

        with self.assertRaises(PluginException) as context:
            self.client._authenticate()
        self.assertIn("Unable to connect", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_success(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ID": 1, "Title": "Test"}
        mock_session.request.return_value = mock_response

        result = self.client.make_request("get", "/TDWebApi/api/42/tickets/1")

        self.assertEqual(result["ID"], 1)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_timeout(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"
        mock_session.request.side_effect = requests.exceptions.Timeout("Timed out")

        with self.assertRaises(PluginException) as context:
            self.client.make_request("get", "/TDWebApi/api/42/tickets/1")
        self.assertIn("timed out", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_connection_error(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"
        mock_session.request.side_effect = requests.exceptions.ConnectionError("Connection refused")

        with self.assertRaises(PluginException) as context:
            self.client.make_request("get", "/TDWebApi/api/42/tickets/1")
        self.assertIn("Unable to connect", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_401_retry(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "expired-token"

        mock_401 = MagicMock()
        mock_401.status_code = 401

        mock_auth = MagicMock()
        mock_auth.status_code = 200
        mock_auth.text = '"new-token"'

        mock_success = MagicMock()
        mock_success.status_code = 200
        mock_success.json.return_value = {"ID": 1}

        mock_session.request.side_effect = [mock_401, mock_success]
        mock_session.post.return_value = mock_auth

        result = self.client.make_request("get", "/TDWebApi/api/42/tickets/1")

        self.assertEqual(result["ID"], 1)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_204_returns_empty(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 204
        mock_session.request.return_value = mock_response

        result = self.client.make_request("delete", "/TDWebApi/api/42/tickets/1/tags")

        self.assertEqual(result, {})

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_400_raises_with_mapped_message(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_session.request.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.client.make_request("post", "/TDWebApi/api/42/tickets")
        self.assertIn("invalid input", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_404_raises_with_mapped_message(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_session.request.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.client.make_request("get", "/TDWebApi/api/42/tickets/99999")
        self.assertIn("not found", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_429_raises_rate_limit(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 429
        mock_response.text = "Too Many Requests"
        mock_session.request.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.client.make_request("post", "/TDWebApi/api/42/tickets/search")
        self.assertIn("rate limit", context.exception.cause)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_make_request_500_raises_server_error(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_session.request.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.client.make_request("get", "/TDWebApi/api/42/tickets/1")
        self.assertIn("internal server error", context.exception.cause)

    def test_base_url_trailing_slash_stripped(self):
        client = TeamDynamixClient(
            base_url="https://example.teamdynamix.com/",
            beid="test",
            web_services_key="test",
            app_id=42,
        )
        self.assertEqual(client.base_url, "https://example.teamdynamix.com")

    def test_tickets_endpoint_property(self):
        self.assertEqual(self.client.tickets_endpoint, "/TDWebApi/api/42/tickets")

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_helper_get_ticket(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ID": 123, "Title": "Test"}
        mock_session.request.return_value = mock_response

        result = self.client.get_ticket(123)

        self.assertEqual(result["ID"], 123)
        call_args = mock_session.request.call_args
        self.assertIn("/TDWebApi/api/42/tickets/123", call_args[1]["url"])

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_helper_search_tickets_returns_list(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"ID": 1}, {"ID": 2}]
        mock_session.request.return_value = mock_response

        result = self.client.search_tickets({"MaxResults": 10})

        self.assertEqual(len(result), 2)

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_helper_search_tickets_non_list_returns_empty(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"unexpected": "response"}
        mock_session.request.return_value = mock_response

        result = self.client.search_tickets({"MaxResults": 10})

        self.assertEqual(result, [])

    @patch("icon_teamdynamix.util.request_helper.requests.Session")
    def test_test_method(self, mock_session_class):
        mock_session = MagicMock()
        self.client._session = mock_session
        self.client._token = "valid-token"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_session.request.return_value = mock_response

        result = self.client.test()

        self.assertTrue(result)
