import logging
from pathlib import Path

import requests
from insightconnect_plugin_runtime import Action

from komand_otrs.connection.connection import Connection
from komand_otrs.connection.schema import Input as ConnectionInput

RESPONSES = Path(__file__).resolve().parent / "responses"

CONNECTION_PARAMS = {
    ConnectionInput.SERVER: "https://otrs.example.com",
    ConnectionInput.CREDENTIALS: {"username": "agent", "password": "dummy-password"},
}


class Util:
    @staticmethod
    def response(name: str, status_code: int = 200) -> requests.Response:
        response = requests.Response()
        response.status_code = status_code
        response._content = (RESPONSES / f"{name}.json.resp").read_bytes()
        return response

    @staticmethod
    def connection() -> Connection:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(CONNECTION_PARAMS)
        return connection

    @staticmethod
    def default_connector(action: Action) -> Action:
        action.connection = Util.connection()
        action.logger = logging.getLogger("action logger")
        return action
