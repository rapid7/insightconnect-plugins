import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from icon_darktrace.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from mock import STUB_CONNECTION, mock_request_200, mock_request_403


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mocked_request: mock.Mock) -> None:
        expected = {"success": True}
        self.assertEqual(self.connection.test(), expected)

    @mock.patch("requests.request", side_effect=mock_request_403)
    def test_connection_error(self, mocked_request: mock.Mock) -> None:
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[PluginException.Preset.API_KEY],
        )
