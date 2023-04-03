import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.search.action import Search
from komand_cisco_umbrella_investigate.actions.search.schema import Input, Output
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

STUB_PARAMS = {
    Input.EXPRESSION: "example.com",
    Input.START: "-1days",
    Input.LIMIT: 0,
    Input.INCLUDE_CATEGORY: "",
}
STUB_RESPONSE = Util.read_file_to_dict("expected/test_search.json.exp")


class TestSearch(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(Search())

    @parameterized.expand(
        [
            (
                STUB_PARAMS,
                STUB_RESPONSE,
            ),
            ({**STUB_PARAMS, Input.START: "2sec"}, STUB_RESPONSE),
            ({**STUB_PARAMS, Input.START: "2min"}, STUB_RESPONSE),
            ({**STUB_PARAMS, Input.START: "2hour"}, STUB_RESPONSE),
            ({**STUB_PARAMS, Input.START: "2months"}, STUB_RESPONSE),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_search_ok(self, input_parameters: Dict[str, Any], expected_response: List[str], mock_get: Mock) -> None:
        response = self.action.run(input_parameters)
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_200, {**STUB_PARAMS, Input.START: "Test"}, "An invalid start time was provided."),
            (mock_request_403, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_search_exception(self, mock_request: Mock, input_parameters: Dict[str, Any], exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, exception)
