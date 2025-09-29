import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_rapid7_insightvm_cloud.actions.start_scan import StartScan
from icon_rapid7_insightvm_cloud.actions.start_scan.schema import Input, StartScanOutput
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from jsonschema import validate

from mock import mock_request
from utils import Utils


class TestStartScan(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "asset_ids": ["5058b0b4-701a-414e-9630-430d2cddbf4d"],
            "asset_ids_invalid": ["invalid asset id"],
            "asset_ids_empty": [],
            "hostnames": ["example-host"],
            "hostnames_empty": [],
            "ips_empty": [],
            "ips": ["8.8.8.8"],
            "ips_invalid": ["invalid ip"],
            "name": "TestScan",
            "name_no_asset_ids": "TestScanNoAssetIDs",
            "name_invalid_asset_ids": "TestScanInvalidAssetIDs",
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(StartScan())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_start_scan(self, _mock_req: MagicMock) -> None:
        actual = self.action.run(
            {
                Input.ASSET_IDS: self.params.get("asset_ids"),
                Input.IPS: self.params.get("ips"),
                Input.NAME: self.params.get("name"),
                Input.HOSTNAMES: self.params.get("hostnames"),
            }
        )
        expected = Utils.read_file_to_dict("expected_responses/start_scan.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, StartScanOutput.schema)

    @patch("requests.request", side_effect=mock_request)
    def test_start_scan_invalid_asset_ids(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_IDS: self.params.get("asset_ids_invalid"),
                    Input.NAME: self.params.get("name_invalid_asset_ids"),
                }
            )
        assistance = "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support."
        cause = "The server is unable to process the request."
        data = Utils.read_file_to_dict("expected_responses/start_scan_invalid_asset_ids.json.resp")
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(str(data), context.exception.data)

    @patch("requests.request", side_effect=mock_request)
    def test_start_scan_no_asset_ids(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_IDS: self.params.get("asset_ids_empty"),
                    Input.NAME: self.params.get("name_no_asset_ids"),
                    Input.HOSTNAMES: self.params.get("hostnames"),
                    Input.IPS: self.params.get("ips"),
                }
            )
        assistance = "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support."
        cause = "The server is unable to process the request."
        data = Utils.read_file_to_dict("expected_responses/start_scan_invalid_asset_ids.json.resp")
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(str(data), context.exception.data)

    @patch("requests.request", side_effect=mock_request)
    def test_start_scan_invalid_ips(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_IDS: self.params.get("asset_ids_empty"),
                    Input.IPS: self.params.get("ips_invalid"),
                    Input.HOSTNAMES: self.params.get("hostnames"),
                    Input.NAME: self.params.get("name_invalid_asset_ids"),
                }
            )
        assistance = "Please enter only valid IP addresses."
        cause = "Invalid IP address provided."
        data = f"'{self.params.get('ips_invalid')[0]}' does not appear to be an IPv4 or IPv6 address"
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(data, context.exception.data)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_start_scan_required_input(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.NAME: self.params.get("name"),
                }
            )
        assistance = "Please enter asset ID, hostname, or IP address."
        cause = "Did not enter necessary information of what to scan."
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(cause, context.exception.cause)

    @patch("requests.request", side_effect=mock_request)
    def test_start_scan_invalid_secret_key(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            StartScan(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_invalid"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_IDS: self.params.get("asset_ids"),
                    Input.IPS: self.params.get("ips_empty"),
                    Input.NAME: self.params.get("name"),
                    Input.HOSTNAMES: self.params.get("hostnames_empty"),
                }
            )
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/scan'"
        assistance = "Unauthorized"
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_server_error(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            StartScan(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_server_error"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_IDS: self.params.get("asset_ids"),
                    Input.IPS: self.params.get("ips"),
                    Input.NAME: self.params.get("name"),
                    Input.HOSTNAMES: self.params.get("hostnames"),
                }
            )
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets'"
        assistance = "An unexpected error occurred. Please contact Rapid7 support."
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
