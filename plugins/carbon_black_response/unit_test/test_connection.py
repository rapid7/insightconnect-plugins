import sys
import os
from parameterized import parameterized
from unittest import TestCase, mock
from icon_carbon_black_response.connection.connection import Connection
from icon_carbon_black_response.actions.uninstall_sensor import UninstallSensor
from icon_carbon_black_response.actions.uninstall_sensor.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import logging
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_204,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    mocked_request,
    STUB_SENSOR_ID,
    STUB_SENSOR_RESPONSE
)

sys.path.append(os.path.abspath("../"))


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get):
        response = self.connection.test()
        expected_response = True
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
