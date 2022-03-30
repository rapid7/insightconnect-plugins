import os
import sys
from unittest import TestCase

import mock
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_urlscan.actions import GetScanResults
from komand_urlscan.actions.get_scan_results.schema import Input
from unit_test.util import Util


@mock.patch("requests.get", side_effect=Util.mocked_requests_post)
class TestGetScanResults(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetScanResults())

    def test_get_scan_results(self, mock_post):
        actual = self.action.run({Input.SCAN_ID: "full_objects"})
        expected = Util.load_json("payloads/get_scan_results.json.exp")

        self.assertEqual(actual, expected)

    def test_get_scan_results_empty(self, mock_post):
        actual = self.action.run({Input.SCAN_ID: "empty"})
        expected = Util.load_json("payloads/get_scan_results_empty_object.json.exp")

        self.assertEqual(actual, expected)

    def test_get_scan_results_404(self, mock_post):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.SCAN_ID: "404"})

        self.assertEqual("The requested scan results were not found.", context.exception.cause)
        self.assertEqual(
            "If you are running this action directly after a new scan, you may need to add a delay to ensure the scan results are available when they are requested (typically ~5-10 seconds is sufficient.",
            context.exception.assistance,
        )
