import os
import sys

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_opsgenie.actions.get_alert import GetAlert
from icon_opsgenie.actions.get_alert.schema import Output
from icon_opsgenie.connection.connection import Connection
from icon_opsgenie.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from unit_test.mock import (
    STUB_ALERT_ID,
    mock_request_200,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mocked_request,
)


class TestGetAlert(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect({Input.API_KEY: {"secretKey": "1234567e-123c-123c-123c-1234567e9xAd"}})

        self.action = GetAlert()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.params = {"identifier": STUB_ALERT_ID}

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_alert_when_status_ok(self, mock_get):
        response = self.action.run(self.params)
        expected_response = {
            Output.DATA: {
                "id": "70413a06-38d6-4c85-92b8-5ebc900d42e2",
                "tinyId": "1791",
                "alias": "event_573",
                "message": "Our servers are in danger",
                "status": "closed",
                "acknowledged": False,
                "isSeen": True,
                "tags": ["OverwriteQuietHours", "Critical"],
                "snoozed": True,
                "snoozedUntil": "2017-04-03T20:32:35.143Z",
                "count": 79,
                "lastOccurredAt": "2017-04-03T20:05:50.894Z",
                "createdAt": "2017-03-21T20:32:52.353Z",
                "updatedAt": "2017-04-03T20:32:57.301Z",
                "source": "Isengard",
                "owner": "example@opsgenie.com",
                "priority": "P5",
                "responders": [
                    {"id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c", "type": "team"},
                    {"id": "bb4d9938-c3c2-455d-aaab-727aa701c0d8", "type": "user"},
                    {"id": "aee8a0de-c80f-4515-a232-501c0bc9d715", "type": "escalation"},
                    {"id": "80564037-1984-4f38-b98e-8a1f662df552", "type": "schedule"},
                ],
                "integration": {"id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c", "name": "ExampleName", "type": "API"},
                "report": {
                    "ackTime": 15702,
                    "closeTime": 60503,
                    "acknowledgedBy": "example@opsgenie.com",
                    "closedBy": "example@opsgenie.com",
                },
                "actions": ["Restart", "Ping"],
                "entity": "EC2",
                "description": "Example description",
                "details": {"serverName": "ExampleName", "region": "ExampleRegion"},
            },
            Output.REQUESTID: "9ae63dd7-ed00-4c81-86f0-c4ffd33142c9",
            Output.ELAPSED_TIME: 0.001,
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_403, PluginException.Preset.UNAUTHORIZED),
            (mock_request_404, PluginException.Preset.NOT_FOUND),
            (mock_request_500, PluginException.Preset.UNKNOWN),
        ],
    )
    def test_get_alert_when_status_error(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(
            context.exception.cause,
            PluginException.causes[exception],
        )
