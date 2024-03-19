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

from icon_threatminer.actions.ssdeep_report import SsdeepReport
from icon_threatminer.actions.ssdeep_report.schema import Input, Output


class TestSsdeepReport(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SsdeepReport())

    @parameterized.expand(
        [
            (
                {Input.QUERY: "1536:TJsNrChuG2K6IVOTjWko8a9P6W3OEHBQc4w4:TJs0oG2KSTj3o8a9PFeEHn4l"},
                {
                    "status_code": 200,
                    "status_message": "Results found.",
                    "results": [
                        {
                            "hash": "3:6QKm2A3T:6QKm2A3T",
                            "similarity": "97",
                            "matches": [
                                {"file_name": "file1.exe", "file_size": "1536", "ssdeep_hash": "3:6QKm2A3T:6QKm2A3T"},
                                {"file_name": "file2.exe", "file_size": "1536", "ssdeep_hash": "3:6QKm2A3T:6QKm2A3T"},
                            ],
                        }
                    ],
                },
            )
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_ssdeep_report(
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
    def test_ssdeep_report_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
