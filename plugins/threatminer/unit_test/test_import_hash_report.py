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

from icon_threatminer.actions.import_hash_report import ImportHashReport
from icon_threatminer.actions.import_hash_report.schema import Input, Output


class TestImportHashReport(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ImportHashReport())

    @parameterized.expand(
        [
            (
                {Input.QUERY: "02699626f388ed830012e5b787640e71c56d42d8"},
                {
                    "status_code": 200,
                    "status_message": "Results found.",
                    "results": [
                        {
                            "hash": "e1faffd7f97e38b1d5c6f2bcbc7f5d3d",
                            "type": "MD5",
                            "first_seen": "2022-01-01 10:30:00",
                            "last_seen": "2022-01-05 14:45:00",
                            "samples": [
                                {"sample": "sample1.exe", "date": "2022-01-01", "source": "malware-database"},
                                {"sample": "sample2.exe", "date": "2022-01-02", "source": "malware-database"},
                            ],
                            "relationships": [
                                {"type": "Related IP", "value": "192.168.1.100"},
                                {"type": "Related Domain", "value": "example.com"},
                            ],
                        }
                    ],
                },
            ),
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_import_hash_report(
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
    def test_import_hash_report_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
