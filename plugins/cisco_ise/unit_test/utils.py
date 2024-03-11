import logging

from icon_cisco_ise.connection.connection import Connection
from icon_cisco_ise.connection.schema import Input
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    Input.CREDENTIALS: {"username": "ExampleUsername", "password": "ExamplePassword"},
    Input.ADDRESS: "example.com",
    Input.SSL_VERIFY: False,
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
