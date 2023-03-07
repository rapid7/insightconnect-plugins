import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.connection.connection import Connection
from komand_cisco_umbrella_investigate.connection.schema import Input
from parameterized import parameterized

from unit_test.util import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mock_request_429,
    mock_request_500,
    mock_request_501,
    mock_request_503,
    mocked_request,
)


class TestConnection(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    @patch("requests.get", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get: Mock) -> None:
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @patch("requests.get", side_effect=mock_request_200)
    def test_connection_not_uuid(self, mock_get: Mock) -> None:
        self.connection.connect(
            {
                Input.API_KEY: {"secretKey": "not-uuid4"},
            }
        )
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(context.exception.cause, "Invalid API key.")
        self.assertEqual(
            context.exception.assistance,
            "The API key is a UUID-v4 key. For more information, see: https://developer.cisco.com/docs/cloud-security/#!umbrella-legacy-authentication/prerequisites",
        )

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_501, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_503, PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE]),
        ],
    )
    def test_connection_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
