import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.action import Action
from komand_sed.connection.connection import Connection


class Util:
    @staticmethod
    def default_connector(action: Action) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect({})
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
