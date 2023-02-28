import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from icon_ivanti_service_manager.connection import Connection
from icon_ivanti_service_manager.connection.schema import Input
from requests.models import HTTPError


class Meta:
    version = "0.0.0"


class Util:
    STUB_URL_API = "This is a url"

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.meta = Meta()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.CREDENTIALS: {"secretKey": "4472f2g7-991z-4w70-li11-7552w8qm0266"},
            Input.SSL_VERIFY: "false",
            Input.URL: "",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()
