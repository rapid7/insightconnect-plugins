import logging

from icon_azure_compute.connection.connection import Connection
from icon_azure_compute.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    Input.HOST: "https://management.azure.com",
    Input.CLIENT_ID: "ExampleClientID",
    Input.CLIENT_SECRET: {"secretKey": "ExampleSecret"},
    Input.TENANT_ID: "ExampleTenantID",
    Input.API_VERSION: "2023-09-01",
}


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(STUB_CONNECTION)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
