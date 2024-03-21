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

from icon_threatminer.actions.report import Report
from icon_threatminer.actions.report.schema import Input, Output

STUB_INPUT_PARAMETERS = {
    Input.FILENAME: "C5_APT_C2InTheFifthDomain.pdf",
    Input.QUERY_TYPE: "Domains",
    Input.YEAR: "2013",
}
STUB_EXPECTED_OUTPUT = {
    "status_code": 200,
    "status_message": "Results found.",
    "results": [{"value": "example.com"}, {"value": "example2.com"}],
}


class TestReport(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Report())

    @parameterized.expand(
        [
            (STUB_INPUT_PARAMETERS, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Hosts"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Emails"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Samples"}, STUB_EXPECTED_OUTPUT),
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_report(self, input_parameters: Dict[str, Any], expected: Dict[str, Any], mock_requests: MagicMock) -> None:
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
    def test_report_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
