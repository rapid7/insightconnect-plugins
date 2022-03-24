import sys
import os

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results import GetXqlQueryResults
from icon_palo_alto_cortex_xdr.actions.get_xql_query_results.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util

import logging

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
            Input.END_TIME_RANGE: 1599080399000,
            Input.LIMIT: 20,
            Input.QUERY: "dataset=xdr_data | fields event_id, event_type, event_sub_type | limit 3",
            Input.START_TIME_RANGE: 1598907600000,
            Input.TENANTS: []
        }

    @patch("requests.post", side_effect=mock_request_200)
    def test_get_xql_query_results(self, _mock_req):
        actual = self.test_action.run(self.test_params)

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

        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            (mock_request_400, "API Error. API returned 400", "Bad request, invalid JSON."),
            (mock_request_401, "API Error. API returned 401", "Authorization failed. Check your API Key ID & API Key."),
            (mock_request_402, "API Error. API returned 402", "Unauthorized access. User does not have the required "
                                                              "license type to run this API."),
            (mock_request_403, "API Error. API returned 403", "Forbidden. The provided API Key does not have the "
                                                              "required RBAC permissions to run this API."),
            (mock_request_404, "API Error. API returned 404", "The object at https://example.com/public_api/v1/xql"
                                                              "/start_xql_query/ does not exist. Check the FQDN "
                                                              "connection setting and try again."),
        ],
    )
    def test_get_xql_query_results_bad(self, _mock_req, cause, assistance):
        mocked_request(_mock_req)
        with self.assertRaises(PluginException) as context:
            self.test_action.run(self.test_params)
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
