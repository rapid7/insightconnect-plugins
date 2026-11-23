import sys
import os

sys.path.append(os.path.abspath("../"))

import base64
import logging
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from icon_bitdefender_gravityzone.connection.connection import Connection
from icon_bitdefender_gravityzone.connection.schema import Input
from icon_bitdefender_gravityzone.util.api import normalize_base_url
from util import NETWORK_URL, STUB_API_KEY, STUB_URL, Util


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.URL: STUB_URL, Input.API_KEY: {"secretKey": STUB_API_KEY}})

    @patch("requests.Session.send")
    def test_connection_success(self, mock_send):
        mock_send.return_value = Util.payload_response("get_endpoints_list.json.resp")

        self.assertEqual({"success": True}, self.connection.test())

        request = Util.sent_request(mock_send)
        payload = Util.sent_payload(mock_send)
        expected_auth = "Basic " + base64.b64encode(f"{STUB_API_KEY}:".encode()).decode()
        self.assertEqual(NETWORK_URL, request.url)
        self.assertEqual(expected_auth, request.headers["Authorization"])
        self.assertEqual("getEndpointsList", payload["method"])
        self.assertEqual({"page": 1, "perPage": 1}, payload["params"])
        self.assertEqual("2.0", payload["jsonrpc"])

    @patch("requests.Session.send")
    def test_connection_unauthorized(self, mock_send):
        mock_send.return_value = Util.response(status_code=401, text="Unauthorized")

        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        self.assertEqual("GravityZone rejected the API key (HTTP 401).", context.exception.cause)
        self.assertEqual(
            "Check that the API key in the connection is correct and active.", context.exception.assistance
        )
        self.assertEqual("Unauthorized", context.exception.data)

    @patch("requests.Session.send")
    def test_connection_api_error(self, mock_send):
        mock_send.return_value = Util.rpc_error(-32001, "Authorization error", "API Key is not allowed")

        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        self.assertEqual("GravityZone API error -32001: Authorization error.", context.exception.cause)
        self.assertIn("Network API and the Incidents API", context.exception.assistance)
        self.assertIn("API Key is not allowed", context.exception.data)

    def test_normalize_base_url(self):
        cases = [
            ("bare host", "https://cloud.gravityzone.bitdefender.com", STUB_URL),
            ("trailing slash", "https://cloud.gravityzone.bitdefender.com/", STUB_URL),
            ("trailing api", "https://cloud.gravityzone.bitdefender.com/api", STUB_URL),
            ("trailing api and slash", "https://cloud.gravityzone.bitdefender.com/api/", STUB_URL),
            ("upper case api and spaces", "  https://cloud.gravityzone.bitdefender.com/API  ", STUB_URL),
            ("api inside the host is kept", "https://api.example.com", "https://api.example.com"),
        ]
        for name, url, expected in cases:
            with self.subTest(name):
                self.assertEqual(expected, normalize_base_url(url))

    @patch("requests.Session.send")
    def test_connection_url_with_api_suffix(self, mock_send):
        mock_send.return_value = Util.payload_response("get_endpoints_list.json.resp")
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect({Input.URL: f"{STUB_URL}/api/", Input.API_KEY: {"secretKey": STUB_API_KEY}})

        connection.test()

        self.assertEqual(NETWORK_URL, Util.sent_request(mock_send).url)
