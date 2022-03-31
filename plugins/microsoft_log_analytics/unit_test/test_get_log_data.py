import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.actions.get_log_data import GetLogData
from icon_microsoft_log_analytics.actions.get_log_data.schema import Input
from icon_microsoft_log_analytics.util.tools import clean_query_output
import logging

from icon_microsoft_log_analytics.util.tools import Message
from unit_test.mock import (
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_403,
    mock_request_409,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mocked_request,
    STUB_CONNECTION,
    mock_request_400,
)

STUB_EXAMPLE_ACTION_RESPONSE = {
    "tables": [
        {
            "name": "PrimaryResult",
            "columns": [{"name": "Category", "type": "string"}, {"name": "count_l", "type": "long"}],
            "rows": [
                {"Category": "Administrative", "count_l": 20839},
                {"Category": "Recommendation", "count_l": 122},
                {"Category": "Alert", "count_l": 64},
                {"Category": "ServiceHealth", "count_l": 11},
            ],
        }
    ]
}

STUB_EXAMPLE_API_RESPONSE = {
    "tables": [
        {
            "name": "PrimaryResult",
            "columns": [{"name": "Category", "type": "string"}, {"name": "count_l", "type": "long"}],
            "rows": [["Administrative", 20839], ["Recommendation", 122], ["Alert", 64], ["ServiceHealth", 11]],
        }
    ]
}


class TestGetLogData(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetLogData()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.QUERY: "TestQuery",
            Input.RESOURCE_GROUP_NAME: "exampleresourcegroupname",
            Input.SUBSCRIPTION_ID: "1234",
            Input.WORKSPACE_NAME: "ExampleWorkspace",
        }

    def test_get_log_data(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(expected_response, response)

    def test_clean_query_output(self):
        response = clean_query_output(STUB_EXAMPLE_API_RESPONSE)
        self.assertEqual(STUB_EXAMPLE_ACTION_RESPONSE, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_409, Message.CONFLICTED_STATE_OF_OBJECT_MESSAGE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
        ],
    )
    @mock.patch("icon_microsoft_log_analytics.util.tools.backoff_function", return_value=0)
    def test_get_log_data_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
