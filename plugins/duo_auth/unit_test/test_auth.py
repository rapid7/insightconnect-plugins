import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from komand_duo_auth.actions.auth import Auth
from komand_duo_auth.actions.auth.schema import Input, Output
from parameterized import parameterized

from utils import MockResponse, Util

STUB_PARAMETERS = {Input.USER_ID: "ExampleUserID"}


class TestAuth(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Auth())

    @parameterized.expand(
        [
            (
                STUB_PARAMETERS,
                "auth",
                {Output.RESULT: "allow", Output.STATUS: "allow", Output.STATUS_MSG: "Success. Logging you in..."},
            ),
            (
                {**STUB_PARAMETERS, Input.ASYNC: True},
                "auth_async",
                {Output.TXID: "45f7c92b-f45f-4862-8545-e0f58e78075a"},
            ),
            (
                {**STUB_PARAMETERS, Input.DEVICE: "1234567"},
                "auth_device",
                {
                    Output.RESULT: "allow",
                    Output.STATUS: "allow",
                    Output.STATUS_MSG: "Success. Logging you in...",
                    Output.TRUSTED_DEVICE_TOKEN: "REkxS00Ld4ddEVTRZOUlYMEldJ05HwUldRRThJR1VTNE0=|35|835c28ca9b042e05e",
                },
            ),
        ]
    )
    @patch("duo_client.client.Client.json_api_call")
    def test_auth(
        self,
        input_parameters: Dict[str, Any],
        response_filename: str,
        expected: Dict[str, Any],
        mock_request: MagicMock,
    ) -> None:
        mock_request.return_value = MockResponse(response_filename, 200).json()
        response = self.action.run(input_parameters)
        self.assertEqual(response, expected)
        mock_request.assert_called()

    @patch("duo_client.client.Client.json_api_call")
    def test_auth_error(self, mock_request: MagicMock) -> None:
        mock_request.side_effect = MockResponse
        with self.assertRaises(PluginException) as context:
            self.action.run(STUB_PARAMETERS)
        self.assertEqual(context.exception.preset, PluginException.Preset.UNKNOWN)
