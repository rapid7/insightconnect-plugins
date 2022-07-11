import json
import os
import logging
from komand_sql.connection.schema import Input


STUB_CREDENTIALS_VALID = {"username": "user@example.com", "password": "mypassword"}
STUB_DB_VALID = "database_name"
STUB_HOST_VALID = "198.51.100.1"
STUB_PORT_VALID = "1433"
STUB_TYPE_VALID = "MSSQL"


STUB_CONNECTION = {
    Input.CREDENTIALS: {"username": "username", "password": "password"},
    Input.DB: STUB_DB_VALID,
    Input.HOST: STUB_HOST_VALID,
    Input.PORT: STUB_PORT_VALID,
    Input.TYPE: STUB_TYPE_VALID,
}


def mock_execute(*args):
    logging.info("mock_execute is called")
    logging.info(args)
    return mock_request_selection(args[0])


def mock_request_selection(query):
    if query == "SELECT * FROM test_data_table":
        return MockResponse("execute", 200)
    if query == "":
        return MockResponse("", "")
    raise Exception("Response not implemented")


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text

    def json(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
        ) as file:
            return json.load(file)

    def is_insert(self):
        return {}
