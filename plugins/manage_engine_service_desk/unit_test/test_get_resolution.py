import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.get_resolution import GetResolution


@patch("requests.request", side_effect=Util.mock_request)
class TestGetResolution(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetResolution())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/get_resolution.json.inp"),
                Util.read_file_to_dict("expected/get_resolution.json.exp"),
            ]
        ]
    )
    def test_get_resolution(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "request_not_found",
                Util.read_file_to_dict("inputs/get_resolution_request_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/request_not_found.json.exp"),
            ]
        ]
    )
    def test_get_resolution_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
