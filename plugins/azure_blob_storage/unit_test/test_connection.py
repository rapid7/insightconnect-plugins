import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_blob_storage.actions.create_container.action import CreateContainer
from icon_azure_blob_storage.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestConnection(TestCase):
    def test_connection(self, mock_request: MagicMock) -> None:
        action = Util.default_connector(
            CreateContainer(),
            {
                Input.ACCOUNT: "valid_account",
                Input.CLIENT_ID: "valid_client_id",
                Input.CLIENT_SECRET: {"secretKey": "valid_api_key"},
                Input.TENANT_ID: "valid_tenant_id",
            },
        )

        self.assertEqual("valid_access_token", action.connection.api_client.auth_token)

    def test_connection_wrong_credentials(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as error:
            action = Util.default_connector(
                CreateContainer(),
                {
                    Input.ACCOUNT: "valid_account",
                    Input.CLIENT_ID: "valid_client_id",
                    Input.CLIENT_SECRET: {"secretKey": "invalid_api_key"},
                    Input.TENANT_ID: "valid_tenant_id",
                },
            )
            auth_token = action.connection.api_client.auth_token

        self.assertEqual("Unable to authorize against Azure Storage API.", error.exception.cause)
        self.assertEqual(
            "The application may not be authorized to connect to the Azure Storage API. Please contact your Azure administrator.",
            error.exception.assistance,
        )
