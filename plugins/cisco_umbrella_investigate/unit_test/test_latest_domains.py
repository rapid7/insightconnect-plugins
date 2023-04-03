import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.latest_domains.action import LatestDomains
from komand_cisco_umbrella_investigate.actions.latest_domains.schema import Input, Output
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

STUB_PARAMS = {Input.IP: "192.168.0.1"}
STUB_RESPONSE = Util.read_file_to_dict("expected/test_latest_domains.json.exp")


class TestLatestDomains(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(LatestDomains())

    @parameterized.expand(
        [
            (
                "192.168.0.1",
                STUB_RESPONSE,
            ),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_latest_domains_ok(self, ip_address: str, expected_response: List[str], mock_get: Mock) -> None:
        response = self.action.run({Input.IP: ip_address})
        expected_response = {Output.DOMAINS: expected_response}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_200, {Input.IP: "invalid_ip"}, "Invalid IP provided by user."),
            (mock_request_403, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_latest_domains_exception(
        self, mock_request: Mock, input_parameters: Dict[str, Any], exception: str
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
