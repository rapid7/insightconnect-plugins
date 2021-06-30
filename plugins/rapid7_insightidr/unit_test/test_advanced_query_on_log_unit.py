import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.advanced_query_on_log import AdvancedQueryOnLog
from komand_rapid7_insightidr.actions.advanced_query_on_log.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch


@patch("requests.Session.get", side_effect=Util.mocked_requests)
class TestAdvancedQueryOnLog(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AdvancedQueryOnLog())

    def test_advanced_query_on_log_one_label(self, mock_post):
        actual = self.action.run({Input.QUERY: "", Input.LOG: "example_log1"})
        self.maxDiff = None
        expected = ["Out of order entry"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_two_labels(self, mock_post):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG: "example_log2",
            }
        )
        expected = ["Out of order entry", "Out of events"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_without_label(self, mock_post):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG: "example_log3",
            }
        )
        expected = None

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_wrong_label(self, mock_post):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG: "example_log4",
            }
        )
        expected = []

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)
