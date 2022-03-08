import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from parameterized import parameterized

from icon_netskope.connection.connection import Connection
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200_connection,
    mock_request_401_connection,
    mock_request_403_connection,
    mock_request_429_connection,
    mock_request_500_connection,
    mock_request_503_connection,
    mock_request_512_connection,
    mocked_request,
)


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    def test_connection_ok(self):
        mocked_request(mock_request_200_connection)
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_401_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_429_connection, PluginException.Preset.RATE_LIMIT),
            (mock_request_500_connection, PluginException.Preset.UNKNOWN),
            (mock_request_512_connection, PluginException.Preset.RATE_LIMIT),
        ],
    )
    def test_connection_exception(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )

    @parameterized.expand(
        [
            (mock_request_401_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_429_connection, PluginException.Preset.RATE_LIMIT),
            (mock_request_500_connection, PluginException.Preset.UNKNOWN),
            (mock_request_503_connection, PluginException.Preset.RATE_LIMIT),
            (mock_request_512_connection, PluginException.Preset.RATE_LIMIT),
        ],
    )
    @mock.patch("icon_netskope.util.api.ApiClient._call_api_v1", return_value=True)
    def test_connection_exception_when_api_v2_rate_limiting(self, mock_request, exception, mock_method):
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
