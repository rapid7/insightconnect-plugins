import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import requests
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from util import BASE_URL, Util


class TestConnection(TestCase):
    def setUp(self):
        self.connection, _ = Util.default_connector(None)

    def test_connection_test_succeeds(self):
        send, sent = Util.mock_send(200, {"items": [], "count": 0})
        with patch.object(requests.Session, "send", send):
            actual = self.connection.test()

        self.assertEqual({"success": True}, actual)
        self.assertEqual(f"{BASE_URL}/assets?_limit=1", sent[0].url)
        self.assertEqual("9de5069c5afe602b2ea0a04b66beb2c0", sent[0].headers.get("Authorization"))

    def test_connection_strips_a_trailing_slash_from_the_url(self):
        connection, _ = Util.default_connector(None, {"api_key": {"secretKey": "key"}, "url": f"{BASE_URL}/"})
        send, sent = Util.mock_send(200, {"items": []})
        with patch.object(requests.Session, "send", send):
            connection.test()

        self.assertEqual(f"{BASE_URL}/assets?_limit=1", sent[0].url)

    @parameterized.expand([("unauthorized", 401), ("forbidden", 403), ("server_error", 500)])
    def test_connection_test_raises_connection_test_exception(self, _test_name, status_code):
        send, _sent = Util.mock_send(status_code, {"error": "Unauthorized", "message": "invalid api key"})
        with patch.object(requests.Session, "send", send):
            with self.assertRaises(ConnectionTestException):
                self.connection.test()
