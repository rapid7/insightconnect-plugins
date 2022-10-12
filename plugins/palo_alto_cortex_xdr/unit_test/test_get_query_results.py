import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Callable, Optional
from unittest import TestCase
from unittest.mock import patch

import timeout_decorator
from icon_palo_alto_cortex_xdr.triggers.get_query_results import GetQueryResults
from icon_palo_alto_cortex_xdr.triggers.get_query_results.schema import Input

from unit_test.mock import mock_request_200
from unit_test.util import MockTrigger, Util


def timeout_pass(error_callback: Optional[Callable] = None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError:
                if error_callback:
                    return error_callback()
                return None

        return func_wrapper

    return func_timeout


def check_error():
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
    if MockTrigger.actual == expected:
        return True

    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


class TestGetIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _, cls.action = Util.default_connector(GetQueryResults())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    @patch("requests.post", side_effect=mock_request_200)
    def test_get_incidents(self, mock_send, mock_post):
        self.action.run(
            {
                Input.LIMIT: 1000,
                Input.QUERY: "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
                Input.TENANTS: ["user1"],
            }
        )
