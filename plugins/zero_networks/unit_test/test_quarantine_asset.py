import json
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

import requests
from parameterized import parameterized

from icon_zero_networks.actions.quarantine_asset import QuarantineAsset
from icon_zero_networks.actions.quarantine_asset.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import APIException, PluginException

from util import BASE_URL, Util


class TestQuarantineAsset(TestCase):
    def setUp(self):
        self.action = QuarantineAsset()
        Util.default_connector(self.action)

    @parameterized.expand([("quarantine", True), ("release", False)])
    def test_quarantine_asset_sends_the_requested_state(self, _test_name, quarantine):
        send, sent = Util.mock_send(200, {})
        with patch.object(requests.Session, "send", send):
            actual = self.action.run({Input.ASSET_ID: "a:a:JF2xro6g", Input.QUARANTINE: quarantine})

        self.assertEqual({Output.SUCCESS: True}, actual)
        self.assertEqual("PUT", sent[0].method)
        self.assertEqual(f"{BASE_URL}/assets/a:a:JF2xro6g/actions/quarantine", sent[0].url)
        self.assertEqual({"quarantine": quarantine}, json.loads(sent[0].body))

    def test_quarantine_asset_trims_whitespace_from_the_asset_id(self):
        send, sent = Util.mock_send(200, {})
        with patch.object(requests.Session, "send", send):
            self.action.run({Input.ASSET_ID: " a:a:JF2xro6g ", Input.QUARANTINE: True})

        self.assertEqual(f"{BASE_URL}/assets/a:a:JF2xro6g/actions/quarantine", sent[0].url)

    def test_quarantine_asset_accepts_an_empty_response_body(self):
        send, _sent = Util.mock_send(200, None)
        with patch.object(requests.Session, "send", send):
            actual = self.action.run({Input.ASSET_ID: "a:a:JF2xro6g", Input.QUARANTINE: True})

        self.assertEqual({Output.SUCCESS: True}, actual)

    @parameterized.expand([("blank", "   "), ("empty", ""), ("none", None)])
    def test_quarantine_asset_rejects_a_missing_asset_id(self, _test_name, asset_id):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ASSET_ID: asset_id, Input.QUARANTINE: True})

        self.assertEqual("No asset ID was provided.", context.exception.cause)

    @parameterized.expand([("bad_request", 400), ("unauthorized", 401), ("not_found", 404)])
    def test_quarantine_asset_raises_on_api_errors(self, _test_name, status_code):
        send, _sent = Util.mock_send(status_code, {"error": "Error", "message": "failed"})
        with patch.object(requests.Session, "send", send):
            with self.assertRaises(APIException) as context:
                self.action.run({Input.ASSET_ID: "a:a:JF2xro6g", Input.QUARANTINE: True})

        self.assertEqual(status_code, context.exception.status_code)
