import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_vpndetection.connection.connection import Connection
from util import API_KEY, Util


@patch("requests.request", side_effect=Util.mock_request)
class TestConnection(TestCase):
    def connection(self, params: dict) -> Connection:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(params)
        return connection

    def test_keyless(self, mock_request: Mock) -> None:
        self.assertEqual({"success": True}, self.connection({}).test())

    def test_valid_key(self, mock_request: Mock) -> None:
        self.assertEqual({"success": True}, self.connection({"api_key": {"secretKey": API_KEY}}).test())

    def test_invalid_key(self, mock_request: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as context:
            self.connection({"api_key": {"secretKey": "wrong-key"}}).test()
        self.assertEqual(PluginException.causes[PluginException.Preset.API_KEY], context.exception.cause)
