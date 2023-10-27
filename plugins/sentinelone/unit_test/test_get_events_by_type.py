import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.get_events_by_type import GetEventsByType
from util import Util
from unittest import TestCase
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetEventsByType(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetEventsByType())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/get_events_by_type_success.json.inp"),
                Util.read_file_to_dict("expected/get_events_by_type_success.json.exp"),
            ],
            [
                "success_with_limit",
                Util.read_file_to_dict("inputs/get_events_by_type_success_with_limit.json.inp"),
                Util.read_file_to_dict("expected/get_events_by_type_success_with_limit.json.exp"),
            ],
            [
                "success_with_sub_query",
                Util.read_file_to_dict("inputs/get_events_by_type_success_with_sub_query.json.inp"),
                Util.read_file_to_dict("expected/get_events_by_type_success_with_sub_query.json.exp"),
            ],
        ]
    )
    def test_get_events_by_type(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "query_not_found",
                Util.read_file_to_dict("inputs/get_events_by_type_query_not_found.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
            [
                "invalid_sub_query",
                Util.read_file_to_dict("inputs/get_events_by_type_invalid_sub_query.json.inp"),
                PluginException.causes[PluginException.Preset.SERVER_ERROR],
                PluginException.assistances[PluginException.Preset.SERVER_ERROR],
            ],
        ]
    )
    def test_get_events_by_type_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
