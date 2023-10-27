import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.agents_reload import AgentsReload
from util import Util
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestAgentsReload(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsReload())

    @parameterized.expand(
        [
            [
                "monitor_module",
                Util.read_file_to_dict("inputs/agents_reload_monitor_module.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "static_module",
                Util.read_file_to_dict("inputs/agents_reload_static_module.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "agent_module",
                Util.read_file_to_dict("inputs/agents_reload_agent_module.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "log_module",
                Util.read_file_to_dict("inputs/agents_reload_log_module.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/agents_reload_invalid_id.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
        ]
    )
    def test_agents_reload(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
