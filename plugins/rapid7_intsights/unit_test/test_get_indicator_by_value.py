import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.get_indicator_by_value import GetIndicatorByValue
from icon_rapid7_intsights.actions.get_indicator_by_value.schema import (
    Input,
    GetIndicatorByValueInput,
    GetIndicatorByValueOutput,
)
from jsonschema import validate


class TestGetIndicatorByValue(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetIndicatorByValue())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_value_should_success(self, make_request):
        input_params = {Input.INDICATOR_VALUE: "rapid7.com"}
        validate(input_params, GetIndicatorByValueInput.schema)
        actual = self.action.run(input_params)
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
            "sources": [{"confidenceLevel": 3, "name": "AlienVault OTX"}],
            "system_tags": ["Phishing"],
            "tags": ["MyTag_1"],
            "type": "Domains",
            "value": "rapid7.com",
            "whitelist": False,
            "reported_feeds": [{"id": "SampleID", "confidenceLevel": 3, "name": "AlienVault OTX"}],
        }
        self.assertEqual(actual, expected)
        validate(actual, GetIndicatorByValueOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_indicator_by_value_should_success_when_empty(self, make_request):
        input_params = {Input.INDICATOR_VALUE: "empty"}
        validate(input_params, GetIndicatorByValueInput.schema)
        actual = self.action.run(input_params)
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
        validate(actual, GetIndicatorByValueOutput.schema)
