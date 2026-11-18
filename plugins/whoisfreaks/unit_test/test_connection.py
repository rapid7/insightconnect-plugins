import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import MagicMock

import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_whoisfreaks.connection.connection import Connection
from icon_whoisfreaks.connection.schema import Input
from util import API_KEY, FakeSession, MockResponse


def connected(*responses) -> tuple:
    connection = Connection()
    connection.logger = MagicMock()
    connection.connect({Input.API_KEY: {"secretKey": API_KEY}})
    session = FakeSession(*responses)
    connection.client._session = lambda: session
    connection.client._sleep = MagicMock()
    return connection, session


class TestConnection(TestCase):
    def test_connect_accepts_credential_and_plain_values(self):
        for value in ({"secretKey": f"  {API_KEY} "}, API_KEY):
            with self.subTest(value=value):
                connection = Connection()
                connection.logger = logging.getLogger("test")
                connection.connect({Input.API_KEY: value})
                self.assertEqual(API_KEY, connection.client._api_key)

    def test_connect_rejects_empty_key(self):
        for value in (None, {}, {"secretKey": "  "}):
            with self.subTest(value=value), self.assertRaises(PluginException):
                connection = Connection()
                connection.logger = logging.getLogger("test")
                connection.connect({Input.API_KEY: value})

    def test_success_uses_usage_endpoint(self):
        connection, session = connected(MockResponse(200, {"apiKey": API_KEY, "apiCredits": {}}))
        self.assertEqual({"success": True}, connection.test())
        self.assertEqual("https://api.whoisfreaks.com/v1.0/whoisapi/usage", session.calls[0]["url"])
        self.assertEqual(API_KEY, session.calls[0]["headers"]["X-API-KEY"])

    def test_invalid_key(self):
        connection, _ = connected(MockResponse(401, {"message": "Provided API key is invalid."}))
        with self.assertRaises(ConnectionTestException) as context:
            connection.test()
        self.assertIn("rejected the API key", context.exception.cause)

    def test_unknown_key(self):
        connection, _ = connected(MockResponse(404, {"message": "The API key does not exist."}))
        with self.assertRaises(ConnectionTestException) as context:
            connection.test()
        self.assertIn("does not recognise the API key", context.exception.cause)

    def test_valid_key_without_credits_passes_with_warning(self):
        connection, _ = connected(MockResponse(401, {"message": "Please buy a subscription plan or add api credits"}))
        self.assertEqual({"success": True}, connection.test())
        connection.logger.warning.assert_called_once()

    def test_network_failure(self):
        connection, session = connected(requests.exceptions.ConnectionError("refused"))
        with self.assertRaises(ConnectionTestException) as context:
            connection.test()
        self.assertIn("Could not connect", context.exception.cause)
        self.assertEqual(4, len(session.calls))
