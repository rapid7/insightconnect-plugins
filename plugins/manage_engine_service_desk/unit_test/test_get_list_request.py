import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_manage_engine_service_desk.actions.get_list_request import GetListRequest


@patch("requests.request", side_effect=Util.mock_request)
class TestGetListRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetListRequest())

    @parameterized.expand(
        [
            [
                "valid_parameters",
                Util.read_file_to_dict("inputs/get_list_request.json.inp"),
                Util.read_file_to_dict("expected/get_list_request.json.exp"),
            ],
            ["no_parameters", {}, Util.read_file_to_dict("expected/get_list_request.json.exp")],
        ]
    )
    def test_get_list_request(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_sort_field",
                Util.read_file_to_dict("inputs/get_list_request_invalid_sort_field.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                Util.read_file_to_dict("expected/get_list_request_invalid_sort_field.json.exp"),
            ]
        ],
    )
    def test_get_list_request_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
