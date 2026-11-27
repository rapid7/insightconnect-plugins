import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

import requests
from icon_halo_itsm.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from util import BASE_URL, LOGGER_NAME, MockResponse, token_response

PARAMS = {
    "base_url": f"{BASE_URL}/",
    "client_id": " client-id ",
    "client_secret": {"secretKey": " client-secret "},
    "tenant": " my-tenant ",
}


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger(LOGGER_NAME)

    @patch("requests.Session.request", return_value=MockResponse(200, {"tickets": []}))
    @patch("requests.post", return_value=token_response())
    def test_connection_test(self, mock_post: MagicMock, mock_request: MagicMock) -> None:
        self.connection.connect(PARAMS)

        self.assertEqual({"success": True}, self.connection.test())
        # Values are trimmed, and the tenant travels as a query parameter instead of being pasted into the URL
        self.assertEqual((f"{BASE_URL}/auth/token",), mock_post.call_args.args)
        self.assertEqual({"tenant": "my-tenant"}, mock_post.call_args.kwargs["params"])
        self.assertEqual("client-id", mock_post.call_args.kwargs["data"]["client_id"])
        self.assertEqual("client-secret", mock_post.call_args.kwargs["data"]["client_secret"])
        self.assertEqual("client_credentials", mock_post.call_args.kwargs["data"]["grant_type"])
        # The test reads one ticket, which proves read access as well as the token
        self.assertEqual(("GET", f"{BASE_URL}/api/tickets"), mock_request.call_args.args)
        self.assertEqual({"count": 1}, mock_request.call_args.kwargs["params"])

    @patch("requests.Session.request", return_value=MockResponse(200, {"tickets": []}))
    @patch("requests.post", return_value=token_response())
    def test_connection_without_tenant_sends_no_tenant(self, mock_post: MagicMock, _mock_request: MagicMock) -> None:
        self.connection.connect({**PARAMS, "tenant": ""})
        self.connection.test()

        self.assertIsNone(mock_post.call_args.kwargs["params"])

    @patch("requests.post", return_value=MockResponse(401, text='{"error": "invalid_client"}'))
    def test_connection_test_bad_credentials(self, _mock_post: MagicMock) -> None:
        self.connection.connect(PARAMS)

        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        # The HTTP status is in the cause and Halo's answer in the data, so a failure can be diagnosed from the log
        self.assertEqual("Authentication failed (HTTP 401).", context.exception.cause)
        self.assertEqual('{"error": "invalid_client"}', context.exception.data)

    @patch("requests.post", return_value=MockResponse(200, {"token_type": "Bearer"}))
    def test_connection_test_without_an_access_token(self, _mock_post: MagicMock) -> None:
        self.connection.connect(PARAMS)

        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        self.assertEqual("No access token returned from authentication endpoint.", context.exception.cause)

    @patch("requests.post", side_effect=requests.exceptions.Timeout())
    def test_connection_test_timeout(self, _mock_post: MagicMock) -> None:
        self.connection.connect(PARAMS)

        with self.assertRaises(ConnectionTestException):
            self.connection.test()

    @patch("requests.post", side_effect=requests.exceptions.ConnectionError("name resolution failed"))
    def test_connection_test_unreachable_host(self, _mock_post: MagicMock) -> None:
        self.connection.connect(PARAMS)

        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        self.assertEqual("Connection error occurred during authentication.", context.exception.cause)
        self.assertEqual("name resolution failed", context.exception.data)
