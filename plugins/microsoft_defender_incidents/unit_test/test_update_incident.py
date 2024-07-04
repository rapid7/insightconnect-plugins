import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

import json
import logging
from unittest import TestCase, mock

from mock import (
    STUB_CONNECTION,
    STUB_INCIDENT_IDENTIFIER,
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

from icon_microsoft_defender_incidents.actions.update_incident import UpdateIncident
from icon_microsoft_defender_incidents.actions.update_incident.schema import Input
from icon_microsoft_defender_incidents.connection.connection import Connection
from icon_microsoft_defender_incidents.util.tools import Message

STUB_ACTION_RESPONSE = {
    "alerts": [],
    "incidentName": "",
    "severity": "",
    "status": "Resolved",
    "assignedTo": "user@example.com",
    "classification": "TruePositive",
    "determination": "Malware",
    "tags": ["Test1", "Test2"],
    "comments": [
        {"comment": "pen testing", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:34:21.5519738Z"},
        {"comment": "valid incident", "createdBy": "user@example.com", "createdTime": "2021-05-02T09:36:27.6652581Z"},
    ],
}


class TestListIncidents(TestCase):
    @mock.patch("icon_microsoft_defender_incidents.util.api.AzureClient._get_auth_token", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = UpdateIncident()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.IDENTIFIER: STUB_INCIDENT_IDENTIFIER,
            Input.STATUS: "Resolved",
            Input.ASSIGNEDTO: "user@example.com",
            Input.CLASSIFICATION: "TruePositive",
            Input.DETERMINATION: "Malware",
            Input.TAGS: ["Test1", "Test2"],
            Input.COMMENTS: [
                {
                    "comment": "pen testing",
                    "createdBy": "user@example.com",
                    "createdTime": "2021-05-02T09:34:21.5519738Z",
                },
                {
                    "comment": "valid incident",
                    "createdBy": "user@example.com",
                    "createdTime": "2021-05-02T09:36:27.6652581Z",
                },
            ],
        }

    def test_update_incident(self):
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
    def test_update_incident_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
