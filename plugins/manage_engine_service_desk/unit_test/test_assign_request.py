import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.assign_request import AssignRequest


@patch("requests.request", side_effect=Util.mock_request)
class TestAssignRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AssignRequest())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/assign_request.json.inp"),
                Util.read_file_to_dict("expected/assign_request.json.exp"),
            ],
        ]
    )
    def test_assign_request(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "request_not_found",
                Util.read_file_to_dict("inputs/assign_request_request_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/request_not_found.json.exp"),
            ],
            [
                "not_enough_parameters",
                Util.read_file_to_dict("inputs/assign_request_not_enough_parameters.json.inp"),
                "Not enough input parameters were provided.",
                "Please provide at least one input parameter except request id and try again. If the issue persists, please contact support.",
                "",
            ],
        ]
    )
    def test_assign_request_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
