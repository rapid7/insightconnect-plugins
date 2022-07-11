import sys
import os
import logging

sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from komand_sql.connection.connection import Connection
from komand_sql.actions.query.action import Query
from komand_sql.actions.query.schema import Input

from unit_test.mock import (
    mock_execute,
    STUB_CONNECTION,
)



class TestQuery(TestCase):
    def setUp(self) -> None:
        print("Set up beginning...")
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection Logger")
        self.connection.connect(STUB_CONNECTION)
        self.action = Query()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

        self.params = {
            Input.QUERY: "SELECT * FROM test_data_table",
            Input.PARAMETERS: {}
        }

    @mock.patch("komand_sql.util.util.generate_results", return_value = {"header": ""})
    @mock.patch("sqlalchemy.orm.session.Session.execute", side_effect=mock_execute)
    def test_query_ok(self, generate_results, mock_execute):
        response = self.action.run(self.params)
        expected_response = {
            "success": {
                    "header": [
                    ],
                    "results": [
                    ],
                    "status": "successfully inserted"
            }
        }
        self.assertEqual(response["header"], expected_response["success"]["header"])
        self.assertEqual(response["results"], expected_response["success"]["results"])
        self.assertTrue(expected_response["success"]["status"], response["status"])
