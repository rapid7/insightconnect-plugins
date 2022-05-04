import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from komand_recorded_future.actions.lookup_url import LookupUrl
from komand_recorded_future.connection.schema import Input


@patch("requests.request", side_effect=Util.mock_request)
class TestLookupUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupUrl())

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_url_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_url_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_url_not_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_url_invalid_url_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_url_not_found.json.resp"),
            ],
        ]
    )
    def test_lookup_url(self, mock_request, input_parameters, expected):
        actual = self.action.run(input_parameters)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "bad_api_key",
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.API_KEY),
                PluginException.assistances.get(PluginException.Preset.API_KEY),
            ],
            [
                "unauthorized",
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                PluginException.assistances.get(PluginException.Preset.UNAUTHORIZED),
            ],
            [
                "unknown",
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNKNOWN),
                PluginException.assistances.get(PluginException.Preset.UNKNOWN),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.SERVER_ERROR),
                PluginException.assistances.get(PluginException.Preset.SERVER_ERROR),
            ],
            [
                "invalid_json",
                Util.read_file_to_dict("inputs/lookup_url_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.INVALID_JSON),
                PluginException.assistances.get(PluginException.Preset.INVALID_JSON),
            ],
        ]
    )
    def test_lookup_url_raise_exception(self, mock_request, token, input_parameters, cause, assistance):
        action = Util.default_connector(LookupUrl(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as e:
            action.run(input_parameters)

        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
