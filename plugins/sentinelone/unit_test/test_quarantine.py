import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.quarantine import Quarantine
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestQuarantine(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Quarantine())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/quarantine.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "unquarantine",
                Util.read_file_to_dict("inputs/unquarantine.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "already_quarantined",
                Util.read_file_to_dict("inputs/quarantine_already_quarantined.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
            [
                "agent_not_found",
                Util.read_file_to_dict("inputs/quarantine_not_found.json.inp"),
                Util.read_file_to_dict("expected/unaffected.json.exp"),
            ],
        ]
    )
    def test_quarantine(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "multiple_agents",
                Util.read_file_to_dict("inputs/quarantine_multiple_agents.json.inp"),
                "Multiple agents found.",
                "Please provide a unique identifier for the agent to be quarantined.",
            ],
            [
                "whitelisted",
                Util.read_file_to_dict("inputs/quarantine_whitelisted.json.inp"),
                "Agent found in the whitelist.",
                "If you would like to block this host, remove 0000000000000000001 from the whitelist and try again.",
            ],
        ]
    )
    def test_quarantine_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
