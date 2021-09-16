import sys
import os
from unittest.mock import patch
from komand_proofpoint_tap.actions.get_all_threats import GetAllThreats
from komand_proofpoint_tap.actions.get_all_threats.schema import Input
from unit_test.test_util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestGetAllThreats(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAllThreats())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_all_threats(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-27T15:00:00Z",
                Input.TIME_END: "2021-08-27T16:00:00Z",
                Input.THREAT_STATUS: "all",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
                "clicksBlocked": [
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
                "clicksPermitted": [],
                "messagesBlocked": [
                    {
                        "threatsInfoMap": [
                            {
                                "threat": "Example Threat",
                                "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
                                "threatStatus": "active",
                                "threatTime": "2021-08-27T15:59:49.000Z",
                                "threatType": "url",
                                "threatUrl": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                                "classification": "phish",
                            }
                        ],
                        "spamScore": 100,
                        "toAddresses": ["user@example.com"],
                        "subject": "Mail delivery failed: returning message to sender",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "messagesDelivered": [],
                "queryEndTime": "2021-08-27T16:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_all_threats_status_active(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-27T15:00:00Z",
                Input.TIME_END: "2021-08-27T16:00:00Z",
                Input.THREAT_STATUS: "active",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
                "clicksBlocked": [
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
                "clicksPermitted": [],
                "messagesBlocked": [],
                "messagesDelivered": [],
                "queryEndTime": "2021-08-27T16:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_all_threats_status_cleared(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-27T15:00:00Z",
                Input.TIME_END: "2021-08-27T16:00:00Z",
                Input.THREAT_STATUS: "cleared",
                Input.THREAT_TYPE: "url",
            }
        )
        expected = {
            "results": {
                "clicksBlocked": [],
                "clicksPermitted": [],
                "messagesBlocked": [],
                "messagesDelivered": [
                    {
                        "threatsInfoMap": [
                            {
                                "threat": "Example Threat",
                                "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
                                "threatStatus": "cleared",
                                "threatTime": "2021-08-27T15:59:49.000Z",
                                "threatType": "url",
                                "threatUrl": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                                "classification": "phish",
                            }
                        ],
                        "spamScore": 100,
                        "toAddresses": ["user@example.com"],
                        "subject": "Mail delivery failed: returning message to sender",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-27T16:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_all_threats_without_time_start(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_END: "2021-08-20T15:00:00Z",
                Input.THREAT_STATUS: "falsePositive",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
                "clicksBlocked": [],
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
                "messagesBlocked": [],
                "messagesDelivered": [],
                "queryEndTime": "2021-08-20T15:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_all_threats_without_time_end(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-20T13:00:00Z",
                Input.THREAT_STATUS: "active",
                Input.THREAT_TYPE: "attachment",
            }
        )
        expected = {
            "results": {
                "clicksBlocked": [],
                "clicksPermitted": [],
                "messagesBlocked": [
                    {
                        "threatsInfoMap": [
                            {
                                "threat": "Example Threat",
                                "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
                                "threatStatus": "active",
                                "threatTime": "2021-08-27T15:59:49.000Z",
                                "threatType": "attachment",
                                "threatUrl": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                                "classification": "phish",
                            }
                        ],
                        "spamScore": 100,
                        "toAddresses": ["user@example.com"],
                        "subject": "Mail delivery failed: returning message to sender",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "messagesDelivered": [],
                "queryEndTime": "2021-08-20T14:00:00Z",
            }
        }
        self.assertEqual(actual, expected)
