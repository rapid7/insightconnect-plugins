import logging

from icon_splunk.connection.connection import Connection
from insightconnect_plugin_runtime.action import Action

STUB_CONNECTION = {
    "host": "localhost",
    "port": 8089,
    "credentials": {"username": "admin", "password": "password"},
    "license": "Free",
    "use_ssl": False,
    "ssl_verify": False,
}


def default_connector(action: Action) -> Action:
    default_connection = Connection()
    default_connection.logger = logging.getLogger("connection logger")
    default_connection.connect(STUB_CONNECTION)
    action.connection = default_connection
    action.logger = logging.getLogger("action logger")
    return action
