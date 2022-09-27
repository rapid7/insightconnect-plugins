import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_indicator_by_value import GetIndicatorByValue
from icon_rapid7_intsights.actions.get_indicator_by_value.schema import Input


class TestGetIndicatorByValue(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetIndicatorByValue())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_value_should_success(self, make_request):
        actual = self.action.run({Input.INDICATOR_VALUE: "rapid7.com"})
        expected = {
            "first_seen": "2020-01-01T20:01:27.344Z",
            "geo_location": "US",
            "last_seen": "2020-01-30T16:18:51.148Z",
            "last_update": "2020-02-21T23:00:51.268Z",
            "related_campaigns": ["SolarWinds"],
            "related_malware": ["doppeldridex", "dridex"],
            "related_threat_actors": ["doppelspider"],
            "score": 100,
            "severity": "High",
            "sources": [{"ConfidenceLevel": 3, "Name": "AlienVault OTX"}],
            "system_tags": ["Phishing"],
            "tags": ["MyTag_1"],
            "type": "Domains",
            "value": "rapid7.com",
            "whitelist": False,
            "reported_feeds": [{"ID": "SampleID", "ConfidenceLevel": 3, "Name": "AlienVault OTX"}],
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_value_should_success_when_empty(self, make_request):
        actual = self.action.run({Input.INDICATOR_VALUE: "empty"})
        expected = {
            "related_campaigns": [],
            "related_malware": [],
            "related_threat_actors": [],
            "score": 0,
            "sources": [],
            "system_tags": [],
            "tags": [],
            "whitelist": False,
            "reported_feeds": [],
        }
        self.assertEqual(actual, expected)
