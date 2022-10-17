import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.close_request import CloseRequest


@patch("requests.request", side_effect=Util.mock_request)
class TestCloseRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CloseRequest())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/close_request.json.inp"),
                Util.read_file_to_dict("expected/close_request.json.exp"),
            ],
        ]
    )
    def test_close_request(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "request_not_found",
                Util.read_file_to_dict("inputs/close_request_request_not_found.json.inp"),
                "Resource not found.",
                "Please verify inputs and if the issue persists, contact support.",
                Util.read_file_to_dict("expected/request_not_found.json.exp"),
            ],
            [
                "request_already_closed",
                Util.read_file_to_dict("inputs/close_request_request_already_closed.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                Util.read_file_to_dict("expected/close_request_request_already_closed.json.exp"),
            ],
        ]
    )
    def test_close_request_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
