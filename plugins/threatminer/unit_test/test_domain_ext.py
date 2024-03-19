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

from icon_threatminer.actions.domain_ext import DomainExt
from icon_threatminer.actions.domain_ext.schema import Input, Output

STUB_INPUT_PARAMETERS = {Input.DOMAIN: "ExampleDomain", Input.QUERY_TYPE: "Related Samples"}
STUB_EXPECTED_OUTPUT = {
    "status_code": 200,
    "status_message": "Results found.",
    "results": [{"domain": "example.com", "subdomains": ["sub1.example.com", "sub2.example.com", "sub3.example.com"]}],
}


class TestDomainExt(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DomainExt())

    @parameterized.expand(
        [
            (STUB_INPUT_PARAMETERS, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Subdomains"}, STUB_EXPECTED_OUTPUT),
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_domain_ext(
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
    def test_domain_ext_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
