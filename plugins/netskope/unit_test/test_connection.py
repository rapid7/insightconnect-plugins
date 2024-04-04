import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_netskope.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from parameterized import parameterized

from mock import (
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

    @patch("requests.request", side_effect=mock_request_200_connection)
    def test_connection_ok(self, mock_request: MagicMock) -> None:
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)
        mock_request.assert_called()

    @parameterized.expand(
        [
            (mock_request_401_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_403_connection, PluginException.Preset.UNAUTHORIZED),
            (mock_request_429_connection, PluginException.Preset.RATE_LIMIT),
            (mock_request_500_connection, PluginException.Preset.UNKNOWN),
            (mock_request_512_connection, PluginException.Preset.RATE_LIMIT),
        ],
    )
    @patch("icon_netskope.util.utils.backoff_function", return_value=0)
    def test_connection_exception(
        self, mock_request: Callable, exception: str, mock_backoff_function: MagicMock
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
        mock_backoff_function.assert_called()

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
    @patch("icon_netskope.util.api.ApiClient._call_api_v1", return_value=True)
    @patch("icon_netskope.util.utils.backoff_function", return_value=0)
    def test_connection_exception_when_api_v2_rate_limiting(
        self, mock_request: Callable, exception: str, mock_method: MagicMock, mock_backoff_function: MagicMock
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
        mock_method.assert_called()
        mock_backoff_function.assert_called()
