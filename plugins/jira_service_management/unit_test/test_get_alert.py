import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import patch

from icon_jira_service_management.actions.get_alert import GetAlert
from icon_jira_service_management.actions.get_alert.schema import GetAlertOutput
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send")
class TestGetAlert(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAlert())

    def test_get_alert(self, mock_send: mock.Mock):
        mock_send.side_effect = [
            Util.MockResponse("get_alert_request.json", 200),
        ]

        input_params = {
            "identifier": "111111-9999-4ec2-8067-acde6abc040-1111123123",
        }

        expected = {
            "data": {
                "id": "e0caa0ce-d52f-4500-81b9-d592d06970b6",
                "tinyId": "1234",
                "createdAt": "2024-01-05T07:06:47.958Z",
                "updatedAt": "2024-01-05T07:06:47.958Z",
                "message": "The CPU usage on Server XYZ has exceeded 80% for over 5 minutes.",
                "entity": "DatabaseServer1",
                "source": "DBMonitoringTool",
                "status": "closed",
                "alias": "DatabaseConnectionFailure_DatabaseServer1",
                "tags": ["OverwriteQuietHours", "Critical"],
                "extraProperties": {
                    "backend": False,
                    "browser": "Firefox 113.0",
                    "browser.name": "Firefox",
                    "bundler": "parcel@2.10.3",
                    "environment": "production",
                },
                "description": "The alert is triggered due to the high CPU usage on Server XYZ. The CPU usage has consistently been above 80% for more than 5 minutes which could potentially lead to server slowdown or even a crash. Suggested action is to investigate the processes consuming high CPU and optimize or terminate them as needed. If the issue persists, consider upgrading the server resources.",
                "acknowledged": True,
                "count": 3,
                "owner": "John Smith",
                "snoozed": False,
                "snoozedUntil": "2022-05-01T00:00:00Z",
                "lastOccurredAt": "2022-04-01T00:00:00Z",
                "integrationType": "API",
                "integrationName": "Default API",
                "priority": "P1",
                "responders": [
                    {"id": "4513b7ea-3b91-438f-b7e4-e3e54af9147c", "type": "team"},
                    {"id": "bb4d9938-c3c2-455d-aaab-727aa701c0d8", "type": "user"},
                    {"id": "aee8a0de-c80f-4515-a232-501c0bc9d715", "type": "escalation"},
                    {"id": "80564037-1984-4f38-b98e-8a1f662df552", "type": "schedule"},
                ],
                "actions": ["RestartServer"],
                "seen": True,
            }
        }

        actual = self.action.run(input_params)
        validate(actual, GetAlertOutput.schema)
        self.assertEqual(actual, expected)
