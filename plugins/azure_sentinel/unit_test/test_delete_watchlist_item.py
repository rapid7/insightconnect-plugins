import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import DeleteWatchlistItem
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestDeleteWatchlistItem(TestCase):
    def setUp(self) -> None:
        self.action = DeleteWatchlistItem()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "watchlistAlias": "14071867",
            "watchlistItemId": "3395856c-e81f-2b73-82de-e72602f798b6",
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_delete_watchlist_item_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.delete_watchlist_items.assert_called_once_with(
            "integrationLab",
            "sentinel",
            "abcde",
            "14071867",
            "3395856c-e81f-2b73-82de-e72602f798b6",
        )
