import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_bitdefender_gravityzone_comprehensive.connection.connection import Connection
from komand_bitdefender_gravityzone_comprehensive.connection.schema import Input
from util import Util

import logging


class TestConnection(TestCase):
    @patch("requests.Session.post", side_effect=Util.mocked_requests)
    def test_connection_success(self, mock_post):
        """Test successful connection."""
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://cloud.gravityzone.bitdefender.com",
            Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
        }
        connection.connect(params)
        result = connection.test()
        self.assertEqual(result, {"success": True})

    @patch("requests.Session.post")
    def test_connection_failure(self, mock_post):
        """Test connection failure raises ConnectionTestException."""
        from requests.exceptions import ConnectionError

        mock_post.side_effect = ConnectionError("Unable to connect")

        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://invalid.example.com",
            Input.API_KEY: {"secretKey": "invalid_key"},
        }
        connection.connect(params)

        with self.assertRaises(ConnectionTestException):
            connection.test()
