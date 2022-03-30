import os
import sys


sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.util.tools import Message

from unit_test.mock import (
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_400,
    mock_request_403,
    mock_request_409,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mocked_request,
    STUB_CONNECTION,
)


class TestConnection(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    def test_connection_ok(self):
        mocked_request(mock_request_200)
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_409, Message.CONFLICTED_STATE_OF_OBJECT_MESSAGE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
        ],
    )
    @mock.patch("icon_microsoft_log_analytics.util.tools.backoff_function", return_value=0)
    def test_connection_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
