import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_rapid7_insightidr.actions.query.action import Query
from komand_rapid7_insightidr.actions.query.schema import Input
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unit_test.mock import mock_get_request


class TestQuery(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "id": "1b1a111d-d1fb-1a12-1651-eb1ff61a651a",
            "not_found_id": "22b2b22b-222b-222b-2222-b2bb2bbb2b2b",
            "most_recent_first_true": True,
            "most_recent_first_false": False,
        }
        self.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(Query())
        self.connection = self.action.connection

    @patch("requests.Session.get", side_effect=mock_get_request)
    def test_query(self, _mock_req):
        actual = self.action.run(
            {Input.ID: self.params.get("id"), Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false")}
        )
        expected = {
            "events": [
                {
                    "labels": [],
                    "log_id": "1b1a111d-d1fb-1a12-1651-eb1ff61a651a",
                    "message": {
                        "computerName": "iagent1-win10",
                        "eventCode": 1111,
                        "eventData": {
                            "data": [],
                            "engineVersion": "1.1.17300.4",
                            "platformVersion": "4.18.2007.8",
                            "productName": "%827",
                            "signatureVersion": "1.321.836.0",
                            "unused": "null",
                        },
                        "isDomainController": "false",
                        "sid": "S-1-5-18",
                        "sourceName": "Microsoft-Windows-Windows Defender",
                        "timeWritten": "2020-08-07T21:44:12.335999900Z",
                    },
                    "sequence_number": 1211198512587571200,
                    "sequence_number_str": "1211198512587571200",
                    "timestamp": 1596836653511,
                }
            ]
        }
        self.assertEqual(actual, expected)

    @patch("requests.Session.get", side_effect=mock_get_request)
    def test_query_not_found(self, _mock_req):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {
                    Input.ID: self.params.get("not_found_id"),
                    Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false"),
                }
            )
        cause = "InsightIDR returned a status code of 404: Not Found"
        self.assertEqual(exception.exception.cause, cause)
