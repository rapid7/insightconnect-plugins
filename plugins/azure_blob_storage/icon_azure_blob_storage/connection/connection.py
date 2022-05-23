import insightconnect_plugin_runtime
import requests

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_azure_blob_storage.connection.schema import Input
from icon_azure_blob_storage.util.api import AzureBlobStorageAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params=None):
        self.logger.info("Connect: Connecting...")
        self.api_client = AzureBlobStorageAPI(
            client_id=params.get(Input.CLIENT_ID),
            client_secret=params.get(Input.CLIENT_SECRET).get("secretKey"),
            tenant_id=params.get(Input.TENANT_ID),
            logger=self.logger,
            account_name=params.get(Input.ACCOUNT),
        )

    def test(self):
        try:
            if self.api_client._auth_token:
                return {"success": True}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance)
