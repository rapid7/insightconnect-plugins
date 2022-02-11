import json
import logging
import os

from unittest.mock import Mock

from komand_powershell.connection import Connection
from komand_powershell.actions.execute_script.schema import Output


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")

        default_connection.connect(connect_params)
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
    def mock_powershell(*args, **kwargs):
        class MockProcess:
            def __init__(self, filename):
                self.response_text = Util.read_file_to_string(f"payloads/{filename}.json.resp")

            def __enter__(self, *args, **kwargs):
                return self

            def __exit__(self, *args, **kwargs):
                pass

            def communicate(self):
                response_dict = json.loads(self.response_text)
                return response_dict.get(Output.STDOUT), response_dict.get(Output.STDERR)

            def run_ps(self, *args, **kwargs):
                response_dict = json.loads(self.response_text)
                mock = Mock()
                mock.status_code = response_dict.get("status_code")
                mock.std_err = bytes(response_dict.get(Output.STDERR), "utf-8")
                mock.std_out = bytes(response_dict.get(Output.STDOUT), "utf-8")
                return mock

        if kwargs.get("transport") == "ntlm":
            return MockProcess("powershell_string_ntlm")
        if kwargs.get("transport") == "credssp":
            return MockProcess("powershell_string_credssp")
        if kwargs.get("transport") == "kerberos":
            return MockProcess("powershell_string_kerberos")

        return MockProcess("powershell_string_local")
