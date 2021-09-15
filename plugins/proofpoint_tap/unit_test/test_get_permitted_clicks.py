import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.actions.get_permitted_clicks import GetPermittedClicks
from komand_proofpoint_tap.actions.get_permitted_clicks.schema import Input
from unit_test.test_util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestGetPermittedClicks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetPermittedClicks())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_permitted_clicks(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-22T12:00:00Z",
                Input.TIME_END: "2021-08-22T13:00:00Z",
                Input.THREAT_STATUS: "active",
                Input.URL: "https://example.com",
            }
        )
        expected = {
            "results": {
                "clicksPermitted": [
                    {
                        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
                        "classification": "malware",
                        "clickIP": "208.86.202.9",
                        "clickTime": "2021-04-20T21:08:13.000Z",
                        "id": "0f5a7622-faa9-4e98-9b38-692581598a5e",
                        "messageID": "<user@example.com>",
                        "recipient": "user@example.com",
                        "sender": "user@example.com",
                        "senderIP": "10.25.0.30",
                        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
                        "threatStatus": "active",
                        "threatTime": "2021-04-20T21:08:38.000Z",
                        "threatURL": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                        "url": "https://example.com",
                        "userAgent": "Mozilla/5.0",
                    }
                ],
                "queryEndTime": "2021-08-22T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_permitted_clicks_cleared_status(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-22T12:00:00Z",
                Input.TIME_END: "2021-08-22T13:00:00Z",
                Input.THREAT_STATUS: "cleared",
                Input.URL: "https://example.com",
            }
        )
        expected = {
            "results": {
                "clicksPermitted": [
                    {
                        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
                        "classification": "malware",
                        "clickIP": "208.86.202.9",
                        "clickTime": "2021-04-20T21:08:13.000Z",
                        "id": "0f5a7622-faa9-4e98-9b38-692581598a5e",
                        "messageID": "<user@example.com>",
                        "recipient": "user@example.com",
                        "sender": "user@example.com",
                        "senderIP": "10.25.0.30",
                        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
                        "threatStatus": "cleared",
                        "threatTime": "2021-04-20T21:08:38.000Z",
                        "threatURL": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                        "url": "https://example.com",
                        "userAgent": "Mozilla/5.0",
                    }
                ],
                "queryEndTime": "2021-08-22T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_permitted_clicks_without_url(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-22T12:00:00Z",
                Input.TIME_END: "2021-08-22T13:00:00Z",
                Input.THREAT_STATUS: "falsePositive",
            }
        )
        expected = {
            "results": {
                "clicksPermitted": [
                    {
                        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
                        "classification": "malware",
                        "clickIP": "208.86.202.9",
                        "clickTime": "2021-04-20T21:08:13.000Z",
                        "id": "0f5a7622-faa9-4e98-9b38-692581598a5e",
                        "messageID": "<user@example.com>",
                        "recipient": "user@example.com",
                        "sender": "user@example.com",
                        "senderIP": "10.25.0.30",
                        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
                        "threatStatus": "falsePositive",
                        "threatTime": "2021-04-20T21:08:38.000Z",
                        "threatURL": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                        "url": "https://example.com",
                        "userAgent": "Mozilla/5.0",
                    }
                ],
                "queryEndTime": "2021-08-22T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_permitted_clicks_without_time_start(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_END: "2021-08-22T15:00:00Z",
                Input.THREAT_STATUS: "all",
                Input.URL: "https://example.com",
            }
        )
        expected = {
            "results": {
                "clicksPermitted": [
                    {
                        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
                        "classification": "malware",
                        "clickIP": "208.86.202.9",
                        "clickTime": "2021-04-20T21:08:13.000Z",
                        "id": "0f5a7622-faa9-4e98-9b38-692581598a5e",
                        "messageID": "<user@example.com>",
                        "recipient": "user@example.com",
                        "sender": "user@example.com",
                        "senderIP": "10.25.0.30",
                        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
                        "threatStatus": "active",
                        "threatTime": "2021-04-20T21:08:38.000Z",
                        "threatURL": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                        "url": "https://example.com",
                        "userAgent": "Mozilla/5.0",
                    }
                ],
                "queryEndTime": "2021-08-22T15:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_permitted_clicks_without_time_end(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-22T13:00:00Z",
                Input.THREAT_STATUS: "all",
                Input.URL: "https://example.com",
            }
        )
        expected = {
            "results": {
                "clicksPermitted": [
                    {
                        "GUID": "X7sh5TwRxBZOAXb-d8ESyugsIdtfv3u",
                        "classification": "malware",
                        "clickIP": "208.86.202.9",
                        "clickTime": "2021-04-20T21:08:13.000Z",
                        "id": "0f5a7622-faa9-4e98-9b38-692581598a5e",
                        "messageID": "<user@example.com>",
                        "recipient": "user@example.com",
                        "sender": "user@example.com",
                        "senderIP": "10.25.0.30",
                        "threatID": "f1f23718b35b8db3db005cd498ff0812e53fe994537567ff0a...",
                        "threatStatus": "active",
                        "threatTime": "2021-04-20T21:08:38.000Z",
                        "threatURL": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                        "url": "https://example.com",
                        "userAgent": "Mozilla/5.0",
                    }
                ],
                "queryEndTime": "2021-08-22T14:00:00Z",
            }
        }
        self.assertEqual(actual, expected)
