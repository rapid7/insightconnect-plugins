import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.passive_dns.action import PassiveDns
from komand_cisco_umbrella_investigate.actions.passive_dns.schema import Input, Output
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

STUB_PARAMS = {Input.NAME: "example", Input.RECORDTYPE: "A", Input.RESOURCE_RECORDS: "Domain"}
STUB_REPONSE = Util.read_file_to_dict("expected/test_passive_dns.json.exp")


class TestPassiveDns(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(PassiveDns())

    @parameterized.expand(
        [
            ("Domain", STUB_REPONSE),
            ("Timeline", {Output.TIMELINE_DATA: []}),
            ("Name", STUB_REPONSE),
            ("IP", STUB_REPONSE),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_passive_dns_ok(self, resource_records: str, expected_response: List[str], mock_get: Mock) -> None:
        response = self.action.run({**STUB_PARAMS, Input.RESOURCE_RECORDS: resource_records})
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_passive_dns_exception(self, mock_request: Mock, input_parameters: Dict[str, Any], exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, exception)
