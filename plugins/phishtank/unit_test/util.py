import json
import os
import sys
import logging
import datetime
import re

import insightconnect_plugin_runtime
from komand_phishtank.connection.connection import Connection


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
