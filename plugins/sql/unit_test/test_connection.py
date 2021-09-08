import unittest
from dataclasses import dataclass
from typing import Optional

from komand_sql.connection.connection import Connection
import logging

from komand_sql.connection.schema import Input


@dataclass
class TestCase:
    name: str
    input_type: str
    input_port: Optional[str]
    expected: str


testcases = [
    TestCase(
        name="mssql_connect",
        input_type="MSSQL",
        input_port="1433",
        expected="mssql+pymssql://username:password@198.51.100.1:1433/database_name",
    ),
    TestCase(
        name="postgres_connect",
        input_type="PostgreSQL",
        input_port="1433",
        expected="postgres://username:password@198.51.100.1:1433/database_name",
    ),
    TestCase(
        name="mysql_connect",
        input_type="MySQL",
        input_port="1433",
        expected="mysql+mysqldb://username:password@198.51.100.1:1433/database_name",
    ),
    TestCase(
        name="mssql_connect_without_port",
        input_type="MSSQL",
        input_port=None,
        expected="mssql+pymssql://username:password@198.51.100.1:1433/database_name",
    ),
    TestCase(
        name="postgres_connect_without_port",
        input_type="PostgreSQL",
        input_port=None,
        expected="postgres://username:password@198.51.100.1:5432/database_name",
    ),
    TestCase(
        name="mysql_connect_without_port",
        input_type="MySQL",
        input_port=None,
        expected="mysql+mysqldb://username:password@198.51.100.1:3306/database_name",
    ),
    TestCase(
        name="mssql_connect_different_port",
        input_type="MSSQL",
        input_port="1111",
        expected="mssql+pymssql://username:password@198.51.100.1:1111/database_name",
    ),
    TestCase(
        name="postgres_connect_different_port",
        input_type="PostgreSQL",
        input_port="1111",
        expected="postgres://username:password@198.51.100.1:1111/database_name",
    ),
    TestCase(
        name="mysql_connect_different_port",
        input_type="MySQL",
        input_port="1111",
        expected="mysql+mysqldb://username:password@198.51.100.1:1111/database_name",
    ),
]


class TestConnection(unittest.TestCase):
    @staticmethod
    def configure_connection(type_: str, port: Optional[str]):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.CREDENTIALS: {"username": "username", "password": "password"},
            Input.PORT: port,
            Input.TYPE: type_,
            Input.HOST: "198.51.100.1",
            Input.DB: "database_name",
        }
        default_connection.connect(params)

        return default_connection

    def test_connect(self):
        for case in testcases:
            with self.subTest(case.name):
                actual = TestConnection.configure_connection(case.input_type, case.input_port).conn_str
                self.assertEqual(
                    case.expected,
                    actual,
                )
