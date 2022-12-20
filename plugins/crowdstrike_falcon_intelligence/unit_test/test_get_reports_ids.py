import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_crowdstrike_falcon_intelligence.actions.getReportsIDs import GetReportsIDs


@patch("requests.request", side_effect=Util.mock_request)
class TestGetReportsIDs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetReportsIDs())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/get_reports_ids.json.inp"),
                Util.read_file_to_dict("expected/get_reports_ids.json.exp"),
            ]
        ]
    )
    def test_get_reports_ids(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_filter",
                Util.read_file_to_dict("inputs/get_reports_ids_invalid_filter.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ]
        ]
    )
    def test_get_reports_ids_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
