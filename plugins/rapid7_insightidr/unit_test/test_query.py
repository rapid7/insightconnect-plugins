import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.query.action import Query
from komand_rapid7_insightidr.actions.query.schema import Input, QueryInput, QueryOutput
from komand_rapid7_insightidr.connection.schema import Input as ConnectionInput

from mock_utils import mock_get_request
from util import Util


class TestQuery(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.params = {
            "id": "1b1a111d-d1fb-1a12-1651-eb1ff61a651a",
            "not_found_id": "22b2b22b-222b-222b-2222-b2bb2bbb2b2b",
            "id_202_error": "33b3b3b-333b-333b-3333-b3bb3bbb3b3b",
            "id_202": "55b5b5b-555b-5555-b5bb5bbb5b5b",
            "id_key_error": "44b4b4b-444b-4444-b4bb4bbb4b4b",
            "most_recent_first_true": True,
            "most_recent_first_false": False,
        }
        cls.connection_params = {
            ConnectionInput.REGION: "United States 1",
            ConnectionInput.API_KEY: {"secretKey": "api_key"},
        }

    def setUp(self) -> None:
        self.action = Util.default_connector(Query())
        self.connection = self.action.connection

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("id"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false"),
        }
        validate(test_input, QueryInput.schema)
        actual = self.action.run(test_input)
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
        validate(actual, QueryOutput.schema)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query_true(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("id"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_true"),
        }
        validate(test_input, QueryInput.schema)
        actual = self.action.run(test_input)
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
        validate(actual, QueryOutput.schema)

    @patch("requests.Session.send", side_effect=mock_get_request)
    @patch("time.time", return_value=1682954418)
    def test_query_true_future(self, _mock_req, mock_time) -> None:
        test_input = {
            Input.ID: self.params.get("id"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_true"),
        }
        validate(test_input, QueryInput.schema)
        actual = self.action.run(test_input)
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
        validate(actual, QueryOutput.schema)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query_202(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("id_202"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_true"),
        }
        validate(test_input, QueryInput.schema)
        actual = self.action.run(test_input)
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
        validate(actual, QueryOutput.schema)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query_202_error(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("id_202_error"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false"),
        }
        validate(test_input, QueryInput.schema)
        with self.assertRaises(PluginException) as exception:
            self.action.run(test_input)
        cause = "The response from InsightIDR was not in the correct format."
        self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query_not_found(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("not_found_id"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false"),
        }
        validate(test_input, QueryInput.schema)
        with self.assertRaises(PluginException) as exception:
            self.action.run(test_input)
        cause = "InsightIDR returned a status code of 404: Not Found"
        self.assertEqual(exception.exception.cause, cause)

    @patch("requests.Session.send", side_effect=mock_get_request)
    def test_query_key_error(self, _mock_req) -> None:
        test_input = {
            Input.ID: self.params.get("id_key_error"),
            Input.MOST_RECENT_FIRST: self.params.get("most_recent_first_false"),
        }
        validate(test_input, QueryInput.schema)
        with self.assertRaises(PluginException) as exception:
            self.action.run(test_input)
        cause = "The response from InsightIDR was not in the correct format."
        self.assertEqual(exception.exception.cause, cause)
