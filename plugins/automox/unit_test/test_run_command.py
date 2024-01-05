import sys
import os

sys.path.append(os.path.abspath('../'))

from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from util import (
    Util,
    mock_request_204,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
    ORG_ID,
    DEVICE_ID,
    POLICY_ID
)

from icon_automox.actions.run_command import RunCommand
from icon_automox.actions.run_command.schema import Input, Output


class TestRunCommand(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(RunCommand())
        self.params = {
            Input.ORG_ID: ORG_ID,
            Input.COMMAND: "GetOS",
            Input.DEVICE_ID: DEVICE_ID,
            Input.PATCHES: [1234],
            Input.POLICY_ID: POLICY_ID,
            }

    @patch("requests.Session.request", side_effect=mock_request_204)
    def test_run_command_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        expected_response = {
            Output.SUCCESS: True,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_200_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
        ],
    )
    def test_run_command_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
