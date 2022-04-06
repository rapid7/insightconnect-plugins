import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import ListAlerts
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestListAlerts(TestCase):
    def setUp(self) -> None:
        self.action = ListAlerts()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.params = {
            "incidentId": "abcde",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_list_alerts_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.list_alerts.assert_called_once_with(
            "abcde", "integrationLab", "sentinel", "abcde"
        )
