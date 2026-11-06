import sys
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("./"))

from icon_dectrax.connection.connection import Connection
from icon_dectrax.actions.query_telemetry import QueryTelemetry
from icon_dectrax.actions.query_telemetry.schema import Input, Output


class TestQueryTelemetry(TestCase):

    def setUp(self):
        self.connection = Connection()
        self.connection.logger = MagicMock()
        self.connection.connect({
            "url": "https://dectrax.internal",
            "api_key": {"secretKey": "test-key"},
            "ssl_verify": False,
        })
        self.action = QueryTelemetry()
        self.action.connection = self.connection
        self.action.logger = MagicMock()

    @patch("requests.get")
    def test_query_telemetry_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "events": [
                {"timestamp": "2026-10-25T20:00:00Z", "protocol": "ssh", "decoy_service": "ssh_honeypot"},
                {"timestamp": "2026-10-25T20:01:00Z", "protocol": "http", "decoy_service": "web_portal"},
            ]
        }
        mock_get.return_value = mock_response

        response = self.action.run({Input.IP: "198.51.100.24"})
        self.assertTrue(response[Output.FOUND])
        self.assertEqual(response[Output.EVENTS_COUNT], 2)
        self.assertIn("ssh", response[Output.PROTOCOLS])
        self.assertIn("http", response[Output.PROTOCOLS])

    @patch("requests.get")
    def test_query_telemetry_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        response = self.action.run({Input.IP: "192.0.2.1"})
        expected = {
            Output.FOUND: False,
            Output.EVENTS_COUNT: 0,
            Output.PROTOCOLS: [],
        }
        self.assertEqual(response, expected)
