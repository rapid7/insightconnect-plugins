import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import CreateUpdateWatchlist
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestCreateWatchlist(TestCase):
    def setUp(self) -> None:
        self.action = CreateUpdateWatchlist()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "watchlistAlias": "testAlias",
            "properties": {
                "displayName": "High Value Assets Watchlist",
                "source": "Local File",
                "provider": "Microsoft",
                "description": "Watchlist from CSV content",
                "numberOfLinesToSkip": 1,
                "rawContent": "This line will be skipped\nheader1,header2\nvalue1,value2",
                "itemsSearchKey": "header1",
                "contentType": "text/csv",
            },
        }

    def test_create_watchlist_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.create_update_watchlist.assert_called_once_with(
            "integrationLab", "sentinel", "testAlias", "abcde", properties=self.params.get("properties")
        )
