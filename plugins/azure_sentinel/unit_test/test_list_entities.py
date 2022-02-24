import sys
import logging
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.actions import ListEntities

sys.path.append(str(Path("../").absolute()))


class TestListEntities(TestCase):
    def setUp(self) -> None:
        self.action = ListEntities()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "api-version": "2021-04-01",
            "incidentId": "abcde",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
        }

    @mock.patch("icon_azure_sentinel.util.helpers.AzureSentinelClient.list_entities")
    def test_list_entities_ok(self, mock_get):
        self.action.run(self.params)
        mock_get.assert_called_once_with(
            "abcde", "integrationLab", "sentinel", {"filter": None, "orderBy": None, "top": None}
        )
