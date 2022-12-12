import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.actions.vuln_search import VulnSearch
from icon_rapid7_insightvm_cloud.actions.vuln_search.schema import Input
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from unittest.mock import patch
from unit_test.utils import Utils
from unit_test.mock import (
    mock_request,
)


class TestVulnSearch(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "asset_criteria": "last_scan_end > 2000-01-01T00:00:00.000Z",
            "asset_criteria_invalid": "invalid asset criteria",
            "size": 10,
            "sort_criteria": {"risk-score": "asc", "criticality-tag": "desc"},
            "vuln_criteria": "severity IN ['Critical', 'Severe']",
            "vuln_criteria_invalid": "invalid vuln criteria",
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(VulnSearch())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_vuln_search_all_inputs(self, _mock_req):
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

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_vuln_search_no_input(self, _mock_req):
        actual = self.action.run()
        expected = Utils.read_file_to_dict("expected_responses/asset_search.json.resp")
        self.assertEqual(expected, actual)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_vuln_invalid_asset_criteria(self, _mock_req):
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
        self.assertEqual(data, context.exception.data)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_asset_vuln_criteria_invalid(self, _mock_req):
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
        self.assertEqual(data, context.exception.data)

    @patch("requests.request", side_effect=mock_request)
    def test_vuln_search_invalid_secret_key(self, _mock_req):
        self.connection, self.action = Utils.default_connector(
            VulnSearch(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_invalid"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run()
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/vulnerabilities'"
        assistance = "Unauthorized"
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_vuln_search_server_error(self, _mock_req):
        self.connection, self.action = Utils.default_connector(
            VulnSearch(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_server_error"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run()
        cause = "Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/vulnerabilities'"
        assistance = "An unexpected error occurred. Please contact Rapid7 support."
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
