import json
import logging
import os

from icon_python_3_script.connection import Connection
from insightconnect_plugin_runtime.action import Action
from typing import Union, Dict, Any


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
    def read_file_to_string(filename: str, directory_path: str = os.path.dirname(os.path.realpath(__file__))) -> str:
        with open(os.path.join(directory_path, filename)) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(
        filename: str, directory_path: str = os.path.dirname(os.path.realpath(__file__))
    ) -> Dict[str, Any]:
        return json.loads(Util.read_file_to_string(filename, directory_path))

    @staticmethod
    def mock_exec_python_function(*args, **kwargs) -> Union[Dict[str, Any], None]:
        if kwargs.get("params", {}).get("input") == {"some_input": "bad"}:
            return None
        if "username" in kwargs.get("function_", ""):
            return Util.read_file_to_dict(f"payloads/run_with_credentials.json.exp")
        if "username" not in kwargs.get("function_", ""):
            return Util.read_file_to_dict(f"payloads/run_no_credentials.json.exp")
        raise NotImplemented
