import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.actions.list_all_searches import ListAllSearches
from icon_microsoft_log_analytics.actions.list_all_searches.schema import Input
import logging

from icon_microsoft_log_analytics.util.tools import Message
from unit_test.mock import (
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_400,
    mock_request_403,
    mock_request_409,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mock_request_505,
    mocked_request,
    STUB_CONNECTION,
    STUB_RESOURCE_GROUP_NAME,
    STUB_WORKSPACE_NAME,
    STUB_SUBSCRIPTION_ID,
)


STUB_EXAMPLE_ACTION_RESPONSE = {
    "saved_searches": [
        {
            "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2015",
            "name": "test-new-saved-search-id-2015",
            "properties": {
                "category": " Saved Search Test Category",
                "displayName": "Create or Update Saved Search Test",
                "query": "* | measure Count() by Computer",
                "tags": [{"name": "Group", "value": "Computer"}],
            },
        },
        {
            "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2016",
            "name": "test-new-saved-search-id-2016",
            "properties": {
                "category": " Saved Search Test 2",
                "displayName": "Simple Test",
                "query": "TimeGenerated",
            },
        },
        {
            "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2017",
            "name": "test-new-saved-search-id-2017",
            "properties": {
                "category": " Saved Search Test 2",
                "displayName": "Simple Test",
                "query": "TimeGenerated",
            },
        },
    ]
}


class TestListAllSearches(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = ListAllSearches()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.RESOURCE_GROUP_NAME: STUB_RESOURCE_GROUP_NAME,
            Input.SUBSCRIPTION_ID: STUB_SUBSCRIPTION_ID,
            Input.WORKSPACE_NAME: STUB_WORKSPACE_NAME,
        }

    def test_list_all_searches(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_409, Message.CONFLICTED_STATE_OF_OBJECT_MESSAGE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    @mock.patch("icon_microsoft_log_analytics.util.tools.backoff_function", return_value=0)
    def test_list_all_searches_exception(self, mock_request, exception, mock_backoff_function):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
