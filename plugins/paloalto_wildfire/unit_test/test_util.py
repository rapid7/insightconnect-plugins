import sys
import os
from komand_paloalto_wildfire.connection.connection import Connection
from komand_paloalto_wildfire.connection.schema import Input
import logging

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.HOST: "wildfire.paloaltonetworks.com",
                Input.API_KEY: {"secretKey": "example-wildfire-apikey"},
                Input.VERIFY: True,
                Input.PROXY: {},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
