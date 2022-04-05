import sys
import os

sys.path.append(os.path.abspath("../"))

import logging
import time

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results.schema import Input
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results import GetXqlQueryResults
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import (
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_402,
    mock_request_400,
    mock_request_404,
    mocked_request,
)


class TestGetEndpointDetails(TestCase):
    def setUp(self) -> None:
        self.log = logging.getLogger("Test")
        self.test_conn, self.test_action = Util.default_connector(GetXqlQueryResults())
        self.test_params = {
            Input.END_TIME: 1599080399000,
            Input.LIMIT: 1000,
            Input.QUERY: "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
            Input.START_TIME: 1598907600000,
            Input.TENANTS: ["user1"],
        }

    @patch("requests.post", side_effect=mock_request_200)
    def test_get_xql_query_results(self, _mock_req):
        actual = self.test_action.run(self.test_params)
        expected = {
            "reply": {
                "status": "SUCCESS",
                "number_of_results": 3,
                "query_cost": {"user1": 0.001596388888888889},
                "remaining_quota": 4.998403611111111,
                "results": {
                    "data": [
                        {
                            "event_id": "eventID1",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825324,
                            "_time": 1621541523000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID2",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825326,
                            "_time": 1621541528000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID3",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825325,
                            "_time": 1621541517000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                    ]
                },
            }
        }
        self.assertEqual(expected, actual)

    @patch("requests.post", side_effect=mock_request_200)
    def test_get_xql_query_results_absent_to(self, _mock_req):
        self.test_params[Input.END_TIME] = None
        actual = self.test_action.run(self.test_params)

        expected = {
            "reply": {
                "status": "SUCCESS",
                "number_of_results": 3,
                "query_cost": {"user1": 0.001596388888888889},
                "remaining_quota": 4.998403611111111,
                "results": {
                    "data": [
                        {
                            "event_id": "eventID1",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825324,
                            "_time": 1621541523000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID2",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825326,
                            "_time": 1621541528000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID3",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825325,
                            "_time": 1621541517000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                    ]
                },
            }
        }

        self.assertEqual(expected, actual)

    @patch("requests.post", side_effect=mock_request_200)
    def test_get_xql_query_results_absent_from(self, _mock_req):
        self.test_params[Input.START_TIME] = None
        actual = self.test_action.run(self.test_params)

        expected = {
            "reply": {
                "status": "SUCCESS",
                "number_of_results": 3,
                "query_cost": {"user1": 0.001596388888888889},
                "remaining_quota": 4.998403611111111,
                "results": {
                    "data": [
                        {
                            "event_id": "eventID1",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825324,
                            "_time": 1621541523000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID2",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825326,
                            "_time": 1621541528000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                        {
                            "event_id": "eventID3",
                            "_vendor": "PANW",
                            "_product": "Fusion",
                            "insert_timestamp": 1621541825325,
                            "_time": 1621541517000,
                            "event_type": "STORY",
                            "event_sub_type": "NULL",
                        },
                    ]
                },
            }
        }

        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            (mock_request_200, 1599080399000, 1598907600000),
            (mock_request_200, 1598907600000, 1598907600000),
            (mock_request_200, int((time.time() * 1000) + 100), 1599080399000),
            (mock_request_200, 1598907600000, int((time.time() * 1000) + 100)),
        ]
    )
    def test_get_xql_query_results_bad_to_from(self, _mock_req, from_, to):
        mocked_request(_mock_req)
        self.test_params[Input.START_TIME] = from_
        self.test_params[Input.END_TIME] = to
        expected_cause = "Invalid 'Start Time' or 'End Time' time range inputs"
        expected_assistance = f"'Start Time' or 'End Time' must be valid Unix timestamps in epoch milliseconds, they must be past timestamps, and 'End Time' must be more recent than 'Start Time'"
        expected_data = f"'From'= {from_}, 'To'= {to}"
        with self.assertRaises(PluginException) as context:
            self.test_action.run(self.test_params)
        self.assertEqual(expected_cause, context.exception.cause)
        self.assertEqual(expected_assistance, context.exception.assistance)
        self.assertEqual(expected_data, context.exception.data)

    @parameterized.expand([(mock_request_200, 1001), (mock_request_200, 0)])
    def test_get_xql_query_results_bad_limit(self, _mock_req, limit):
        mocked_request(_mock_req)
        self.test_params[Input.LIMIT] = limit
        expected_cause = f"A limit of {limit} is an invalid input value"
        expected_assistance = "Limit input value must be between 1 and 1000"
        with self.assertRaises(PluginException) as context:
            self.test_action.run(self.test_params)
        self.assertEqual(expected_cause, context.exception.cause)
        self.assertEqual(expected_assistance, context.exception.assistance)

    @parameterized.expand(
        [
            (mock_request_400, "API Error. API returned 400", "Bad request, invalid JSON."),
            (mock_request_401, "API Error. API returned 401", "Authorization failed. Check your API Key ID & API Key."),
            (
                mock_request_402,
                "API Error. API returned 402",
                "Unauthorized access. User does not have the required " "license type to run this API.",
            ),
            (
                mock_request_403,
                "API Error. API returned 403",
                "Forbidden. The provided API Key does not have the " "required RBAC permissions to run this API.",
            ),
            (
                mock_request_404,
                "API Error. API returned 404",
                "The object at https://example.com/public_api/v1/xql"
                "/start_xql_query/ does not exist. Check the FQDN "
                "connection setting and try again.",
            ),
        ],
    )
    def test_get_xql_query_results_bad_response(self, _mock_req, cause, assistance):
        mocked_request(_mock_req)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(self.test_params)
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
