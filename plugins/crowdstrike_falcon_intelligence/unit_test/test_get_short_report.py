import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_crowdstrike_falcon_intelligence.actions.getShortReport import GetShortReport


@patch("requests.request", side_effect=Util.mock_request)
class TestGetShortReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetShortReport())

    @parameterized.expand(
        [
            [
                "single_id",
                Util.read_file_to_dict("inputs/get_short_report.json.inp"),
                Util.read_file_to_dict("expected/get_short_report.json.exp"),
            ],
            [
                "many_ids",
                Util.read_file_to_dict("inputs/get_short_report_many_ids.json.inp"),
                Util.read_file_to_dict("expected/get_short_report_many_ids.json.exp"),
            ],
        ]
    )
    def test_get_short_report(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/get_short_report_invalid_id.json.inp"),
                "Reports {reports_ids} not found.",
                "Please provide valid report IDs and if the issue persists, contact support.",
            ]
        ]
    )
    def test_get_short_report_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause.format(reports_ids=input_parameters.get("ids")))
        self.assertEqual(error.exception.assistance, assistance)
