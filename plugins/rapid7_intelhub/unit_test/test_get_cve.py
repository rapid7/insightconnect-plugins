import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_intelhub.actions.get_cve import GetCve
from komand_rapid7_intelhub.actions.get_cve.schema import Input, Output
from parameterized import parameterized

from util import (
    STUB_CVE_ID,
    STUB_CVE_ID_WITHOUT_RAPID7_CONTENT,
    STUB_UNAUTHORIZED_CONNECTION,
    STUB_UNKNOWN_CVE_ID,
    STUB_UNLICENSED_CONNECTION,
    Util,
)


class TestGetCve(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetCve())

    @parameterized.expand(
        [
            ["with_rapid7_content", STUB_CVE_ID, Util.read_file_to_dict("expected/get_cve.json.exp")],
            [
                "without_rapid7_content",
                STUB_CVE_ID_WITHOUT_RAPID7_CONTENT,
                Util.read_file_to_dict("expected/get_cve_without_rapid7_content.json.exp"),
            ],
            ["not_found", STUB_UNKNOWN_CVE_ID, {Output.CVE: {}, Output.FOUND: False}],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve(self, _name: str, cve_id: str, expected: dict, mock_request: MagicMock) -> None:
        input_params = {Input.CVE_ID: cve_id}
        validate(input_params, self.action.input.schema)
        response = self.action.run(input_params)
        validate(response, self.action.output.schema)
        self.assertEqual(expected, response)

    @parameterized.expand(
        [
            ["unauthorized", STUB_UNAUTHORIZED_CONNECTION, "unauthorized", "Unauthorized"],
            ["license_not_found", STUB_UNLICENSED_CONNECTION, "license_not_found", "Product license not found."],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_cve_raise_exception(
        self, _name: str, connection_params: dict, payload: str, cause: str, mock_request: MagicMock
    ) -> None:
        action = Util.default_connector(GetCve(), connection_params)
        with self.assertRaises(PluginException) as context:
            action.run({Input.CVE_ID: STUB_CVE_ID})
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(Util.read_file_to_string(f"payloads/{payload}.json.resp"), context.exception.data)
