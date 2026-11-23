import sys
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("./"))

from icon_dectrax.connection.connection import Connection
from icon_dectrax.actions.get_attacker_ips import GetAttackerIps
from icon_dectrax.actions.get_attacker_ips.schema import Input, Output


class TestGetAttackerIps(TestCase):

    def setUp(self):
        self.connection = Connection()
        self.connection.logger = MagicMock()
        self.connection.connect({
            "url": "https://dectrax.internal",
            "api_key": {"secretKey": "test-key"},
            "ssl_verify": False,
        })
        self.action = GetAttackerIps()
        self.action.connection = self.connection
        self.action.logger = MagicMock()

    @patch("requests.get")
    def test_get_attacker_ips(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "attackers": ["198.51.100.24", "203.0.113.88"]
        }
        mock_get.return_value = mock_response

        response = self.action.run({Input.LIMIT: 100})
        expected = {
            Output.ATTACKERS: ["198.51.100.24", "203.0.113.88"],
            Output.COUNT: 2,
        }
        self.assertEqual(response, expected)
