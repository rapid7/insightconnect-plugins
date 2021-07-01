import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.advanced_query_on_log_set import AdvancedQueryOnLogSet
from komand_rapid7_insightidr.actions.advanced_query_on_log_set.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch


@patch("requests.Session.get", side_effect=Util.mocked_requests)
@patch("aiohttp.ClientSession.get", side_effect=Util.mocked_async_requests)
class TestAdvancedQueryOnLogSet(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AdvancedQueryOnLogSet())

    def test_advanced_query_on_log_set_one_label(self, mock_get, mock_async_get):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG_SET: "log_set",
            }
        )
        expected = ["Out of order entry"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_set_two_label(self, mock_get, mock_async_get):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG_SET: "log_set2",
            }
        )
        expected = ["Out of order entry", "Out of events"]

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_set_without_label(self, mock_get, mock_async_get):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG_SET: "log_set3",
            }
        )
        expected = []

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)

    def test_advanced_query_on_log_set_wrong_label(self, mock_get, mock_async_get):
        actual = self.action.run(
            {
                Input.QUERY: "",
                Input.LOG_SET: "log_set4",
            }
        )
        expected = []

        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(actual.get(Output.RESULTS)[0].get("labels"), expected)
