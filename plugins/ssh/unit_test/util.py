import logging
import os
import sys
from typing import TextIO, Tuple

sys.path.append(os.path.abspath("../"))

from pathlib import Path

from insightconnect_plugin_runtime.action import Action
from komand_ssh.connection.connection import Connection
from komand_ssh.connection.schema import Input

STUB_CONNECTION = {
    Input.HOST: "0.0.0.0",
    Input.PORT: "22",
    Input.KEY: {},
    Input.USE_KEY: False,
    Input.PASSWORD: {"secretKey": "ABC"},
    Input.USERNAME: "username",
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

    @staticmethod
    def mock_execute_command(command: str) -> Tuple[TextIO, TextIO, TextIO]:
        command.strip()
        file_ = open(Path(__file__).parent / "responses" / "results.txt", "r")
        return file_, file_, file_
