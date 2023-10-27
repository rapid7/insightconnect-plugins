import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from util import Util
from unittest import TestCase
from komand_sentinelone.actions.disable_agent import DisableAgent
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestDisableAgent(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DisableAgent())

    @parameterized.expand(
        [
            [
                "by_id",
                Util.read_file_to_dict("inputs/disable_agent_by_id.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "by_hostname",
                Util.read_file_to_dict("inputs/disable_agent_by_hostname.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "by_ip_address",
                Util.read_file_to_dict("inputs/disable_agent_by_ip_address.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "by_mac_address",
                Util.read_file_to_dict("inputs/disable_agent_by_mac_address.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "by_uuid",
                Util.read_file_to_dict("inputs/disable_agent_by_uuid.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "no_affected",
                Util.read_file_to_dict("inputs/disable_agent_no_affected.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
            [
                "2_affected_by_filter",
                Util.read_file_to_dict("inputs/disable_agent_multiple_agents_affected_by_filter.json.inp"),
                Util.read_file_to_dict("expected/affected_2.json.exp"),
            ],
        ]
    )
    def test_disable_agent(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "multiple_agents",
                Util.read_file_to_dict("inputs/enable_agent_multiple_agents_found.json.inp"),
                "Multiple agents found.",
                "Please provide a unique agent identifier so the action can be performed on the intended agent.",
            ],
            [
                "agent_not_found",
                Util.read_file_to_dict("inputs/enable_agent_not_found.json.inp"),
                "No agents found for: Hostname4.",
                "Please check provided information and try again.",
            ],
            [
                "invalid_expiration_date",
                Util.read_file_to_dict("inputs/disable_agent_invalid_expiration_date.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_disable_agent_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
