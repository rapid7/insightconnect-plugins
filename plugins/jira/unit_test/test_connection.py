import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_jira.connection import Connection
from parameterized import param, parameterized
from requests.auth import HTTPBasicAuth


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @parameterized.expand(
        [
            param(
                "basic_auth",
                {
                    "user": "jakub",
                    "api_key": {"secretKey": "1234567"},
                    "url": "http://jira-123456.example.com",
                },
            ),
            param(
                "pat_auth",
                {
                    "pat": {"secretKey": "1234567"},
                    "url": "http://jira-123456.example.com",
                },
            ),
            param(
                "oauth2_auth",
                {
                    "client_id": "my-client-id",
                    "client_secret": {"secretKey": "my-client-secret"},
                    "url": "http://jira-123456.example.com",
                },
            ),
        ]
    )
    def test_validate_params_ok(self, name: str, params: dict[str, Any]) -> None:
        self.connection._validate_params(params)

    @parameterized.expand(
        [
            param(
                "password_no_username",
                {
                    "api_key": {"secretKey": "12345"},
                    "url": "http://jira-123456.example.com",
                },
                "Incomplete Basic Auth credentials.",
            ),
            param(
                "username_no_password",
                {
                    "user": "jakub",
                    "url": "http://jira-123456.example.com",
                },
                "Incomplete Basic Auth credentials.",
            ),
            param(
                "pat_and_basic_auth",
                {
                    "pat": {"secretKey": "1234567"},
                    "user": "jakub",
                    "api_key": {"secretKey": "12345"},
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "pat_and_oauth2",
                {
                    "pat": {"secretKey": "1234567"},
                    "client_id": "my-client-id",
                    "client_secret": {"secretKey": "my-client-secret"},
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "basic_auth_and_oauth2",
                {
                    "user": "jakub",
                    "api_key": {"secretKey": "12345"},
                    "client_id": "my-client-id",
                    "client_secret": {"secretKey": "my-client-secret"},
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "all_three_auth_methods",
                {
                    "pat": {"secretKey": "1234567"},
                    "user": "jakub",
                    "api_key": {"secretKey": "12345"},
                    "client_id": "my-client-id",
                    "client_secret": {"secretKey": "my-client-secret"},
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "oauth2_client_id_only",
                {
                    "client_id": "my-client-id",
                    "url": "http://jira-123456.example.com",
                },
                "Incomplete OAuth2 credentials.",
            ),
            param(
                "oauth2_client_secret_only",
                {
                    "client_secret": {"secretKey": "my-client-secret"},
                    "url": "http://jira-123456.example.com",
                },
                "Incomplete OAuth2 credentials.",
            ),
            param(
                "oauth2_and_basic_auth",
                {
                    "client_id": "my-client-id",
                    "client_secret": {"secretKey": "my-client-secret"},
                    "user": "jakub",
                    "api_key": {"secretKey": "12345"},
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "pat_with_username",
                {
                    "pat": {"secretKey": "1234567"},
                    "user": "jakub",
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "pat_with_client_id",
                {
                    "pat": {"secretKey": "1234567"},
                    "client_id": "my-client-id",
                    "url": "http://jira-123456.example.com",
                },
                "Multiple authentication methods provided.",
            ),
            param(
                "no_credentials",
                {
                    "url": "http://jira-123456.example.com",
                },
                "No authentication credentials provided.",
            ),
        ]
    )
    def test_validate_params_raise(self, name: str, params: dict[str, Any], cause: str) -> None:
        with self.assertRaises(PluginException) as exception_ctx:
            self.connection._validate_params(params)
        self.assertEqual(exception_ctx.exception.cause, cause)

    @parameterized.expand(
        [
            param(
                "basic_auth",
                {
                    "user": "test_user",
                    "api_key": {"secretKey": "test_password"},
                    "url": "http://jira-123456.example.com",
                },
            ),
        ]
    )
    @patch("komand_jira.connection.connection.JiraApi")
    @patch("komand_jira.connection.connection.JIRA")
    def test_connect_basic_auth(
        self, name: str, params: dict[str, Any], mock_jira: MagicMock, mock_jira_api: MagicMock
    ) -> None:
        # Connect using the provided parameters
        self.connection.connect(params)

        # Verify JIRA client was initialized with basic auth
        mock_jira.assert_called_once_with(
            options={"server": params.get("url")},
            basic_auth=(params.get("user"), params.get("api_key", {}).get("secretKey")),
        )

        # Verify JiraApi was initialized with HTTPBasicAuth
        mock_jira_api.assert_called_once()
        call_args = mock_jira_api.call_args
        self.assertEqual(call_args[0][0], params.get("url"))
        self.assertIsInstance(call_args[0][1], HTTPBasicAuth)
        self.assertEqual(call_args[0][1].username, params.get("user"))
        self.assertEqual(call_args[0][1].password, params.get("api_key", {}).get("secretKey"))

    @parameterized.expand(
        [
            param(
                "pat_auth",
                {
                    "pat": {"secretKey": "test_pat_token"},
                    "url": "http://jira-123456.example.com",
                },
            ),
        ]
    )
    @patch("komand_jira.connection.connection.JiraApi")
    @patch("komand_jira.connection.connection.JIRA")
    def test_connect_pat_auth(
        self, name: str, params: dict[str, Any], mock_jira: MagicMock, mock_jira_api: MagicMock
    ) -> None:
        # Connect using the provided parameters
        self.connection.connect(params)

        # Verify JIRA client was initialized with PAT
        mock_jira.assert_called_once_with(
            options={"server": params.get("url")}, token_auth=params.get("pat", {}).get("secretKey")
        )

        # Verify JiraApi was initialized with Bearer token
        mock_jira_api.assert_called_once()
        call_args = mock_jira_api.call_args
        self.assertEqual(call_args[0][0], params.get("url"))
        self.assertEqual(call_args[0][1], {"Authorization": f"Bearer {params.get('pat', {}).get('secretKey')}"})

    @parameterized.expand(
        [
            param(
                "oauth2_auth",
                {
                    "client_id": "test_client_id",
                    "client_secret": {"secretKey": "test_client_secret"},
                    "url": "http://jira-123456.example.com",
                },
            ),
        ]
    )
    @patch("komand_jira.connection.connection.JiraApi")
    @patch("komand_jira.connection.connection.JIRA")
    def test_connect_oauth2_auth(
        self, name: str, params: dict[str, Any], mock_jira: MagicMock, mock_jira_api: MagicMock
    ) -> None:
        # Connect using the provided parameters
        self.connection.connect(params)

        # Verify JIRA client was NOT initialized (OAuth2 not supported by JIRA library)
        mock_jira.assert_not_called()
        self.assertIsNone(self.connection.client)

        # Verify JiraApi was initialized with OAuth2 credentials
        mock_jira_api.assert_called_once()
        call_args = mock_jira_api.call_args
        self.assertEqual(call_args[0][0], params.get("url"))
        self.assertEqual(
            call_args[0][1],
            {"client_id": params.get("client_id"), "client_secret": params.get("client_secret", {}).get("secretKey")},
        )
