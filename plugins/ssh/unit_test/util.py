import logging
import os
import sys
from typing import Tuple
from unittest.mock import MagicMock

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
    def mock_execute_command(command: str, exit_status: int = 0) -> Tuple[MagicMock, MagicMock, MagicMock]:
        with open(Path(__file__).parent / "responses" / "results.txt", "rb") as response_file:
            content = response_file.read()

        stdin = MagicMock()
        stdout = MagicMock()
        stderr = MagicMock()
        stdout.read = MagicMock(side_effect=[content, b""])
        stderr.read = MagicMock(side_effect=[b"", b""])
        stdout.channel = MagicMock(recv_exit_status=MagicMock(return_value=exit_status))
        stdin.channel = stdout.channel
        stderr.channel = stdout.channel
        return stdin, stdout, stderr
