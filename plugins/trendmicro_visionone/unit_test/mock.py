import json
import logging
import os

import pytmv1

from icon_trendmicro_visionone.connection.connection import Connection


def mock_params(action=None):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "action_io.json")) as file_:
        params = json.load(file_)
        if action:
            return params[action]
    return params


def mock_connection():
    connection = Connection()
    connection.logger = logging.getLogger()
    connection.url = "https://tmv1-mock.trendmicro.com"
    connection.key = "Dummy-Secret-Token"
    connection.app = "TM-R7"
    connection.client = pytmv1.client(connection.app, connection.key, connection.url)
    return connection
