import sys
import os
from unittest.mock import patch
from komand_proofpoint_tap.actions.get_all_threats import GetAllThreats
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.util.exceptions import ApiException
from test_util import Util
from unittest import TestCase
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetAllThreats(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAllThreats())

    @parameterized.expand(
        [
            [
                "all_threats",
                Util.read_file_to_dict("inputs/get_all_threats.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats.json.exp"),
            ],
            [
                "all_threats_status_active",
                Util.read_file_to_dict("inputs/get_all_threats_status_active.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats_status_active.json.exp"),
            ],
            [
                "all_threats_status_cleared",
                Util.read_file_to_dict("inputs/get_all_threats_status_cleared.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats_status_cleared.json.exp"),
            ],
            [
                "all_threats_without_time_start",
                Util.read_file_to_dict("inputs/get_all_threats_without_time_start.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats_without_time_start.json.exp"),
            ],
            [
                "all_threats_without_time_end",
                Util.read_file_to_dict("inputs/get_all_threats_without_time_end.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats_without_time_end.json.exp"),
            ],
            [
                "all_threats_without_time_start_end",
                Util.read_file_to_dict("inputs/get_all_threats_without_time_start_end.json.inp"),
                Util.read_file_to_dict("expected/get_all_threats_without_time_start_end.json.exp"),
            ],
        ]
    )
    def test_get_all_threats(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "all_threats_timerange_invalid",
                Util.read_file_to_dict("inputs/get_all_threats_timerange_invalid.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_get_all_threats_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
