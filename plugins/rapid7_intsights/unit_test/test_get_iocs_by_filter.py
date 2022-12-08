import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_iocs_by_filter import GetIocsByFilter
from icon_rapid7_intsights.actions.get_iocs_by_filter.schema import Input


class TestGetIocsByFilter(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.expected = {
            "content": [
                {
                    "firstSeen": "2020-01-01T20:01:27.344Z",
                    "geoLocation": "US",
                    "lastSeen": "2020-01-30T16:18:51.148Z",
                    "lastUpdateDate": "2020-02-21T23:00:51.268Z",
                    "relatedCampaigns": ["SolarWinds"],
                    "relatedMalware": ["doppeldridex", "dridex"],
                    "relatedThreatActors": ["doppelspider"],
                    "score": 100,
                    "severity": "High",
                    "sources": [{"ConfidenceLevel": 3, "Name": "AlienVault OTX"}],
                    "tags": ["MyTag_1"],
                    "type": "Domains",
                    "value": "rapid7.com",
                    "whitelisted": "false",
                    "reportedFeeds": [{"ID": "SampleID", "ConfidenceLevel": 3, "Name": "AlienVault OTX"}],
                }
            ],
            "nextOffset": "2022-11-18T16:59:01.626Z",
        }
        cls.action = Util.default_connector(GetIocsByFilter())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success(self, make_request):
        actual = self.action.run({Input.LAST_UPDATED_FROM: "2000-12-31T00:00:00Z"})
        self.assertEqual(self.expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success_all_inputs(self, make_request):
        actual = self.action.run(
            {
                Input.LAST_UPDATED_FROM: "2000-12-31T00:00:00Z",
                Input.LIMIT: 1000,
                Input.TYPE: ["Domains"],
                Input.LAST_UPDATED_TO: "2000-12-31T00:00:00Z",
                Input.LAST_SEEN_FROM: "2000-12-31T00:00:00Z",
                Input.LAST_SEEN_TO: "2000-12-31T00:00:00Z",
                Input.FIRST_SEEN_FROM: "2000-12-31T00:00:00Z",
                Input.FIRST_SEEN_TO: "2000-12-31T00:00:00Z",
                Input.STATUS: "Active",
                Input.SEVERITY: ["High", "Low"],
                Input.SOURCE_IDS: ["123450000012345000001233"],
                Input.KILL_CHAIN_PHASES: ["Exploitation", "Installation"],
                Input.OFFSET: "2022-11-18T16:59:01.626Z",
            }
        )
        self.assertEqual(self.expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success_when_empty(self, make_request):
        actual = self.action.run({Input.LAST_UPDATED_FROM: "2000-12-30T00:00:00Z"})
        expected = {"content": []}
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success_when_limit_changed(self, make_request):
        actual = self.action.run({Input.LAST_UPDATED_FROM: "2000-12-31T00:00:00Z", Input.LIMIT: 1})
        self.assertEqual(self.expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success_when_limit_lower(self, make_request):
        actual = self.action.run({Input.LAST_UPDATED_FROM: "2000-12-31T00:00:00Z", Input.LIMIT: 0})
        self.assertEqual(self.expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_filter_should_success_when_limit_higher(self, make_request):
        actual = self.action.run({Input.LAST_UPDATED_FROM: "2000-12-31T00:00:00Z", Input.LIMIT: 1001})
        self.assertEqual(self.expected, actual)
