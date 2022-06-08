import json
import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import ListIncidents
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))

# Opening JSON file
path = Path(__file__).parent / "payloads/example_incident.json"
with open(path) as file:
    TEST_INCIDENT = json.load(file)


class TestListIncidents(TestCase):
    def setUp(self) -> None:
        self.action = ListIncidents()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)
        self.action.connection.api_client.list_incident.return_value = ([TEST_INCIDENT], 3)

    def test_list_incidents_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.list_incident.assert_called_once_with(
            "integrationLab", "sentinel", {"orderBy": None, "top": None}, "abcde"
        )
