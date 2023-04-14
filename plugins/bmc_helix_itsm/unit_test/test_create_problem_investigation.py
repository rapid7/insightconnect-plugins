import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_bmc_helix_itsm.actions.createProblemInvestigation import CreateProblemInvestigation


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateProblemInvestigation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateProblemInvestigation())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/create_problem_investigation.json.inp"),
                Util.read_file_to_dict("expected/create_problem_investigation.json.exp"),
            ],
        ]
    )
    def test_create_problem_investigation(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_service_type",
                Util.read_file_to_dict("inputs/create_problem_investigation_incorrect_name.json.inp"),
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ]
        ]
    )
    def test_create_problem_investigation_raise_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
