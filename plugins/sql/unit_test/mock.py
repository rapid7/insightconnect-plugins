import json
import os
import requests
import logging
import komand_sql.connection.connection
from komand_sql.connection.schema import Input
from komand.exceptions import ConnectionTestException
from typing import Callable
from unittest import mock
from sqlalchemy.orm import *
from sqlalchemy_utils import *
from sqlalchemy.engine import result
import sqlalchemy.testing.engines
import sqlalchemy.testing.assertions
from alchemy_mock.mocking import AlchemyMagicMock


STUB_CREDENTIALS_VALID = {"username": "user@example.com", "password": "mypassword"}
STUB_DB_VALID = "database_name"
STUB_HOST_VALID = "198.51.100.1"
STUB_PORT_VALID = "1433"
STUB_TYPE_VALID = "MSSQL"
STUB_TYPE_CONNSTRING = f"mssql+pymssql://{STUB_CREDENTIALS_VALID['username']}:{STUB_CREDENTIALS_VALID['password']}@{STUB_HOST_VALID}:{STUB_PORT_VALID}/{STUB_DB_VALID}"

STUB_CREDENTIALS_INVALID = {"username": "invalid_name", "password": "invalid_password"}
STUB_DB_INVALID = "invalid_db"
STUB_HOST_INVALID = "invalid_host"
STUB_PORT_INVALID = "invalid_port"
STUB_TYPE_INVALID = "invalid_type"

STUB_CONNECTION = {
    Input.CREDENTIALS: {"username": "username", "password": "password"},
    Input.DB: STUB_DB_VALID,
    Input.HOST: STUB_HOST_VALID,
    Input.PORT: STUB_PORT_VALID,
    Input.TYPE: STUB_TYPE_VALID
}


#ERROR: CANNOT ASSIGN TO LITERAL
# STUB_BAD_CONNECTION = {
#     Input.CREDENTIALS = STUB_CREDENTIALS_INVALID,
#     Input.DB: STUB_DB_INVALID,
#     Input.HOST: STUB_HOST_INVALID,
#     Input.PORT: STUB_PORT_INVALID,
#     Input.TYPE: STUB_TYPE_INVALID
# }

# def mock_connection():
#
def mock_session(*args):
    logging.info("Mock session is called")
    logging.info(args)
    return mock_request_selection(args[0])

def mock_engine(*args):
    logging.info("mock_engine is called")
    logging.info(args)
    mock_engine = create_mock_engine(f"mssql+pymssql://{STUB_CREDENTIALS_VALID['username']}:{STUB_CREDENTIALS_VALID['password']}@{STUB_HOST_VALID}:{STUB_PORT_VALID}/{STUB_DB_VALID}")
    #found in sqlalchemy.utils.functions.mock.py


#We may need to mock the entire session or mock createEngine
def mock_execute(*args):
    logging.info("mock_execute is called")
    logging.info(args)
    #session = AlchemyMagicMock()
    #Here we need to return a resultproxy object
    #sqlalchemy.engine.result.resultproxy
    return mock_request_selection(args[0])



def mock_commit(*args):
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


#ARE THESE APPLICABLE TO SQL REQUESTS?
# def mock_request_200(*args, **kwargs) -> MockResponse:
#     return mock_conditions(args[0], args[1], 200)
#
# def mock_request_400(*args, **kwargs) -> MockResponse:
#     return mock_conditions(args[0], args[1], 400)

#REST FOUND IN yuckymock.txt
# def mock_request(address):
#     if address == f"postgres://{STUB_CREDENTIALS_VALID['username']}:{STUB_CREDENTIALS_VALID['password']}@{STUB_HOST_VALID}:{STUB_PORT_VALID}/{STUB_DB_VALID}":
#         return MockResponse("using_postgresql_connection_string", 200)
#     if address == f"mssql+pymssql://{STUB_CREDENTIALS_VALID['username']}:{STUB_CREDENTIALS_VALID['password']}@{STUB_HOST_VALID}:{STUB_PORT_VALID}/{STUB_DB_VALID}":
#         return MockResponse("using_mssql_connection_string", 200)
#     if address == f"mysql+mysqldb://{STUB_CREDENTIALS_VALID['username']}:{STUB_CREDENTIALS_VALID['password']}@{STUB_HOST_VALID}:{STUB_PORT_VALID}/{STUB_DB_VALID}":
#         return MockResponse("using_mysql_connection_string", 200)


#DITCHING THIS
# def mocked_request(side_effect: Callable) -> None:
#     mock_function = requests
#     mock_function.request = mock.Mock(side_effect=side_effect)