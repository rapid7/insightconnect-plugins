import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from komand_recorded_future.actions.lookup_domain import LookupDomain
from komand_recorded_future.connection.schema import Input


class TestLookupDomain(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupDomain())

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_domain_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_domain_found_with_http.json.resp"),
                Util.read_file_to_dict("expected/lookup_domain_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_domain_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_domain_not_found.json.resp"),
            ],
            [
                Util.read_file_to_dict("inputs/lookup_domain_invalid_domain_not_found.json.resp"),
                Util.read_file_to_dict("expected/lookup_domain_not_found.json.resp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_lookup_domain(self, input_parameters, expected, mock_request):
        actual = self.action.run(input_parameters)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        (
            [
                ["www.google.com", "www.google.com"],
                ["google.gs", "google.gs"],
                ["http://google.gs", "google.gs"],
                ["https://google.gs", "google.gs"],
                ["https://www.example.com/path/to/file", "www.example.com"],
            ]
        )
    )
    def test_get_domain(self, input_url, expected_url):
        actual = self.action.get_domain(input_url)
        self.assertEqual(actual, expected_url)

    @parameterized.expand(
        [
            [
                "bad_api_key",
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.API_KEY),
                PluginException.assistances.get(PluginException.Preset.API_KEY),
            ],
            [
                "unauthorized",
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNAUTHORIZED),
                PluginException.assistances.get(PluginException.Preset.UNAUTHORIZED),
            ],
            [
                "unknown",
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.UNKNOWN),
                PluginException.assistances.get(PluginException.Preset.UNKNOWN),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.SERVER_ERROR),
                PluginException.assistances.get(PluginException.Preset.SERVER_ERROR),
            ],
            [
                "invalid_json",
                Util.read_file_to_dict("inputs/lookup_domain_found.json.resp"),
                PluginException.causes.get(PluginException.Preset.INVALID_JSON),
                PluginException.assistances.get(PluginException.Preset.INVALID_JSON),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_lookup_domain_raise_exception(self, token, input_parameters, cause, assistance, mock_request):
        action = Util.default_connector(LookupDomain(), {Input.API_KEY: {"secretKey": token}})
        with self.assertRaises(PluginException) as e:
            action.run(input_parameters)

        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
