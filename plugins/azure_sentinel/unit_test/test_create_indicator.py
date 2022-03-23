import logging
import sys
import os
from unittest import TestCase, mock

from icon_azure_sentinel.connection import Connection
from icon_azure_sentinel.actions.create_indicator import CreateIndicator
from icon_azure_sentinel.util.api import AzureSentinelClient

sys.path.append(os.path.abspath("../"))


class TestCreateIndicator(TestCase):
    def setUp(self) -> None:
        self.action = CreateIndicator()
        self.connection = Connection()
        self.connection.auth_token = "12345"
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")
        self.params = {
            "resourceGroupName": "integrationLab",
            "subscriptionId": "abcde",
            "workspaceName": "sentinel",
            "properties": {
                "confidence": 100,
                "description": "Example description",
                "displayName": "Test indicator",
                "pattern": "[url:value = 'https://www.contoso.com']",
                "patternType": "url",
                "source": "Azure Sentinel",
                "threatTypes": ["compromised"],
            },
        }
        self.action.connection.api_client = mock.create_autospec(AzureSentinelClient)

    def test_create_indicator(self):
        self.action.run(self.params)
        self.action.connection.api_client.create_indicator.assert_called_once_with(
            "integrationLab", "sentinel", "abcde", properties=self.params["properties"]
        )
