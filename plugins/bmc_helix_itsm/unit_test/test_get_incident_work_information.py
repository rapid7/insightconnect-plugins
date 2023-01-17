import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_bmc_helix_itsm.actions.getIncidentWorkInformation import GetIncidentWorkInformation


@patch("requests.request", side_effect=Util.mock_request)
class TestGetIncidentWorkInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetIncidentWorkInformation())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/get_incident_work_information.json.inp"),
                Util.read_file_to_dict("expected/get_incident_work_information.json.exp"),
            ],
        ]
    )
    def test_get_incident_work_information(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_service_type",
                Util.read_file_to_dict("inputs/get_incident_work_information_incident_not_found.json.inp"),
                "Incident INC00fake404 not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_get_incident_work_information_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
