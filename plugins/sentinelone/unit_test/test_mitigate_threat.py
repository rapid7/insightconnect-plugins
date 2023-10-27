import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.mitigate_threat import MitigateThreat
from util import Util
from unittest import TestCase


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMitigateThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MitigateThreat())

    @parameterized.expand(
        [
            [
                "mitigate_threat_rollback",
                Util.read_file_to_dict("inputs/mitigate_threat_rollback.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mitigate_threat_quarantine",
                Util.read_file_to_dict("inputs/mitigate_threat_quarantine.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mitigate_threat_kill",
                Util.read_file_to_dict("inputs/mitigate_threat_kill.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mitigate_threat_remediate",
                Util.read_file_to_dict("inputs/mitigate_threat_remediate.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
            [
                "mitigate_threat_unquarantine",
                Util.read_file_to_dict("inputs/mitigate_threat_unquarantine.json.inp"),
                Util.read_file_to_dict("expected/agents_action.json.exp"),
            ],
        ]
    )
    def test_mitigate_threat(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "mitigate_threat_invalid_id",
                Util.read_file_to_dict("inputs/mitigate_threat_invalid_id.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_mitigate_threat_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
