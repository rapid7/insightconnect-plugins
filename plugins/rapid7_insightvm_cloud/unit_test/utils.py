import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_rapid7_insightvm_cloud.connection.connection import Connection
from icon_rapid7_insightvm_cloud.connection.schema import Input

DEFAULT_ENCODING = "utf-8"


class Utils:
    @staticmethod
    def read_file_to_dict(filename):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), encoding=DEFAULT_ENCODING
        ) as file:
            text = file.read()
            return json.loads(text)

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.REGION: "us",
                Input.CREDENTIALS: {"secretKey": "secret_key"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return default_connection, action
