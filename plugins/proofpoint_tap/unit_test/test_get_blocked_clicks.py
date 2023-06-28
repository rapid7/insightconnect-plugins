import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.actions.get_blocked_clicks import GetBlockedClicks
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.util.exceptions import ApiException
from test_util import Util
from unittest import TestCase
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetBlockedClicks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetBlockedClicks())

    @parameterized.expand(
        [
            [
                "blocked_clicks",
                Util.read_file_to_dict("inputs/get_blocked_clicks.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks.json.exp"),
            ],
            [
                "blocked_clicks_cleared_status",
                Util.read_file_to_dict("inputs/get_blocked_clicks_cleared_status.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks_cleared_status.json.exp"),
            ],
            [
                "blocked_clicks_without_url",
                Util.read_file_to_dict("inputs/get_blocked_clicks_without_url.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks_without_url.json.exp"),
            ],
            [
                "blocked_clicks_without_time_start",
                Util.read_file_to_dict("inputs/get_blocked_clicks_without_time_start.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks_without_time_start.json.exp"),
            ],
            [
                "blocked_clicks_without_time_end",
                Util.read_file_to_dict("inputs/get_blocked_clicks_without_time_end.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks_without_time_end.json.exp"),
            ],
            [
                "blocked_clicks_without_time_start_end",
                Util.read_file_to_dict("inputs/get_blocked_clicks_without_time_start_end.json.inp"),
                Util.read_file_to_dict("expected/get_blocked_clicks_without_time_start_end.json.exp"),
            ],
        ]
    )
    def test_get_blocked_clicks(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "blocked_clicks_timerange_invalid",
                Util.read_file_to_dict("inputs/get_blocked_clicks_timerange_invalid.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_get_blocked_clicks_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
