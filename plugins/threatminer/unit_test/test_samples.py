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

from icon_threatminer.actions.samples import Samples
from icon_threatminer.actions.samples.schema import Input, Output

STUB_INPUT_PARAMETERS = {
    Input.QUERY: "9de5069c5afe602b2ea0a04b66beb2c0",
    Input.QUERY_TYPE: "Metadata",
}
STUB_EXPECTED_OUTPUT = {
    "status_code": 200,
    "status_message": "Results found.",
    "results": [
        {
            "md5": "e6ff1bf0821f00384cdd25efb9b1cc09",
            "sha1": "16fd388151c0e73b074faa33698b9afc5c024b59",
            "sha256": "555b3689dec6ad888348c595426d112d041de5c989d4929284594d1e09f3d85f",
            "sha512": "7be8545c03f26192feb6eaf361b78b91966de28d2917ba1902508ad8589e0f0df748e82a265513f0426b50fedfda8fa6947c8b9e511b5d9a771ab20dc748367b",
            "ssdeep": "3072:HcRtvDzzrup4skvknm+GytbPlIyWYmxHznEt3xnDn1iyG6mb2LoUEb:HEtvD7MkvVIpPlIjYQjQ3NMV1AtE",
            "imphash": "dc73a9bd8de0fd640549c85ac4089b87",
            "file_type": "PE32 executable (GUI) Intel 80386, for MS Windows",
            "architecture": "32 Bit",
            "authentihash": "f3ec83f9862e9b09203a21ddac5ecdc4f874a591c2b03ffc4d9a5749e4655e28",
            "file_name": "installaware.15-patch.exe",
            "file_size": "546304 bytes",
            "date_analysed": "2016-03-13 03:46:38",
        }
    ],
}


class TestSamples(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Samples())

    @parameterized.expand(
        [
            (STUB_INPUT_PARAMETERS, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "HTTP Traffic"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Hosts"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Mutants"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Registry keys"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "AV detections"}, STUB_EXPECTED_OUTPUT),
            ({**STUB_INPUT_PARAMETERS, Input.QUERY_TYPE: "Report Tagging"}, STUB_EXPECTED_OUTPUT),
        ]
    )
    @patch("requests.request", side_effect=mock_request_200)
    def test_samples(
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
    def test_samples_exception(self, mock_request: Callable, cause: str, assistance: str) -> None:
        mocked_request(mock_request, "request")
        with self.assertRaises(PluginException) as context:
            self.action.run({})
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
