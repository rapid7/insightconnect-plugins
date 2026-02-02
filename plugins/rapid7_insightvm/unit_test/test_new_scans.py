import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import mock_open, patch

from komand_rapid7_insightvm.triggers import NewScans

from util import Util


class TestNewScans(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(NewScans())

    @patch("os.makedirs")
    @patch(
        "komand_rapid7_insightvm.util.cache_file_manager.CacheFileManager",
        mock_open(read_data='{"foo": "bar"}'),
    )
    @patch("builtins.open", mock_open(read_data='{"foo": "bar"}'))
    def test_get_cache_site_scans(self, mocked_makedirs) -> None:
        actual = NewScans.get_cache_site_scans(NewScans())
        expected = {"foo": "bar"}
        self.assertEqual(expected, actual)

    def test_get_track_site_scans(self) -> None:
        site_scans = {"abc": [{"scan_id": "abc"}], "def": [{"scan_id": "def"}]}
        actual = NewScans.get_track_site_scans(NewScans(), site_scans)
        expected = {"abc": ["abc"], "def": ["def"]}
        self.assertEqual(expected, actual)

    @patch("requests.Session.get", side_effect=Util.mocked_requests)
    def test_get_scan_details(self, mock_get) -> None:
        scan = {"scan_id": "abc"}
        actual = self.action.get_scan_details("https://example.com/api/getscandetails", scan)
        expected = {"foo": "bar"}
        self.assertEqual(actual, expected)
