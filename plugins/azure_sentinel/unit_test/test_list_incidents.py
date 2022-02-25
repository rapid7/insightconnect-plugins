import sys
import logging
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.actions import ListIncidents

sys.path.append(str(Path("../").absolute()))


class TestListIncidents(TestCase):
    def setUp(self) -> None:
        self.action = ListIncidents()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "api-version": "2021-04-01",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
        }

    @mock.patch("icon_azure_sentinel.util.helpers.AzureSentinelClient.list_incident")
    def test_list_incidents_ok(self, mock_get):
        self.action.run(self.params)
        mock_get.assert_called_once_with("integrationLab", "sentinel", {"filter": None, "orderBy": None, "top": None})
