import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.agents_action import AgentsAction
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestAgentsAction(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AgentsAction())

    @parameterized.expand(
        [
            [
                "initiate-scan",
                Util.read_file_to_dict("inputs/agents_action_initiate_scan.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "abort-scan",
                Util.read_file_to_dict("inputs/agents_action_abort_scan.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "fetch-logs",
                Util.read_file_to_dict("inputs/agents_action_fetch_logs.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "connect",
                Util.read_file_to_dict("inputs/agents_action_connect.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "disconnect",
                Util.read_file_to_dict("inputs/agents_action_disconnect.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "restart-machine",
                Util.read_file_to_dict("inputs/agents_action_restart_machine.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "disconnect",
                Util.read_file_to_dict("inputs/agents_action_shutdown.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "uninstall",
                Util.read_file_to_dict("inputs/agents_action_uninstall.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "decommission",
                Util.read_file_to_dict("inputs/agents_action_decommission.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "not_found",
                Util.read_file_to_dict("inputs/agents_action_not_found.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
        ]
    )
    def test_agents_action(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_filter",
                Util.read_file_to_dict("inputs/agents_action_invalid_filter.json.inp"),
                "Wrong filter parameter.",
                "One of the following filter arguments must be supplied - ids, groupIds or filterId.",
            ]
        ]
    )
    def test_agents_action_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
