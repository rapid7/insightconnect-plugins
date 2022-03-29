import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from komand_recorded_future.actions.lookup_IP_address import LookupIPAddress
from komand_recorded_future.connection.schema import Input


@patch("requests.request", side_effect=Util.mock_request)
class TestLookupIP(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupIPAddress())

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
    def test_lookup_ip(self, mock_request, input_parameters, expected):
        actual = self.action.run(input_parameters)
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
    def test_lookup_ip_raise_exception(self, mock_request, token, input_parameters, cause, assistance):
        action = Util.default_connector(LookupIPAddress(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as e:
            action.run(input_parameters)

        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)