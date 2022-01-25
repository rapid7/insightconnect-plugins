import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_opsgenie.connection.connection import Connection
from icon_opsgenie.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from unit_test.mock import mock_request_200, mock_request_403, mock_request_404, mock_request_500, mocked_request


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.API_KEY: {"secretKey": "1234567e-123c-123c-123c-1234567e9xAd"}})

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get):
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.NOT_FOUND),
            (mock_request_500, PluginException.Preset.UNKNOWN),
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
