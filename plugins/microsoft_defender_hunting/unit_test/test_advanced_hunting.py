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

from icon_microsoft_defender_hunting.actions.advanced_hunting import AdvancedHunting
from icon_microsoft_defender_hunting.actions.advanced_hunting.schema import Input
from icon_microsoft_defender_hunting.connection.connection import Connection
from icon_microsoft_defender_hunting.util.tools import Message

STUB_ACTION_RESPONSE = {
    "columns": [
        {"Name": "Timestamp", "Type": "DateTime"},
        {"Name": "FileName", "Type": "String"},
        {"Name": "InitiatingProcessFileName", "Type": "String"},
        {"Name": "DeviceId", "Type": "String"},
    ],
    "rows": [
        {
            "Timestamp": "2020-02-05T01:10:26.2648757Z",
            "FileName": "csc.exe",
            "InitiatingProcessFileName": "powershell.exe",
            "DeviceId": "10cbf9182d4e95660362f65cfa67c7731f62fdb3",
        },
        {
            "Timestamp": "2020-02-05T01:10:26.5614772Z",
            "FileName": "csc.exe",
            "InitiatingProcessFileName": "powershell.exe",
            "DeviceId": "10cbf9182d4e95660362f65cfa67c7731f62fdb3",
        },
    ],
}


class TestListIncidents(TestCase):
    @mock.patch(
        "icon_microsoft_defender_hunting.util.api.MicrosoftDefenderClientAPI._get_auth_token", return_value=None
    )
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = AdvancedHunting()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.QUERY: "DeviceProcessEvents | where InitiatingProcessFileName =~ 'powershell.exe' |where ProcessCommandLine contains 'appdata' |project Timestamp, FileName, InitiatingProcessFileName, DeviceId |limit 2"
        }

    def test_advanced_hunting(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = STUB_ACTION_RESPONSE
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, Message.RESOURCE_WAS_NOT_FOUND_CAUSE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    @mock.patch("icon_microsoft_defender_hunting.util.tools.backoff_function", return_value=0)
    def test_advanced_hunting_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
