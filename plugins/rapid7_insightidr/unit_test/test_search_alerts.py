import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.search_alerts import SearchAlerts
from komand_rapid7_insightidr.actions.search_alerts.schema import (
    Input,
    SearchAlertsInput,
    SearchAlertsOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestSearchAlerts(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchAlerts())

    @parameterized.expand(Util.load_parameters("search_alerts").get("parameters"))
    def test_search_alerts(
        self,
        mock_request,
        start_time,
        end_time,
        leql,
        terms,
        sorts,
        field_ids,
        aggregates,
        size,
        index,
        rrns_only,
        expected,
    ):
        test_input = {
            Input.START_TIME: start_time,
            Input.END_TIME: end_time,
            Input.LEQL: leql,
            Input.TERMS: terms,
            Input.SORTS: sorts,
            Input.FIELD_IDS: field_ids,
            Input.AGGREGATES: aggregates,
            Input.SIZE: size,
            Input.INDEX: index,
            Input.RRNS_ONLY: rrns_only,
        }
        validate(test_input, SearchAlertsInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, SearchAlertsInput.schema)

    @parameterized.expand(Util.load_parameters("search_alerts_bad_times").get("parameters"))
    def test_search_alerts_bad_times(self, mock_request, start_time, end_time, cause, assistance):
        test_input = {Input.START_TIME: start_time, Input.END_TIME: end_time}
        validate(test_input, SearchAlertsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
