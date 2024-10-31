import os
import sys
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

sys.path.append(os.path.abspath("../"))

from icon_crowdstrike_falcon_intelligence.actions.getFullReport import GetFullReport
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestGetFullReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFullReport())

    @parameterized.expand(
        [
            [
                "single_id",
                Util.read_file_to_dict("inputs/get_full_report.json.inp"),
                Util.read_file_to_dict("expected/get_full_report.json.exp"),
            ],
            [
                "many_ids",
                Util.read_file_to_dict("inputs/get_full_report_many_ids.json.inp"),
                Util.read_file_to_dict("expected/get_full_report_many_ids.json.exp"),
            ],
        ]
    )
    def test_get_full_report(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/get_full_report_invalid_id.json.inp"),
                "Reports {reports_ids} not found.",
                "Please provide valid report IDs and if the issue persists, contact support.",
            ]
        ]
    )
    def test_get_full_report_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause.format(reports_ids=input_parameters.get("ids")))
        self.assertEqual(error.exception.assistance, assistance)
