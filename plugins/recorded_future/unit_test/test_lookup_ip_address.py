from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_recorded_future.actions.lookup_ip_address import LookupIpAddress
from komand_recorded_future.connection.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestLookupIpAddress(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupIpAddress())

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_ip_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_ip_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_ip_not_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_ip_invalid_ip_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_ip_not_found.json.resp"),
            ],
        ]
    )
    def test_lookup_ip(
        self, mock_request: MagicMock, input_parameters: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_parameters)
        validate(actual, self.action.output.schema)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "bad_api_key",
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.API_KEY),
                PluginException.assistances.get(PluginException.Preset.API_KEY),
            ],
            [
                "unauthorized",
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                PluginException.assistances.get(PluginException.Preset.UNAUTHORIZED),
            ],
            [
                "unknown",
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNKNOWN),
                PluginException.assistances.get(PluginException.Preset.UNKNOWN),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.SERVER_ERROR),
                PluginException.assistances.get(PluginException.Preset.SERVER_ERROR),
            ],
            [
                "invalid_json",
                Util.read_file_to_dict("inputs/lookup_ip_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.INVALID_JSON),
                PluginException.assistances.get(PluginException.Preset.INVALID_JSON),
            ],
        ]
    )
    def test_lookup_ip_raise_exception(
        self, mock_request: MagicMock, token: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        action = Util.default_connector(LookupIpAddress(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as error:
            action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
