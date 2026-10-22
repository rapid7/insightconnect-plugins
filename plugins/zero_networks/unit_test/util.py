import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

import requests

from icon_zero_networks.connection.connection import Connection
from icon_zero_networks.connection.schema import Input

BASE_URL = "https://portal.zeronetworks.com/api/v1"


def mock_response(status_code: int, body=None, url: str = BASE_URL) -> requests.Response:
    """Build a real requests.Response so the runtime's response handling is exercised as it is in production."""
    response = requests.Response()
    response.status_code = status_code
    response.url = url
    response.encoding = "utf-8"
    response.headers["Content-Type"] = "application/json"
    response._content = b"" if body is None else json.dumps(body).encode("utf-8")
    return response


class Util:
    @staticmethod
    def default_connector(action, connect_params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = connect_params or {
            Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
            Input.URL: BASE_URL,
        }
        default_connection.connect(params)
        if action is not None:
            action.connection = default_connection
            action.logger = logging.getLogger("action logger")
        return default_connection, action

    @staticmethod
    def mock_send(status_code: int, body=None):
        """Build a requests.Session.send replacement that records the prepared request it was given."""
        sent = []

        def _send(_session, prepared_request, **kwargs):
            sent.append(prepared_request)
            return mock_response(status_code, body, url=prepared_request.url)

        return _send, sent
