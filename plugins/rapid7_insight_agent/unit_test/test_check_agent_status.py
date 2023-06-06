import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.actions.check_agent_status.action import CheckAgentStatus
from icon_rapid7_insight_agent.actions.check_agent_status.schema import Input
from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestCheckAgentStatus(TestCase):
    def test_check_agent_status(self, mock_request):
        action = Util.default_connector(CheckAgentStatus())
        actual = action.run({Input.AGENT_ID: "goodID"})
        expect = Util.load_json("expected/check_agent_status.exp")
        self.assertEqual(expect, actual)

    def test_bad_agent_id(self, mock_request):
        with self.assertRaises(PluginException) as exception:
            action = Util.default_connector(CheckAgentStatus())
            action.run({Input.AGENT_ID: "badID"})
        self.assertEqual(exception.exception.cause, "Received an unexpected response from the server.")
        self.assertEqual(
            exception.exception.assistance,
            "Verify your plugin connection inputs are correct especially region. If the issue persists, please contact support.",
        )
