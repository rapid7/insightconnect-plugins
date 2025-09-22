import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_rapid7_insightvm_cloud.actions.get_asset import GetAsset
from icon_rapid7_insightvm_cloud.actions.get_asset.schema import GetAssetOutput, Input
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from jsonschema import validate

from mock import mock_request
from utils import Utils


class TestGetAsset(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "asset_id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
            "asset_id_bad": "5058b0b4-701a-414e-9630-430d2cddbf4e",
            "include_vulns_false": False,
            "include_vulns_true": True,
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(GetAsset())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_include_vulns_false(self, _mock_req: MagicMock) -> None:
        actual = self.action.run(
            {Input.ID: self.params.get("asset_id"), Input.INCLUDE_VULNS: self.params.get("include_vulns_false")}
        )
        expected = Utils.read_file_to_dict("expected_responses/get_asset.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, GetAssetOutput.schema)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_include_vulns_true(self, _mock_req: MagicMock) -> None:
        actual = self.action.run(
            {Input.ID: self.params.get("asset_id"), Input.INCLUDE_VULNS: self.params.get("include_vulns_true")}
        )
        expected = Utils.read_file_to_dict("expected_responses/get_asset_include_vulns.json.resp")
        self.assertEqual(expected, actual)
        validate(actual, GetAssetOutput.schema)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_not_found(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {Input.ID: self.params.get("asset_id_bad"), Input.INCLUDE_VULNS: self.params.get("include_vulns_false")}
            )
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets/{self.params.get('asset_id_bad')}'"
        assistance = "The requested resource does not exist."
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_not_found_include_vulns(self, _mock_req: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {Input.ID: self.params.get("asset_id_bad"), Input.INCLUDE_VULNS: self.params.get("include_vulns_true")}
            )
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets/{self.params.get('asset_id_bad')}'"
        assistance = "The requested resource does not exist."
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_invalid_secret_key(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            GetAsset(), {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_invalid"}}
        )
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {Input.ID: self.params.get("asset_id"), Input.INCLUDE_VULNS: self.params.get("include_vulns_false")}
            )
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets/{self.params.get('asset_id')}'"
        assistance = "Unauthorized"
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)

    @patch("requests.request", side_effect=mock_request)
    def test_asset_search_server_error(self, _mock_req: MagicMock) -> None:
        self.connection, self.action = Utils.default_connector(
            GetAsset(),
            {ConnectionInput.REGION: "us", ConnectionInput.CREDENTIALS: {"secretKey": "secret_key_server_error"}},
        )
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {Input.ID: self.params.get("asset_id"), Input.INCLUDE_VULNS: self.params.get("include_vulns_false")}
            )
        cause = f"Failed to get a valid response from InsightVM at endpoint 'https://us.api.insight.rapid7.com/vm/v4/integration/assets/{self.params.get('asset_id')}'"
        assistance = "An unexpected error occurred. Please contact Rapid7 support."
        self.assertIn(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
