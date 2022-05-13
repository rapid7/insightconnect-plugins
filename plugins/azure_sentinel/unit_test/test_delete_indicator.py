import logging
import sys
import os
from unittest import TestCase, mock

from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.actions.delete_indicator import DeleteIndicator
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(os.path.abspath("../"))


class TestDeleteIndicator(TestCase):
    def setUp(self) -> None:
        self.action = DeleteIndicator()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_delete_indicator(self):
        self.action.run(self.params)
        self.action.connection.api_client.delete_indicator.assert_called_once_with(
            "integrationLab",
            "sentinel",
            "abcde",
            "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
        )
