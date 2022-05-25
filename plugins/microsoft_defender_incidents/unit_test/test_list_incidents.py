import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase, mock

from mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_400,
    mock_request_403,
    mock_request_404,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mock_request_505,
    mocked_request,
)

from icon_microsoft_defender_incidents.actions.list_incidents import ListIncidents
from icon_microsoft_defender_incidents.actions.list_incidents.schema import Input
from icon_microsoft_defender_incidents.connection.connection import Connection
from icon_microsoft_defender_incidents.util.tools import Message

STUB_ACTION_RESPONSE = {
    "incidents": [
        {
            "incidentId": 924518,
            "incidentName": "Email reported by user as malware or phish",
            "createdTime": "2020-09-06T12:07:55.1366667Z",
            "lastUpdateTime": "2020-09-06T12:07:55.32Z",
            "classification": "Unknown",
            "determination": "NotAvailable",
            "status": "Active",
            "severity": "Informational",
            "alerts": [
                {
                    "alertId": "faf8edc936-85f8-a603-b800-08d8525cf099",
                    "incidentId": 924518,
                    "serviceSource": "OfficeATP",
                    "creationTime": "2020-09-06T12:07:54.3716642Z",
                    "lastUpdatedTime": "2020-09-06T12:37:40.88Z",
                    "firstActivity": "2020-09-06T12:04:00Z",
                    "lastActivity": "2020-09-06T12:04:00Z",
                    "title": "Email reported by user as malware or phish",
                    "description": "This alert is triggered when any email message is reported as malware or phish by users -V1.0.0.2",
                    "category": "InitialAccess",
                    "status": "InProgress",
                    "severity": "Informational",
                    "investigationState": "Queued",
                    "detectionSource": "OfficeATP",
                    "assignedTo": "Automation",
                    "entities": [
                        {
                            "entityType": "MailBox",
                            "userPrincipalName": "testUser3@example.com",
                            "mailboxDisplayName": "test User3",
                            "mailboxAddress": "testUser3@example.com",
                        }
                    ],
                }
            ],
        }
    ],
}


class TestListIncidents(TestCase):
    @mock.patch("icon_microsoft_defender_incidents.util.api.AzureClient._get_auth_token", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = ListIncidents()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.STATUS: "All",
        }

    def test_list_incidents(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = STUB_ACTION_RESPONSE
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, Message.RESOURCE_WAS_NOT_FOUND_CAUSE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    @mock.patch("icon_microsoft_defender_incidents.util.tools.backoff_function", return_value=0)
    def test_list_incidents_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
