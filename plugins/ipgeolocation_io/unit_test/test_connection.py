from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_ipgeolocation_io.connection.connection import Connection
from unit_test.mock import UNAUTHORIZED_API_KEY, make_connection, mock_request, sent_params
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestConnection(TestCase):
    def test_connection_test_succeeds(self, mocked):
        connection = make_connection()

        self.assertEqual(connection.test(), {"success": True})
        # The test must hit /v3/ipgeo, the only endpoint every plan can reach.
        self.assertTrue(mocked.call_args.args[1].endswith("/v3/ipgeo"))
        self.assertNotIn("ip", sent_params(mocked))

    def test_connection_test_raises_connection_test_exception_on_401(self, mocked):
        connection = make_connection(UNAUTHORIZED_API_KEY)

        with self.assertRaises(ConnectionTestException) as context:
            connection.test()
        self.assertIn("rejected the API key", context.exception.cause)

    def test_connect_rejects_blank_secret_key(self, mocked):
        connection = Connection()
        connection.logger = logging.getLogger("test-connection")

        with self.assertRaises(PluginException) as context:
            connection.connect({"api_key": {"secretKey": "   "}})
        self.assertIn("No IPGeolocation.io API key", context.exception.cause)

    def test_connect_builds_api_client(self, mocked):
        connection = make_connection()

        self.assertIsNotNone(connection.api)
        self.assertEqual(connection.api.api_key, "0123456789abcdef0123456789abcdef")
