import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import CreateUpdateIncident
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestCreateUpdateIncident(TestCase):
    def setUp(self) -> None:
        self.action = CreateUpdateIncident()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "incidentId": "14071867",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "properties": {
                "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
                "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
                "description": "This is a demo incident",
                "title": "Incident At Work",
                "owner": {"objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70"},
                "severity": "High",
                "classification": "FalsePositive",
                "classificationComment": "Not a malicious activity",
                "classificationReason": "IncorrectAlertLogic",
                "status": "Closed",
            },
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_create_update_incident_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.create_incident.assert_called_once_with(
            "14071867",
            "integrationLab",
            "sentinel",
            "abcde",
            properties={
                "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
                "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
                "description": "This is a demo incident",
                "title": "Incident At Work",
                "owner": {"objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70"},
                "severity": "High",
                "classification": "FalsePositive",
                "classificationComment": "Not a malicious activity",
                "classificationReason": "IncorrectAlertLogic",
                "status": "Closed",
            },
        )
