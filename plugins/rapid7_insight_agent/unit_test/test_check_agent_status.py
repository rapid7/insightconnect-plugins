import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

sys.path.append(os.path.abspath("../"))
from util import Util

from icon_rapid7_insight_agent.actions.check_agent_status.action import CheckAgentStatus
from icon_rapid7_insight_agent.actions.check_agent_status.schema import Input


@patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
class TestCheckAgentStatus(TestCase):
    def test_check_agent_status(self, mock_request: MagicMock) -> None:
        action = Util.default_connector(CheckAgentStatus())
        actual = action.run({Input.AGENT_ID: "goodID"})
        expect = Util.load_json("expected/check_agent_status.exp")
        validate(actual, action.output.schema)
        self.assertEqual(expect, actual)

    def test_bad_agent_id(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as exception:
            action = Util.default_connector(CheckAgentStatus())
            action.run({Input.AGENT_ID: "badID"})
        self.assertEqual(exception.exception.cause, "Received an unexpected response from the server.")
        self.assertEqual(
            exception.exception.assistance,
            "Verify your plugin connection inputs are correct especially region. If the issue persists, please contact support.",
        )
