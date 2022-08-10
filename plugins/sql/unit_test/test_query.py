import logging
import os
import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock


sys.path.append(os.path.abspath("../"))

from komand_sql.connection import Connection
from komand_sql.actions import Query


class TestQuery(TestCase):
    def setUp(self) -> None:
        self.action = Query()
        self.connection = Connection()
        self.connection.conn_str = "postgres://user:password@127.0.0.1:5432/localhost"
        self.connection.type = "postgres"

        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action loger")
        self.params = {"parameters": {}, "query": "select DB_NAME()"}

    @mock.patch("komand_sql.connection.connection.SQLConnection", return_value=MagicMock())
    def test_query(self, sql_connection):
        query_action = self.action.run(self.params)
        expected_response = {
            "status": "successfully inserted",
            "results": [],
            "header": [],
        }
        self.assertEqual(query_action["results"], expected_response["results"])
        self.assertEqual(query_action["header"], expected_response["header"])
        self.assertTrue(expected_response["status"], query_action["status"])
