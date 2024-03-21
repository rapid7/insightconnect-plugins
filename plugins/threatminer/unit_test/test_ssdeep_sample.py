import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from mock import mock_request_200, mock_request_500, mock_request_503, mocked_request
from parameterized import parameterized
from utils import Util

from icon_threatminer.actions.ssdeep_sample import SsdeepSample
from icon_threatminer.actions.ssdeep_sample.schema import Input, Output


class TestSsdeepSample(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SsdeepSample())

    @parameterized.expand(
        [
            (
                {Input.QUERY: "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"},
                {
                    "status_code": 200,
                    "status_message": "Results found.",
                    "results": [{"value": "ecc5943b5c2ec75065ba1bdb668bb0a2c63c0451be259dea47a902811b318c00"}],
                },
            )
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_ssdeep_sample(
        self, input_parameters: Dict[str, Any], expected: Dict[str, Any], mock_requests: MagicMock
    ) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.RESPONSE: expected})
        mock_requests.assert_called()

    @parameterized.expand(
        [
            (
                mock_request_500,
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ),
            (
                mock_request_503,
                PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE],
                PluginException.assistances[PluginException.Preset.SERVICE_UNAVAILABLE],
            ),
        ]
    )
    def test_ssdeep_sample_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
