import sys
import os
import json
from typing import Any

sys.path.append(os.path.abspath("../"))

from jsonschema import validate
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from util import (
    Util,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mocked_request,
    mock_request_200_invalid_json,
)

from icon_automox.actions.submit_remediation import SubmitRemediation
from icon_automox.actions.submit_remediation.schema import Input, Output

ORG_ID = 1234


class TestSubmitRemediation(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SubmitRemediation())
        self.single_device = [
            {"id": "ext-1", "mac_address": "00:1c:42:e9:10:ab", "cves": ["CVE-2019-9894"]},
        ]
        self.params = {
            Input.ORG_ID: ORG_ID,
            Input.ACTION_TYPE: "match",
            Input.DEVICES_JSON: json.dumps(self.single_device),
        }

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_single_chunk_ok(self, mock: Mock) -> None:
        response = self.action.run(self.params)
        self.assertEqual(response[Output.TOTAL_DEVICES], 1)
        self.assertEqual(response[Output.CHUNKS_SENT], 1)
        self.assertIsInstance(response[Output.BATCH_UUID], str)
        self.assertEqual(len(response[Output.RESPONSES]), 1)

    @parameterized.expand(
        [
            # 250 devices with one CVE each
            ("many_devices", [{"id": f"ext-{number}", "cves": ["CVE-2019-9894"]} for number in range(250)], 250, 3),
            # 100 devices, two of them split into 4 and 3 entries for having more than 500 CVEs, so 105 entries
            # The first big device sits at entries 97 to 100, so its entries straddle both chunks
            (
                "devices_split_by_cves",
                [{"id": f"ext-{number}", "cves": ["CVE-2019-9894"]} for number in range(97)]
                + [{"id": "ext-big-1", "cves": [f"CVE-2026-{cve}" for cve in range(1786)]}]
                + [{"id": "ext-big-2", "cves": [f"CVE-2026-{cve}" for cve in range(1188)]}]
                + [{"id": "ext-97", "cves": ["CVE-2019-9894"]}],
                100,
                2,
            ),
        ],
    )
    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_multi_chunk(
        self, _name: str, devices: list[dict[str, Any]], total_devices: int, chunks: int, mock: Mock
    ) -> None:
        self.params[Input.DEVICES_JSON] = json.dumps(devices)
        response = self.action.run(self.params)
        validate(response, self.action.output.schema)
        self.assertEqual(response[Output.TOTAL_DEVICES], total_devices)
        self.assertEqual(response[Output.CHUNKS_SENT], chunks)
        self.assertEqual(len(response[Output.RESPONSES]), chunks)
        # Verify 1 GET org + one POST per chunk were made
        self.assertEqual(mock.call_count, chunks + 1)

        # Automox refuses a batch_uuid it has already seen, so each chunk must carry its own
        batch_uuids = [call.kwargs.get("json", {}).get("batch_uuid") for call in mock.call_args_list[1:]]
        self.assertEqual(len(set(batch_uuids)), chunks)
        self.assertEqual(response[Output.BATCH_UUID], batch_uuids[0])

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_exactly_100_devices(self, mock: Mock) -> None:
        devices = [{"id": f"ext-{i}", "cves": ["CVE-2019-9894"]} for i in range(100)]
        self.params[Input.DEVICES_JSON] = json.dumps(devices)
        response = self.action.run(self.params)
        self.assertEqual(response[Output.CHUNKS_SENT], 1)
        # 1 GET org + 1 POST remediate
        self.assertEqual(mock.call_count, 2)

    @parameterized.expand(
        [
            ("invalid_json_string", "not valid json", "preset", PluginException.Preset.INVALID_JSON),
            ("empty_device_list", "[]", "cause", "Invalid input"),
            ("missing_cves", json.dumps([{"id": "ext-1"}]), "cause", "Invalid input"),
        ],
    )
    def test_invalid_devices_input(self, _name: str, devices_json: str, attr: str, expected: object) -> None:
        self.params[Input.DEVICES_JSON] = devices_json
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(getattr(context.exception, attr), expected)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    def test_api_error_propagation(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
