import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.actions.get_asset import GetAsset
from icon_rapid7_insightvm_cloud.actions.get_asset.schema import Input
import logging
from unittest.mock import patch
from unit_test.utils import Utils
from unit_test.mock import (
    mock_request,
)


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
    def test_get_asset_include_vulns_false(self, _mock_req):
        actual = self.action.run({
            Input.ID: self.params.get("asset_id"),
            Input.INCLUDE_VULNS: self.params.get("include_vulns_false")
        })
        expected = Utils.read_file_to_dict("payloads/get_asset.json.resp").get("expected")
        self.assertEqual(expected, actual)

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_get_asset_include_vulns_true(self, _mock_req):
        actual = self.action.run({
            Input.ID: self.params.get("asset_id"),
            Input.INCLUDE_VULNS: self.params.get("include_vulns_true")
        })
        expected = Utils.read_file_to_dict("expected_responses/get_asset.json.resp")
        self.assertEqual(actual, expected)
