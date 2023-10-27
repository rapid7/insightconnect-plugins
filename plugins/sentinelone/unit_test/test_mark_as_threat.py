import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.mark_as_threat import MarkAsThreat
from util import Util
from unittest import TestCase


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMarkAsThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MarkAsThreat())

    @parameterized.expand(
        [
            [
                "mark_as_threat_1",
                Util.read_file_to_dict("inputs/mark_as_threat_1.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mark_as_threat_2",
                Util.read_file_to_dict("inputs/mark_as_threat_2.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mark_as_threat_3",
                Util.read_file_to_dict("inputs/mark_as_threat_3.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mark_as_threat_4",
                Util.read_file_to_dict("inputs/mark_as_threat_4.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
        ]
    )
    def test_mark_as_threat(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "mark_as_threat_invalid_id",
                Util.read_file_to_dict("inputs/mark_as_threat_invalid_id.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_mark_as_threat_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
