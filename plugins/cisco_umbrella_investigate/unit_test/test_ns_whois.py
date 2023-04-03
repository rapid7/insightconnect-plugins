import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.ns_whois.action import NsWhois
from komand_cisco_umbrella_investigate.actions.ns_whois.schema import Input, Output
from parameterized import parameterized

from unit_test.util import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mock_request_429,
    mock_request_500,
    mocked_request,
)

STUB_PARAMS = {Input.NAMESERVER: "example"}
STUB_RESPONSE = Util.read_file_to_dict("expected/test_ns_whois.json.exp")


class TestNsWhois(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(NsWhois())

    @parameterized.expand(
        [
            ("example", STUB_RESPONSE),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_ns_whois_ok(self, nameserver: str, expected_response: List[str], mock_get: Mock) -> None:
        response = self.action.run({Input.NAMESERVER: nameserver})
        expected_response = {Output.DOMAIN: expected_response}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_200, {Input.NAMESERVER: "invalid_nameserver"}, "Invalid nameserver."),
            (mock_request_403, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_ns_whois_exception(self, mock_request: Mock, input_parameters: Dict[str, Any], exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, exception)
