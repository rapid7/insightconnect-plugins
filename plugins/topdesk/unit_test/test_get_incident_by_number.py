import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from util import Util
from parameterized import parameterized
from icon_topdesk.actions.getIncidentByNumber.action import GetIncidentByNumber
from icon_topdesk.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestGetIncidentByNumber(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIncidentByNumber())

    @parameterized.expand(
        [
            [
                "existing_number_1",
                Util.read_file_to_dict("inputs/get_incident_by_number_found.json.inp"),
                Util.read_file_to_dict("expected/get_incident_by_number_found.json.exp"),
            ]
        ]
    )
    def test_get_incident_by_number(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "non_existing_number",
                Util.read_file_to_dict("inputs/get_incident_by_number_non_existing.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "invalid_number",
                Util.read_file_to_dict("inputs/get_incident_by_number_invalid.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_get_incident_by_number_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
