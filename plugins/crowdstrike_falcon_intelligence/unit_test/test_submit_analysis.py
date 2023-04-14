import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_crowdstrike_falcon_intelligence.actions.submitAnalysis import SubmitAnalysis


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
    def test_submit_analysis(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
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
    def test_submit_analysis_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
