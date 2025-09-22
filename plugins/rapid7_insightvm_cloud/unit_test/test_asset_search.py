import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_rapid7_insightvm_cloud.actions.asset_search import AssetSearch
from icon_rapid7_insightvm_cloud.actions.asset_search.schema import AssetSearchOutput, Input
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from jsonschema import validate

from mock import mock_request
from utils import Utils


class TestAssetSearch(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "asset_criteria": "last_scan_end > 2000-01-01T00:00:00.000Z",
            "asset_criteria_invalid": "invalid asset criteria",
            "size": 10,
            "sort_criteria": {"risk-score": "asc", "criticality-tag": "desc"},
            "vuln_criteria": "severity IN ['Critical', 'Severe']",
            "vuln_criteria_invalid": "invalid vuln criteria",
            "comparison_time": "2000-01-01T00:00:00.000Z",
            "current_time": "2000-01-01T00:00:00.000Z",
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(AssetSearch())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_all_inputs(self, _mock_req: MagicMock) -> None:
        actual = self.action.run(
            {
                Input.ASSET_CRITERIA: self.params.get("asset_criteria"),
                Input.SIZE: self.params.get("size"),
                Input.SORT_CRITERIA: self.params.get("sort_criteria"),
                Input.VULN_CRITERIA: self.params.get("vuln_criteria"),
            }
        )
        expected = Utils.read_file_to_dict("expected_responses/asset_search.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AssetSearchOutput.schema)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_no_input(self, _mock_req: MagicMock) -> None:
        actual = self.action.run()
        expected = Utils.read_file_to_dict("expected_responses/asset_search.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, AssetSearchOutput.schema)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_asset_invalid_asset_criteria(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_CRITERIA: self.params.get("asset_criteria_invalid"),
                    Input.SIZE: self.params.get("size"),
                    Input.SORT_CRITERIA: self.params.get("sort_criteria"),
                    Input.VULN_CRITERIA: self.params.get("vuln_criteria"),
                }
            )
        cause = "The server is unable to process the request."
        assistance = "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support."
        data = Utils.read_file_to_dict("expected_responses/asset_search_invalid_asset_criteria.json.resp")
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(str(data), context.exception.data)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_asset_vuln_criteria_invalid(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.ASSET_CRITERIA: self.params.get("asset_criteria"),
                    Input.SIZE: self.params.get("size"),
                    Input.SORT_CRITERIA: self.params.get("sort_criteria"),
                    Input.VULN_CRITERIA: self.params.get("vuln_criteria_invalid"),
                }
            )
        cause = "The server is unable to process the request."
        assistance = "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support."
        data = Utils.read_file_to_dict("expected_responses/asset_search_invalid_vuln_criteria.json.resp")
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(str(data), context.exception.data)

    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_invalid_secret_key(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            AssetSearch(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_invalid"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run()
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets'"
        assistance = "Unauthorized"
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_server_error(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            AssetSearch(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_server_error"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run()
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets'"
        assistance = "An unexpected error occurred. Please contact Rapid7 support."
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
