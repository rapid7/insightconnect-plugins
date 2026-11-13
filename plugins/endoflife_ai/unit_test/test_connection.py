import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_endoflife_ai.connection.schema import Input

from util import connection, mocked_requests_get, STUB_CONNECTION_ANONYMOUS, STUB_CONNECTION_WITH_KEY


class TestConnection(TestCase):
    def test_connect_anonymous(self):
        test_connection = connection(STUB_CONNECTION_ANONYMOUS)
        self.assertEqual("https://api.endoflife.ai", test_connection.base)
        self.assertIsNone(test_connection.api_key)
        self.assertNotIn("X-API-Key", test_connection.headers)

    def test_connect_with_key_and_trailing_slash(self):
        params = dict(STUB_CONNECTION_WITH_KEY)
        params[Input.URL] = "https://api.endoflife.ai/"
        test_connection = connection(params)
        self.assertEqual("https://api.endoflife.ai", test_connection.base)
        self.assertEqual("test-key", test_connection.headers["X-API-Key"])

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_connection_test(self, mock_get):
        result = connection(STUB_CONNECTION_ANONYMOUS).test()
        self.assertEqual({"success": True, "tier": "anon", "rate_limit": "100 requests/day"}, result)
        self.assertEqual("https://api.endoflife.ai/v1", mock_get.call_args[0][0])

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_connection_test_wrong_url(self, mock_get):
        with self.assertRaises(ConnectionTestException):
            connection({Input.URL: "https://example.invalid"}).test()
