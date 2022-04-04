import logging
import os
import json

from icon_palo_alto_cortex_xdr.connection.connection import Connection
from icon_palo_alto_cortex_xdr.connection.schema import Input


class Util:
    @staticmethod
    def read_file_to_dict(filename):
        with open(filename, "rt", encoding="utf8"):
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
                Input.API_KEY_ID: "1",
                Input.SECURITY_LEVEL: "Standard",
                Input.URL: "https://example.com/",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return default_connection, action
