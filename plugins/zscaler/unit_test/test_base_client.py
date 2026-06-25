"""
Unit tests for BaseClient (OAuth 2.0 auth, token caching, error handling, routing).
"""

import os
import sys
import time
import json
import logging
from unittest import TestCase

sys.path.append(os.path.abspath("../"))
from unittest.mock import Mock, patch

from parameterized import parameterized
import requests

sys.path.append(os.path.abspath("../"))

from icon_zscaler.util.zia_client import ZIAClient
from icon_zscaler.util.zpa_client import ZPAClient
from icon_zscaler.util.constants import Cause, Assistance
from insightconnect_plugin_runtime.exceptions import PluginException

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_zia_client():
    client = ZIAClient(
        client_id="test-client-id",
        private_key="fake-private-key",
        vanity_domain="mycompany",
        cloud="zsapi.net",
        logger=logging.getLogger("test"),
    )
    client._token = "pre-seeded-token"
    client._token_expiry = int(time.time()) + 3600
    return client


def _mock_response(status_code=200, json_data=None, text="", headers=None):
    resp = Mock(spec=requests.Response)
    resp.status_code = status_code
    resp.text = text or json.dumps(json_data if json_data is not None else {})
    resp.headers = headers or {}
    resp.json.return_value = json_data if json_data is not None else {}
    return resp


def _generate_rsa_pem():
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


# ---------------------------------------------------------------------------
# _authenticate()
# ---------------------------------------------------------------------------


class TestAuthenticate(TestCase):

    @patch("requests.request")
    def test_produces_valid_jwt_and_stores_token(self, mock_request):
        mock_request.return_value = _mock_response(200, {"access_token": "tok123", "expires_in": 3600})

        client = _make_zia_client()
        client._token = None
        client._token_expiry = 0
        client.private_key = _generate_rsa_pem()

        client._authenticate()

        self.assertEqual(client._token, "tok123")
        self.assertGreater(client._token_expiry, int(time.time()))

        call_kwargs = mock_request.call_args[1]
        self.assertEqual(call_kwargs["url"], "https://mycompany.zsapi.net/oauth2/v1/token")
        self.assertIn("grant_type=client_credentials", call_kwargs["data"])
        self.assertIn("client_assertion=", call_kwargs["data"])

        import jwt

        assertion = call_kwargs["data"].split("client_assertion=")[1]
        decoded = jwt.decode(assertion, options={"verify_signature": False})
        self.assertEqual(decoded["iss"], "test-client-id")
        self.assertEqual(decoded["sub"], "test-client-id")
        self.assertEqual(decoded["exp"] - decoded["iat"], 300)

    @patch("requests.request")
    def test_raises_on_failed_token_response(self, mock_request):
        mock_request.return_value = _mock_response(401, text="Unauthorized")

        client = _make_zia_client()
        client._token = None
        client._token_expiry = 0
        client.private_key = _generate_rsa_pem()

        with self.assertRaises(PluginException) as ctx:
            client._authenticate()
        self.assertIn("Failed to obtain OAuth 2.0 access token", ctx.exception.cause)


# ---------------------------------------------------------------------------
# _get_token() caching
# ---------------------------------------------------------------------------


class TestGetToken(TestCase):

    def test_returns_cached_when_valid(self):
        client = _make_zia_client()
        self.assertEqual(client._get_token(), "pre-seeded-token")

    @patch("requests.request")
    def test_refreshes_when_near_expiry(self, mock_request):
        mock_request.return_value = _mock_response(200, {"access_token": "refreshed", "expires_in": 3600})

        client = _make_zia_client()
        client._token_expiry = int(time.time()) + 20  # within 30s buffer
        client.private_key = _generate_rsa_pem()

        self.assertEqual(client._get_token(), "refreshed")
        mock_request.assert_called_once()


# ---------------------------------------------------------------------------
# _handle_status() error mapping and 401 retry
# ---------------------------------------------------------------------------


