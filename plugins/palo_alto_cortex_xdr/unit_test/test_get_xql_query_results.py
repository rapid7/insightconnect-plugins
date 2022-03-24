import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_palo_alto_cortex_xdr.connection.connection import Connection
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results import GetXqlQueryResults
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results.schema import Input
import json
import logging

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    mocked_request,
)

class TestGetEndpointDetails(TestCase):

    def setUp(self) -> None:
        self.log = logging.getLogger("Test")

        self.test_conn = Connection()
        self.test_conn.logger = self.log
        self.test_conn.connect(STUB_CONNECTION)

        self.test_action = GetXqlQueryResults()
        self.test_action.logger = self.log
        self.test_action.connection = self.test_conn

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_xql_query_results1(self, mock_post):


        actual = self.test_action.run(
            {
                Input.END_TIME_RANGE: 1599080399000,
                Input.LIMIT: 20,
                Input.QUERY: "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
                Input.START_TIME_RANGE: 1598907600000,
                Input.TENANTS: []
            }
        )

        expected = {
            "reply": {
                "status": "SUCCESS",
                "number_of_results": 0,
                "query_cost": {
                    "1098781949": 0.0013580555555555555
                },
                "remaining_quota": 4.991908888888889,
                "results": {
                    "data": []
                }
            }
        }

        self.assertEqual(actual, expected)

    def test_get_xql_query_results(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetXqlQueryResults()
        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_xql_query_results.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        print(results)
        self.assertIsNotNone(results)
