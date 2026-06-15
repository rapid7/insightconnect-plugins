import sys
import os
import json

sys.path.append(os.path.abspath("../"))

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

    @patch("requests.Session.request", side_effect=mock_request_200)
    def test_multi_chunk(self, mock: Mock) -> None:
        devices = [{"id": f"ext-{i}", "cves": ["CVE-2019-9894"]} for i in range(250)]
        self.params[Input.DEVICES_JSON] = json.dumps(devices)
        response = self.action.run(self.params)
        self.assertEqual(response[Output.TOTAL_DEVICES], 250)
        self.assertEqual(response[Output.CHUNKS_SENT], 3)
        self.assertEqual(len(response[Output.RESPONSES]), 3)
        # Verify 1 GET org + 3 POST calls were made
        self.assertEqual(mock.call_count, 4)

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
