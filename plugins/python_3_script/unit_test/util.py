import json
import logging
import os

from komand_python_3_script.connection import Connection
from komand_python_3_script.actions.run.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
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
    def read_file_to_string(filename, directory_path=os.path.dirname(os.path.realpath(__file__))):
        with open(os.path.join(directory_path, filename)) as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename, directory_path=os.path.dirname(os.path.realpath(__file__))):
        return json.loads(Util.read_file_to_string(filename, directory_path))

    @staticmethod
    def mock_exec_python_function(*args, **kwargs):
        function = kwargs.get("params", dict()).get(Input.FUNCTION, "").split("\n")
        if "return {" in function[-1]:
            return Util.read_file_to_dict(f"payloads/run.json.resp")
        return None
