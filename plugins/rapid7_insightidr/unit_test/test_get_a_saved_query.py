import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_rapid7_insightidr.actions.get_a_saved_query.action import GetASavedQuery
from komand_rapid7_insightidr.actions.get_a_saved_query.schema import Input, GetASavedQueryInput, GetASavedQueryOutput
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from mock import (
    mock_get_request,
)
from jsonschema import validate


class TestGetASavedQuery(TestCase):
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
        self.action = Util.default_connector(GetASavedQuery())
        self.connection = self.action.connection

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_get_a_saved_query(self, _mock_req):
        test_input = {Input.QUERY_ID: self.params.get("query_id")}
        validate(test_input, GetASavedQueryInput.schema)
        actual = self.action.run(test_input)
        expected = {
            "saved_query": {
                "id": "00000000-0000-1eec-0000-000000000000",
                "leql": {
                    "during": {"from": 1234567890, "time_range": "yesterday", "to": 1234567890},
                    "statement": "where(931dde6c60>=800)",
                },
                "logs": ["31a4d56e-460e-460f-9542-c2bc8edd7c6b"],
                "name": "Large Values Yesterday",
            }
        }
        self.assertEqual(actual, expected)
        validate(actual, GetASavedQueryOutput.schema)

    def test_get_a_saved_query_invalid_query_id(self):
        test_input = {Input.QUERY_ID: self.params.get("invalid_query_id")}
        validate(test_input, GetASavedQueryInput.schema)
        with self.assertRaises(PluginException) as exception:
            self.action.run(test_input)
        cause = "Query ID field did not contain a valid UUID."
        self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_get_a_saved_query_not_found(self, _mock_req):
        test_input = {Input.QUERY_ID: self.params.get("not_found_query_id")}
        validate(test_input, GetASavedQueryInput.schema)
        with self.assertRaises(PluginException) as exception:
            self.action.run(test_input)
        cause = "InsightIDR returned a status code of 404: Not Found"
        self.assertEqual(exception.exception.cause, cause)
