import sys
import os
from parameterized import parameterized
from unittest import TestCase, mock
from icon_carbon_black_response.connection.connection import Connection
from icon_carbon_black_response.actions.uninstall_sensor import UninstallSensor
from icon_carbon_black_response.actions.uninstall_sensor.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
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


class TestUninstallSensors(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = UninstallSensor()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {Input.ID: STUB_SENSOR_ID}

    @mock.patch("requests.request", side_effect=mock_request_204)
    def test_successful(self, mock_patch):
        response = self.action.run(self.params)
        expected_response = {}

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, "Bad request"),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR])
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