class TestHandleStatus(TestCase):

    @parameterized.expand(
        [
            (400, Cause.INVALID_DETAILS, Assistance.VERIFY_INPUT),
            (403, Cause.INSUFFICIENT_PERMISSIONS, Assistance.CHECK_PERMISSIONS),
            (404, Cause.RESOURCE_NOT_FOUND, Assistance.VERIFY_INPUT),
            (429, Cause.RATE_LIMITED, Assistance.RATE_LIMIT_WAIT),
            (500, Cause.SERVER_ERROR, Assistance.CONTACT_SUPPORT),
            (503, Cause.SERVICE_UNAVAILABLE, Assistance.RETRY_LATER),
        ]
    )
    def test_maps_error_codes(self, status_code, expected_cause, expected_assistance):
        client = _make_zia_client()
        with self.assertRaises(PluginException) as ctx:
            client._handle_status(_mock_response(status_code, text="err"), "GET", "https://api.zsapi.net/test")
        self.assertEqual(ctx.exception.cause, expected_cause)
        self.assertEqual(ctx.exception.assistance, expected_assistance)

    @patch("requests.request")
    def test_401_retries_once_then_succeeds(self, mock_request):
        mock_request.return_value = _mock_response(200, {"ok": True})
        client = _make_zia_client()
        client._authenticate = Mock()

        result = client._handle_status(_mock_response(401), "GET", "https://api.zsapi.net/test")
        self.assertEqual(result.status_code, 200)
        client._authenticate.assert_called_once()

    @patch("requests.request")
    def test_401_raises_after_retry_still_fails(self, mock_request):
        mock_request.return_value = _mock_response(401, text="still bad")
        client = _make_zia_client()
        client._authenticate = Mock()

        with self.assertRaises(PluginException) as ctx:
            client._handle_status(_mock_response(401), "GET", "https://api.zsapi.net/test")
        self.assertEqual(ctx.exception.cause, Cause.TOKEN_EXPIRED)


# ---------------------------------------------------------------------------
# _call_api() transport errors
# ---------------------------------------------------------------------------


class TestCallApi(TestCase):

    @patch("requests.request", side_effect=requests.exceptions.Timeout("timed out"))
    def test_timeout(self, _):
        client = _make_zia_client()
        with self.assertRaises(PluginException) as ctx:
            client._call_api("GET", "https://api.zsapi.net/test")
        self.assertIn("timed out", ctx.exception.cause.lower())

    @patch("requests.request", side_effect=requests.exceptions.ConnectionError("refused"))
    def test_connection_error(self, _):
        client = _make_zia_client()
        with self.assertRaises(PluginException) as ctx:
            client._call_api("GET", "https://api.zsapi.net/test")
        self.assertIn("connection error", ctx.exception.cause.lower())


# ---------------------------------------------------------------------------
# Request routing (URLs, auth headers, service prefixes)
# ---------------------------------------------------------------------------


class TestRouting(TestCase):

    @patch("requests.request")
    def test_zia_routes_to_oneapi_with_bearer(self, mock_request):
        mock_request.return_value = _mock_response(200, {"rules": []})
        client = _make_zia_client()
        client.list_firewall_rules()

        call_kwargs = mock_request.call_args[1]
        self.assertTrue(call_kwargs["url"].startswith("https://api.zsapi.net/"))
        self.assertIn("/zia/api/v1/firewallRules", call_kwargs["url"])
        self.assertEqual(call_kwargs["headers"]["Authorization"], "Bearer pre-seeded-token")

    @patch("requests.request")
    def test_zpa_routes_to_oneapi_with_bearer(self, mock_request):
        mock_request.return_value = _mock_response(200, {"segments": []})
        client = ZPAClient(
            client_id="test-client-id",
            private_key="fake-private-key",
            vanity_domain="mycompany",
            cloud="zsapi.net",
            logger=logging.getLogger("test"),
        )
        client._token = "pre-seeded-token"
        client._token_expiry = int(time.time()) + 3600
        client.list_application_segments()

        call_kwargs = mock_request.call_args[1]
        self.assertIn("/zpa/api/v1/application", call_kwargs["url"])
        self.assertEqual(call_kwargs["headers"]["Authorization"], "Bearer pre-seeded-token")

    @patch("requests.request")
    def test_next_link_uses_direct_url(self, mock_request):
        mock_request.return_value = _mock_response(200, {"rules": []})
        client = _make_zia_client()
        direct_url = "https://api.zsapi.net/zia/api/v1/firewallRules?page=2"
        client.list_firewall_rules(next_link=direct_url)

        call_kwargs = mock_request.call_args[1]
        self.assertEqual(call_kwargs["url"], direct_url)
