import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from icon_rapid7_insightvm_cloud.actions.stop_scan import StopScan
from icon_rapid7_insightvm_cloud.actions.stop_scan.schema import Input

from unittest.mock import patch
from unit_test.utils import Utils
from unit_test.mock import (
    mock_request,
)


class TestStopScan(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "scan_id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
            "scan_id_invalid": "invalid scan id",
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(StopScan())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_stop_scan(self, _mock_req):
        actual = self.action.run({Input.ID: self.params.get("scan_id")})
        expected = Utils.read_file_to_dict("expected_responses/stop_scan.json.resp")
        self.assertEqual(expected, actual)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_stop_scan_invalid_scan_id(self, _mock_req):
        actual = self.action.run({Input.ID: self.params.get("scan_id_invalid")})
        expected = Utils.read_file_to_dict("expected_responses/stop_scan_invalid_scan_id.json.resp")
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=mock_request)
    def test_stop_scan_invalid_secret_key(self, _mock_req):
        self.connection, self.action = Utils.default_connector(
            StopScan(), {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_invalid"}}
        )
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ID: self.params.get("scan_id")})
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/scan/{self.params.get('scan_id')}/stop'"
        assistance = "Unauthorized"
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_server_error(self, _mock_req):
        self.connection, self.action = Utils.default_connector(
            StopScan(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_server_error"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ID: self.params.get("scan_id")})
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/scan/{self.params.get('scan_id')}/stop'"
        assistance = "An unexpected error occurred. Please contact Rapid7 support."
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
