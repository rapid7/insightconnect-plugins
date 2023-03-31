import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase
from unittest.mock import Mock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from komand_cisco_umbrella_investigate.actions.sample_samples.action import SampleSamples
from komand_cisco_umbrella_investigate.actions.sample_samples.schema import Input, Output
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

STUB_PARAMS = {Input.HASH: "ExampleHash", Input.LIMIT: 0, Input.OFFSET: 0}
STUB_RESPONSE = Util.read_file_to_dict("expected/test_sample_samples.json.exp")


class TestSampleSamples(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_connection: Mock) -> None:
        self.action = Util.default_connector(SampleSamples())

    @parameterized.expand(
        [
            (STUB_PARAMS, STUB_RESPONSE),
        ]
    )
    @patch("requests.get", side_effect=mock_request_200)
    def test_sample_samples_ok(
        self, input_parameters: Dict[str, Any], expected_response: List[str], mock_get: Mock
    ) -> None:
        response = self.action.run(input_parameters)
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_200, {**STUB_PARAMS, Input.HASH: "ExampleHashError"}, "Unable to return artifact data."),
            (mock_request_403, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_429, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, STUB_PARAMS, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_sample_samples_exception(
        self, mock_request: Mock, input_parameters: Dict[str, Any], exception: str
    ) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, exception)
