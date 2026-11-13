import logging
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)

from icon_luminar.connection.connection import Connection
from icon_luminar.util.api import LuminarManager


class TestConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @mock.patch.object(LuminarManager, "access_token", return_value="fake-token")
    def test_connection_success(self, mock_access_token: mock.Mock):
        """Test successful connection when access_token is returned"""
        params = {
            "base_url": "https://example.com",
            "account_id": "test-account",
            "client_id": "test-client",
            "client_secret": {"secretKey": "secret"},
        }
        self.connection.connect(params)
        result = self.connection.test()
        self.assertEqual(result, {"success": True})
        mock_access_token.assert_called_once()

    @mock.patch.object(
        LuminarManager,
        "access_token",
        side_effect=PluginException(preset=PluginException.Preset.API_KEY),
    )
    def test_connection_failure(self, mock_access_token: mock.Mock):
        """Test connection failure when PluginException is raised"""
        params = {
            "base_url": "https://example.com",
            "account_id": "test-account",
            "client_id": "test-client",
            "client_secret": {"secretKey": "secret"},
        }
        self.connection.connect(params)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.API_KEY],
        )
