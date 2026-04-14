import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

_this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _this_dir)
sys.path.insert(0, os.path.join(_this_dir, ".."))

from util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.add_request import AddRequest


@patch("requests.request", side_effect=Util.mock_request)
class TestAddRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddRequest())

    @parameterized.expand(
        [
            [
                "many_parameters",
                Util.read_file_to_dict("inputs/add_request_many_parameters.json.inp"),
                Util.read_file_to_dict("expected/add_request.json.exp"),
            ],
            [
                "few_parameters",
                Util.read_file_to_dict("inputs/add_request_few_parameters.json.inp"),
                Util.read_file_to_dict("expected/add_request.json.exp"),
            ],
        ]
    )
    def test_add_request(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "incorrect_level",
                Util.read_file_to_dict("inputs/add_request_incorrect_level.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                Util.read_file_to_dict("expected/add_request_incorrect_level.json.exp"),
            ],
            [
                "missing_requester",
                Util.read_file_to_dict("inputs/add_request_missing_requester.json.inp"),
                "Requester parameter not provided.",
                "Please provide a Requester parameter and try again. If the issue persists, please contact support.",
                "",
            ],
        ]
    )
    def test_add_request_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
