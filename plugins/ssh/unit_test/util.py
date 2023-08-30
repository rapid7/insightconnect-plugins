import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_ssh.connection.connection import Connection
from komand_ssh.connection.schema import Input


class Util:
    @staticmethod
    def default_connector():
        connection = Connection()
        params = {
            Input.HOST: "0.0.0.0",
            Input.PORT: "22",
            Input.KEY: {},
            Input.USE_KEY: False,
            Input.PASSWORD: {"secretKey": "ABC"},
            Input.USERNAME: "username",
        }
        connection.logger = logging.getLogger("action logger")
        connection.parameters = params
        return connection
