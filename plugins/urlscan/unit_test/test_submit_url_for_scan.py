import os
import sys

import mock

from unittest import TestCase
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from unit_test.util import Util
from komand_urlscan.actions.submit_url_for_scan import SubmitUrlForScan



@mock.patch("requests.post", side_effect=Util.mocked_requests_post)
class TestSubmitUrlForScan(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitUrlForScan())

    def test_submit_url_for_scan(self, mock_post):
        actual = self.action.run({"public": True, "url": "test"})
        expected = {"was_scan_skipped": False, "scan_id": "123"}

        self.assertEqual(actual, expected)

    def test_submit_url_for_scan_201(self, mock_post):
        actual = self.action.run({"public": False, "url": "201"})
        expected = {"was_scan_skipped": True, "scan_id": ""}

        self.assertEqual(actual, expected)

    def test_submit_url_for_scan_401(self, mock_post):
        with self.assertRaises(PluginException) as error:
            self.action.run({"public": True, "url": "401"})

        self.assertTrue("Invalid API key provided" in error.exception.cause)
        self.assertTrue("Verify your API key configured in your connection is correct" in error.exception.assistance)

    def test_submit_url_for_scan_429(self, mock_post):
        with self.assertRaises(PluginException) as error:
            self.action.run({"public": False, "url": "429"})

        self.assertTrue("API limit error." in error.exception.cause)

    def test_submit_url_for_scan_unexpect(self, mock_post):
        with self.assertRaises(PluginException) as error:
            self.action.run({"public": True, "url": "unexpect"})

        self.assertTrue("Received an unexpected response from the Urlscan API." in error.exception.cause)
        self.assertTrue("If the problem persists, please contact support." in error.exception.assistance)

    def test_submit_url_for_scan_json_decoder_error(self, mock_post):
        with self.assertRaises(PluginException) as error:
            self.action.run({"public": True, "url": "json_error"})

        self.assertTrue("Received an unexpected response from the Urlscan API." in error.exception.cause)
        self.assertTrue("(non-JSON or no response was received). Response was: " in error.exception.assistance)

    def test_submit_url_for_scan_499(self, mock_post):
        with self.assertRaises(PluginException) as error:
            self.action.run({"public": True, "url": "499"})

        self.assertTrue("Error 499." in error.exception.cause)
        self.assertTrue("Test 499" in error.exception.assistance)
