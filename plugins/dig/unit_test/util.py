import json
import os
import sys
import logging

import insightconnect_plugin_runtime
from komand_dig.connection.connection import Connection


sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_dict(filename: str, encodingenabled: bool = False) -> dict:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            data = json.load(file_reader)
            if encodingenabled:
                encodeddata = {}
                for key, value in data.items():
                    encodeddata[key] = value.encode("utf-8")
                return encodeddata
            else:
                return data

    @staticmethod
    def mock_dig(*args, **kwargs):
        cmd = args[0]
        if cmd == f"/usr/bin/dig @8.8.8.8 rapid7.com MX":
            filename = "forward.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=True)
            return test_data
        elif cmd == f"/usr/bin/dig rapid7.com MX":
            filename = "forward_no_resolver.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=True)
            return test_data
        elif cmd == f"/usr/bin/dig @8 rapid7.com MX":
            filename = "forward_raise_error.json.resp"
            test_data = Util.read_file_to_dict(f"responses/{filename}", encodingenabled=True)
            return test_data
