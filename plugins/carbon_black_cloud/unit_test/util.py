import logging

from icon_carbon_black_cloud.connection.connection import Connection
from icon_carbon_black_cloud.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    Input.URL: "https://example.com",
    Input.ORG_KEY: "12345",
    Input.API_ID: "67890",
    Input.API_SECRET_KEY: {"secretKey": "example"},
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
