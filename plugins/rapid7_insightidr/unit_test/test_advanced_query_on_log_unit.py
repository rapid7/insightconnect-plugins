import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.advanced_query_on_log import AdvancedQueryOnLog
from komand_rapid7_insightidr.actions.advanced_query_on_log.schema import (
    AdvancedQueryOnLogInput,
    AdvancedQueryOnLogOutput,
    Input,
    Output,
)

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
@patch("aiohttp.ClientSession.get", side_effect=Util.mocked_async_requests)
class TestAdvancedQueryOnLog(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AdvancedQueryOnLog())

    def test_advanced_query_on_log_one_label(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG: "example_log1",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)

        self.maxDiff = None
        expected = ["Out of order entry"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS_EVENTS)[0].get("labels"), expected)

        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_two_labels(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG: "example_log2",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)
        expected = ["Out of order entry", "Out of events"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS_EVENTS)[0].get("labels"), expected)

        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_without_label(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG: "example_log3",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)
        expected = []

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS_EVENTS)[0].get("labels"), expected)

        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_wrong_label(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG: "example_log4",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)
        expected = []

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS_EVENTS)[0].get("labels"), expected)

        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_statistical_result_calculate(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "where(hostname='WindowsX64') calculate(count)",
            Input.LOG: "example_log5",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)
        expected = {
            "count": 462,
            "results_statistical": {
                "leql": {
                    "during": {"from": 1699567413000, "to": 1699610613000},
                    "statement": "where(hostname='WindowsX64') calculate(count)",
                },
                "logs": ["553048ff-e6ab-4597-a3e0-2b24032c233e", "3244ed07-c3af-4bee-90b5-905a38a034b4"],
                "search_stats": {
                    "bytes_all": 6291099,
                    "bytes_checked": 3589232,
                    "duration_ms": 19,
                    "events_all": 1025,
                    "events_checked": 595,
                    "events_matched": 462,
                    "index_factor": 0.4294746,
                },
                "statistics": {
                    "all_exact_result": None,
                    "cardinality": 0,
                    "count": 462,
                    "from": 1699567413000,
                    "granularity": 4320000,
                    "groups": [],
                    "groups_timeseries": [],
                    "others": {},
                    "stats": {"global_timeseries": {"count": 462.0}},
                    "status": 200,
                    "timeseries": {
                        "global_timeseries": [
                            {"count": 38.0},
                            {"count": 47.0},
                            {"count": 36.0},
                            {"count": 56.0},
                            {"count": 60.0},
                            {"count": 40.0},
                            {"count": 39.0},
                            {"count": 41.0},
                            {"count": 61.0},
                            {"count": 44.0},
                        ]
                    },
                    "to": 1699610613000,
                    "type": "count",
                },
            },
        }

        self.assertEqual(actual, expected)
        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_statistical_result_groupby(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "groupby(r7_context.asset.name)",
            Input.LOG: "example_log7",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)

        actual = self.action.run(test_input)
        expected = {
            "count": 1020,
            "results_statistical": {
                "leql": {
                    "during": {"from": 1699569260000, "to": 1699612460000},
                    "statement": "groupby(r7_context.asset.name)",
                },
                "logs": ["553048ff-e6ab-4597-a3e0-2b24032c233e", "3244ed07-c3af-4bee-90b5-905a38a034b4"],
                "search_stats": {
                    "bytes_all": 6276329,
                    "bytes_checked": 6276329,
                    "duration_ms": 36,
                    "events_all": 1022,
                    "events_checked": 1022,
                    "events_matched": 1020,
                    "index_factor": 0.0,
                },
                "statistics": {
                    "all_exact_result": True,
                    "cardinality": 0,
                    "from": 1699569260000,
                    "granularity": 4320000,
                    "groups": [{"tomascybereasonsensor": {"count": 555.0}}, {"windowsx64": {"count": 465.0}}],
                    "groups_timeseries": [
                        {
                            "tomascybereasonsensor": {
                                "groups_timeseries": [],
                                "series": [
                                    {"count": 31.0},
                                    {"count": 37.0},
                                    {"count": 56.0},
                                    {"count": 25.0},
                                    {"count": 17.0},
                                    {"count": 273.0},
                                    {"count": 22.0},
                                    {"count": 38.0},
                                    {"count": 33.0},
                                    {"count": 23.0},
                                ],
                                "totals": {"count": 555.0},
                            }
                        },
                        {
                            "windowsx64": {
                                "groups_timeseries": [],
                                "series": [
                                    {"count": 28.0},
                                    {"count": 53.0},
                                    {"count": 42.0},
                                    {"count": 56.0},
                                    {"count": 57.0},
                                    {"count": 32.0},
                                    {"count": 46.0},
                                    {"count": 50.0},
                                    {"count": 54.0},
                                    {"count": 47.0},
                                ],
                                "totals": {"count": 465.0},
                            }
                        },
                    ],
                    "others": {"series": []},
                    "stats": {},
                    "status": 200,
                    "timeseries": {},
                    "to": 1699612460000,
                    "type": "count",
                },
            },
        }

        self.assertEqual(actual, expected)
        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_using_log_id(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG_ID: "123456-abcd-1234-abcd-123456abc",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }
        validate(test_input, AdvancedQueryOnLogInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual.get(Output.COUNT), 1)
        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_both_name_and_id(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.LOG_ID: "123456-abcd-1234-abcd-123456abc",
            Input.LOG: "example_log7",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }
        validate(test_input, AdvancedQueryOnLogInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual.get(Output.COUNT), 1)
        validate(actual, AdvancedQueryOnLogOutput.schema)

    def test_advanced_query_on_log_no_name_and_id(self, mock_get, mock_async_get) -> None:
        test_input = {
            Input.QUERY: "",
            Input.TIMEOUT: 60,
            Input.RELATIVE_TIME: "Last 5 Minutes",
        }

        validate(test_input, AdvancedQueryOnLogInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, "No values were provided for log id or log name")
        self.assertEqual(error.exception.assistance, "Please enter a valid value for either log id or log name")
