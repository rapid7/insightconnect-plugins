import os
import sys
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from icon_crowdstrike_falcon_intelligence.actions.checkAnalysisStatus import CheckAnalysisStatus
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestCheckAnalysisStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CheckAnalysisStatus())

    @parameterized.expand(
        [
            [
                "single_id",
                Util.read_file_to_dict("inputs/check_analysis_status.json.inp"),
                Util.read_file_to_dict("expected/check_analysis_status.json.exp"),
            ],
            [
                "many_ids",
                Util.read_file_to_dict("inputs/check_analysis_status_many_ids.json.inp"),
                Util.read_file_to_dict("expected/check_analysis_status_many_ids.json.exp"),
            ],
        ]
    )
    def test_check_analysis_status(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/check_analysis_status_invalid_ids.json.inp"),
                "Analysis {analysis_ids} not found.",
                "Please provide valid analysis IDs and if the issue persists, contact support.",
            ]
        ]
    )
    def test_check_analysis_status_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause.format(analysis_ids=input_parameters.get("ids")))
        self.assertEqual(error.exception.assistance, assistance)
