import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Union
from unittest.mock import MagicMock

from icon_python_3_script.connection import Connection
from icon_python_3_script.connection.schema import Input
from insightconnect_plugin_runtime.action import Action


class Util:
    @staticmethod
    def default_connector(action: Action, connect_params: object = None) -> Action:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {"modules": [], "timeout": 60}
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def make_connection(modules: list = None, timeout: int = 60) -> Connection:
        connection = Connection()
        connection.logger = logging.getLogger("test_connection")
        connection.connect({Input.MODULES: modules or [], Input.TIMEOUT: timeout})
        return connection

    @staticmethod
    def temporary_directory_mock(path: str = "/tmp/fake_environment") -> MagicMock:
        context_manager = MagicMock()
        context_manager.__enter__ = MagicMock(return_value=path)
        context_manager.__exit__ = MagicMock(return_value=False)
        return context_manager

    @staticmethod
    def final_directory_mock(exists: bool) -> MagicMock:
        directory = MagicMock(spec=Path)
        directory.exists.return_value = exists
        return directory

    @staticmethod
    def read_file_to_string(filename: str, directory_path: str = os.path.dirname(os.path.realpath(__file__))) -> str:
        with open(os.path.join(directory_path, filename)) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(
        filename: str, directory_path: str = os.path.dirname(os.path.realpath(__file__))
    ) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(filename, directory_path))

    @staticmethod
    def mock_execute_function_as_process(*args, **kwargs) -> Union[Dict[str, Any], None]:
        # Parse function and parameters from subprocess args
        function_ = args[0] if len(args) > 0 else ""
        parameters = args[1] if len(args) > 1 else {}

        # Return None on bad input
        if parameters.get("some_input") == "bad":
            return None

        # Return appropriate mock payload based on function name
        if "username" in function_:
            return Util.read_file_to_dict("payloads/run_with_credentials.json.exp")
        return Util.read_file_to_dict("payloads/run_no_credentials.json.exp")
