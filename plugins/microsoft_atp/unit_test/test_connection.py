import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_microsoft_atp.connection.connection import Connection
from parameterized import parameterized

from unit_test.util import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestConnection(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    @patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get: Mock) -> None:
        response = self.connection.test()
        expected_response = {"status": True}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
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
