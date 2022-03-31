import logging
import os
import json

from komand_carbon_black_defense.connection.connection import Connection
from komand_carbon_black_defense.connection.schema import Input


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
                Input.CONNECTOR: "connector",
                Input.URL: "url",
                Input.API_KEY: {"secretKey": "api_key"},
                Input.ORG_KEY: "org_key",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return default_connection, action
