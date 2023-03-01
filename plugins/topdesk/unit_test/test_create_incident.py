import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_topdesk.actions.createIncident import CreateIncident
from icon_topdesk.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateIncident(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateIncident())

    @parameterized.expand(
        [
            [
                "correct_fields",
                Util.read_file_to_dict("inputs/create_incident_correct.json.inp"),
                Util.read_file_to_dict("expected/create_incident_correct.json.exp"),
            ]
        ]
    )
    def test_create_incident(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found_object",
                Util.read_file_to_dict("inputs/create_incident_not_found_object.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ],
            [
                "missing_required_field",
                Util.read_file_to_dict("inputs/create_incident_missing_required_field.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ],
            [
                "invalid_field",
                Util.read_file_to_dict("inputs/create_incident_invalid_field.json.inp"),
                Cause.INVALID_REQUEST,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_create_incident_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
