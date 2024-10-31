import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_crowdstrike_falcon_intelligence.actions.submitAnalysis import SubmitAnalysis
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestSubmitAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitAnalysis())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/submit_analysis.json.inp"),
                Util.read_file_to_dict("expected/submit_analysis.json.exp"),
            ]
        ]
    )
    def test_submit_analysis(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_filter",
                Util.read_file_to_dict("inputs/submit_analysis_url_and_hash.json.inp"),
                "Sha256 and URL parameters used together",
                "Please provide sha256 or URL parameter (not both) and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_submit_analysis_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
