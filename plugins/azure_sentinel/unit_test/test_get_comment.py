import logging
import sys
from pathlib import Path
from unittest import TestCase, mock

from icon_azure_sentinel.actions import GetComment
from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(str(Path("../").absolute()))


class TestGetComment(TestCase):
    def setUp(self) -> None:
        self.action = GetComment()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "incidentId": "14071867",
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "incidentCommentId": "comment_id",
        }

    def test_get_incident_ok(self):
        self.action.run(self.params)
        self.action.connection.api_client.get_comment.assert_called_once_with(
            "14071867", "comment_id", "integrationLab", "sentinel", "abcde"
        )
