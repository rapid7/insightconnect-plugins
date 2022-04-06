import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.triggers.search import Search
from icon_microsoft_log_analytics.triggers.search.schema import Input
from icon_microsoft_log_analytics.util.tools import return_non_empty_query_output
import logging

from icon_microsoft_log_analytics.util.tools import Message
from unit_test.mock import (
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

STUB_EXAMPLE_FUNCTION_RESPONSE = {
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
        },
    ]
}

STUB_EXAMPLE_API_RESPONSE = {
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
        },
        {
            "name": "PrimaryResult2",
            "columns": [{"name": "Category", "type": "string"}, {"name": "count_l", "type": "long"}],
            "rows": [],
        },
    ]
}


class TestSearch(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.trigger = Search()
        self.trigger.connection = self.connection
        self.trigger.logger = logging.getLogger("trigger logger")

        self.payload = {
            Input.QUERY: "TestQuery",
            Input.INTERVAL: 10,
            Input.RESOURCE_GROUP_NAME: "exampleresourcegroupname",
            Input.SUBSCRIPTION_ID: "1234",
            Input.WORKSPACE_NAME: "ExampleWorkspace",
        }

    def test_return_non_empty_query_output(self):
        response = return_non_empty_query_output(STUB_EXAMPLE_API_RESPONSE)
        self.assertEqual(STUB_EXAMPLE_FUNCTION_RESPONSE, response)

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
    def test_search_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.trigger.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
