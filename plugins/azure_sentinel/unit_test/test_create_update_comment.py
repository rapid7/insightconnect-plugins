import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import CreateUpdateComment
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestCreateUpdateIncident(TestCase):
    def setUp(self) -> None:
        self.action = CreateUpdateComment()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "incidentId": "14071867",
            "incidentCommentId": "12345",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "properties": {"message": "Gallia est omnis divisa in partes tres."},
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_create_update_incident_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.create_update_comment.assert_called_once_with(
            "14071867",
            "12345",
            "integrationLab",
            "sentinel",
            "abcde",
            properties={"message": "Gallia est omnis divisa in partes tres."},
        )
