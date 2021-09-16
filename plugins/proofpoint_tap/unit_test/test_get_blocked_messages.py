import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.actions.get_blocked_messages import GetBlockedMessages
from komand_proofpoint_tap.actions.get_blocked_messages.schema import Input
from unit_test.test_util import Util
from unittest import TestCase

sys.path.append(os.path.abspath("../"))


class TestGetBlockedMessages(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetBlockedMessages())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-23T12:00:00Z",
                Input.TIME_END: "2021-08-23T13:00:00Z",
                Input.SUBJECT: "A phishy email",
                Input.THREAT_STATUS: "all",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
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
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages_active_status(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-23T12:00:00Z",
                Input.TIME_END: "2021-08-23T13:00:00Z",
                Input.SUBJECT: "A phishy email",
                Input.THREAT_STATUS: "active",
                Input.THREAT_TYPE: "url",
            }
        )
        expected = {
            "results": {
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
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages_cleared_status(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-23T12:00:00Z",
                Input.TIME_END: "2021-08-23T13:00:00Z",
                Input.SUBJECT: "A phishy email",
                Input.THREAT_STATUS: "cleared",
                Input.THREAT_TYPE: "attachment",
            }
        )
        expected = {
            "results": {
                "messagesBlocked": [
                    {
                        "threatsInfoMap": [
                            {
                                "threat": "Example Threat",
                                "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
                                "threatStatus": "cleared",
                                "threatTime": "2021-08-27T15:59:49.000Z",
                                "threatType": "attachment",
                                "threatUrl": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                                "classification": "phish",
                            }
                        ],
                        "spamScore": 100,
                        "toAddresses": ["user@example.com"],
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages_without_subject(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-23T12:00:00Z",
                Input.TIME_END: "2021-08-23T13:00:00Z",
                Input.THREAT_STATUS: "falsePositive",
                Input.THREAT_TYPE: "messageText",
            }
        )
        expected = {
            "results": {
                "messagesBlocked": [
                    {
                        "threatsInfoMap": [
                            {
                                "threat": "Example Threat",
                                "threatID": "d22be456cbc0a0e5d900696c36c92c547bea13cc76d32b63ed...",
                                "threatStatus": "falsePositive",
                                "threatTime": "2021-08-27T15:59:49.000Z",
                                "threatType": "messageText",
                                "threatUrl": "https://threatinsight.proofpoint.com/e65934ff-e650...",
                                "classification": "phish",
                            }
                        ],
                        "spamScore": 100,
                        "toAddresses": ["user@example.com"],
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T13:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages_without_time_start(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_END: "2021-08-23T15:00:00Z",
                Input.SUBJECT: "A phishy email",
                Input.THREAT_STATUS: "all",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
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
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T15:00:00Z",
            }
        }
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_get_blocked_messages_without_time_end(self, mock_request):
        actual = self.action.run(
            {
                Input.TIME_START: "2021-08-23T13:00:00Z",
                Input.SUBJECT: "A phishy email",
                Input.THREAT_STATUS: "all",
                Input.THREAT_TYPE: "all",
            }
        )
        expected = {
            "results": {
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
                        "subject": "A phishy email",
                        "fromAddress": ["user@example.com"],
                        "quarantineFolder": "Phish",
                    }
                ],
                "queryEndTime": "2021-08-23T14:00:00Z",
            }
        }
        self.assertEqual(actual, expected)
