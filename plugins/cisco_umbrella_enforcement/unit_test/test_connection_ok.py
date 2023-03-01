import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cisco_umbrella_enforcement.connection.connection import Connection
from komand_cisco_umbrella_enforcement.connection.schema import Input
import logging
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from unit_test.mock import (
    STUB_CONNECTION,
    mocked_request,
    mock_request_200_connection,
    mock_request_403_connection,
    mock_request_500_connection,
)


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.params = STUB_CONNECTION

    def test_connection_ok(self):
        mocked_request(mock_request_200_connection)
        response = self.connection.connect(self.params)
        expected_response = None
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_500_connection, PluginException.Preset.SERVER_ERROR),
        ],
    )
    def test_connection_exception(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(context.exception.cause, PluginException.causes[exception])
