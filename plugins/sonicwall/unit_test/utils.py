import logging

from icon_sonicwall.connection.connection import Connection
from icon_sonicwall.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    Input.URL: "https://example.com",
    Input.PORT: 443,
    Input.VERIFY_SSL: False,
    Input.CREDENTIALS: {"username": "ExampleUsername", "password": "ExamplePassword"},
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
