import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightidr.actions.list_alerts_for_investigation import ListAlertsForInvestigation
from komand_rapid7_insightidr.actions.list_alerts_for_investigation.schema import Input
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from unit_test.mock import mock_get_request, STUB_INVESTIGATION_IDENTIFIER
from unit_test.util import Util


class TestCreateInvestigation(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "query_id": "00000000-0000-1eec-0000-000000000000",
            "not_found_query_id": "00000000-0000-8eec-0000-000000000000",
            "invalid_query_id": "0000000-000-9ee-000-00000000000",
        }
        self.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(ListAlertsForInvestigation())
        self.connection = self.action.connection

    @patch("requests.Session.get", side_effect=mock_get_request)
    def test_list_alerts_for_investigation(self, _mock_req):
        actual = self.action.run({Input.ID: STUB_INVESTIGATION_IDENTIFIER})
        expected = {
            "alerts": [
                {
                    "alert_type": "Example Type",
                    "alert_type_description": "Example Description",
                    "created_time": "01-01-2020T00:00:00",
                    "detection_rule_rrn": "rrn:example",
                    "first_event_time": "01-01-2020T00:00:00",
                    "id": "11111111-1111-1111-1111-111111111111",
                    "latest_event_time": "01-01-2020T00:00:00",
                    "title": "Example Title",
                }
            ],
            "metadata": {"index": 0, "size": 1, "total_data": 1, "total_pages": 1},
        }
        self.assertEqual(actual, expected)
