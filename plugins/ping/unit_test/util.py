import logging
import insightconnect_plugin_runtime
from komand_ping.connection import Connection


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect({})
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
