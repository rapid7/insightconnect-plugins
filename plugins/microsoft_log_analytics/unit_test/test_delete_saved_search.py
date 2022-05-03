import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from parameterized import parameterized

from icon_microsoft_log_analytics.connection.connection import Connection
from icon_microsoft_log_analytics.actions.delete_saved_search import DeleteSavedSearch
from icon_microsoft_log_analytics.actions.delete_saved_search.schema import Input
import logging

from icon_microsoft_log_analytics.util.tools import Message
from unit_test.mock import (
    mock_request_200,
    mock_request_400,
    mock_request_429,
    mock_request_500,
    mock_request_503,
    mock_request_505,
    mocked_request,
    STUB_CONNECTION,
    STUB_RESOURCE_GROUP_NAME,
    STUB_WORKSPACE_NAME,
    STUB_SUBSCRIPTION_ID,
    STUB_SAVED_SEARCH_NAME,
)


STUB_EXAMPLE_ACTION_RESPONSE = {
    "message": "Saved search test-new-saved-search-id-2015 has been deleted",
    "deleted_saved_search": {
        "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2015",
        "name": "test-new-saved-search-id-2015",
        "properties": {
            "category": " Saved Search Test Category",
            "displayName": "Create or Update Saved Search Test",
            "query": "* | where TimeGenerated > ago(1h)",
        },
    },
}


class TestDeleteSavedSearch(TestCase):
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI._connection", return_value=None)
    def setUp(self, mock_connection) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DeleteSavedSearch()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {
            Input.RESOURCE_GROUP_NAME: STUB_RESOURCE_GROUP_NAME,
            Input.SUBSCRIPTION_ID: STUB_SUBSCRIPTION_ID,
            Input.WORKSPACE_NAME: STUB_WORKSPACE_NAME,
            Input.SAVED_SEARCH_NAME: STUB_SAVED_SEARCH_NAME,
        }

    def test_delete_saved_search_ok(self):
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_400, Message.BAD_REQUEST_MESSAGE),
            (mock_request_429, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.RATE_LIMIT]),
            (mock_request_505, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    @mock.patch("icon_microsoft_log_analytics.util.tools.backoff_function", return_value=0)
    @mock.patch("icon_microsoft_log_analytics.util.api.AzureLogAnalyticsClientAPI.get_saved_search")
    def test_delete_saved_search_exception(self, mock_request, exception, mock_backoff_function, mock_get):
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
