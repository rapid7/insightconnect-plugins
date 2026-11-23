import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import requests
from parameterized import parameterized

from icon_zero_networks.actions.search_asset import SearchAsset
from icon_zero_networks.actions.search_asset.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import APIException, PluginException

from util import BASE_URL, Util


class TestSearchAsset(TestCase):
    def setUp(self):
        self.action = SearchAsset()
        Util.default_connector(self.action)

    def test_search_asset_returns_matching_asset_id(self):
        send, sent = Util.mock_send(200, {"assetId": "a:a:JF2xro6g"})
        with patch.object(requests.Session, "send", send):
            actual = self.action.run({Input.FQDN: "server.domain.local"})

        self.assertEqual({Output.FOUND: True, Output.ASSET_ID: "a:a:JF2xro6g"}, actual)
        self.assertEqual(f"{BASE_URL}/assets/searchId?fqdn=server.domain.local", sent[0].url)
        self.assertEqual("GET", sent[0].method)
        self.assertEqual("9de5069c5afe602b2ea0a04b66beb2c0", sent[0].headers.get("Authorization"))

    def test_search_asset_trims_whitespace_from_the_fqdn(self):
        send, sent = Util.mock_send(200, {"assetId": "a:a:JF2xro6g"})
        with patch.object(requests.Session, "send", send):
            self.action.run({Input.FQDN: "  server.domain.local  "})

        self.assertEqual(f"{BASE_URL}/assets/searchId?fqdn=server.domain.local", sent[0].url)

    @parameterized.expand(
        [
            ("empty_object", 200, {}),
            ("null_asset_id", 200, {"assetId": None}),
            ("empty_asset_id", 200, {"assetId": ""}),
            ("not_found", 404, {"error": "NotFound", "message": "asset not found"}),
        ]
    )
    def test_search_asset_reports_not_found(self, _test_name, status_code, body):
        send, _sent = Util.mock_send(status_code, body)
        with patch.object(requests.Session, "send", send):
            actual = self.action.run({Input.FQDN: "missing.domain.local"})

        self.assertEqual({Output.FOUND: False, Output.ASSET_ID: ""}, actual)

    @parameterized.expand([("blank", "   "), ("empty", ""), ("none", None)])
    def test_search_asset_rejects_a_missing_fqdn(self, _test_name, fqdn):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.FQDN: fqdn})

        self.assertEqual("No fully qualified domain name was provided.", context.exception.cause)

    @parameterized.expand([("unauthorized", 401), ("forbidden", 403), ("server_error", 500)])
    def test_search_asset_raises_on_api_errors(self, _test_name, status_code):
        send, _sent = Util.mock_send(status_code, {"error": "Error", "message": "failed"})
        with patch.object(requests.Session, "send", send):
            with self.assertRaises(APIException) as context:
                self.action.run({Input.FQDN: "server.domain.local"})

        self.assertEqual(status_code, context.exception.status_code)
