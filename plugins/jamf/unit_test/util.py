import logging
from typing import Any, Dict

import insightconnect_plugin_runtime
from icon_jamf.connection.connection import Connection

from mock import STUB_CONNECTION


class Util:
    @staticmethod
    def default_connection_connector(input_params: Dict[str, Any]) -> insightconnect_plugin_runtime.Connection:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(input_params)
        return connection

    @staticmethod
    def default_action_connector(
        input_connection_params: Dict[str, Any], action: insightconnect_plugin_runtime.Action
    ) -> insightconnect_plugin_runtime.Action:
        action = action
        action.connection = Util.default_connection_connector(input_connection_params)
        action.logger = logging.getLogger("action logger")
        return action
