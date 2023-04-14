import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_google_web_risk.connection.connection import Connection
from icon_google_web_risk.actions.lookup import Lookup
import logging


class MockRequest:
    def __init__(self, endpoint, params):
        self.status_code = 200
        self.endpoint = endpoint
        self.params = params


class MockRequestFullData(MockRequest):
    @staticmethod
    def json():
        return {"threat": {"expireTime": "2019-09-23T15:00:01.288672152Z", "threatTypes": ["MALWARE"]}}


class MockRequestNoData(MockRequest):
    @staticmethod
    def json():
        return {}


class MockRequestWithWrongStatusCode(MockRequest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_code = 400

    @staticmethod
    def json():
        return {"error": {"message": "error message"}}


class TestLookup(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({"credentials": {"secretKey": "secret_123"}})

        self.action = Lookup()
        self.action.connection = self.connection

        self.params = {
            "threat_type_malware": True,
            "threat_type_social": True,
            "threat_type_unwanted": True,
            "url": "https://example.com",
        }

    @mock.patch("icon_google_web_risk.actions.lookup.action.requests.get", side_effect=MockRequestFullData)
    def test_lookup_when_response_full_data(self, mock):
        result = self.action.run(self.params)

        expected_result = {"expireTime": "2019-09-23T15:00:01.288672152Z", "threatTypes": ["MALWARE"]}
        self.assertEqual(result, expected_result)

    @mock.patch("icon_google_web_risk.actions.lookup.action.requests.get", side_effect=MockRequestNoData)
    def test_lookup_when_response_no_data(self, mock):
        result = self.action.run(self.params)

        expected_result = {}
        self.assertEqual(result, expected_result)

    @mock.patch("icon_google_web_risk.actions.lookup.action.requests.get", side_effect=MockRequestWithWrongStatusCode)
    def test_lookup_when_response_failed(self, mock):
        with self.assertRaises(PluginException):
            self.action.run(self.params)
