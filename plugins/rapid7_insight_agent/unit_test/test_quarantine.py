import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.actions.quarantine.action import Quarantine
from icon_rapid7_insight_agent.actions.quarantine.schema import Input
from unit_test.util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestCheckAgentStatus(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_request_for_api_key)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(Quarantine())

    def test_check_agent_status(self, mock_request):
        actual = self.action.run(
            {Input.AGENT_ID: "goodIDQuarantine", Input.INTERVAL: 604800, Input.QUARANTINE_STATE: True}
        )
        expect = Util.load_json("expected/quarantine.exp")
        self.assertEqual(expect, actual)

    def test_bad_agent_id(self, mock_request):
        actual = self.action.run(
            {Input.AGENT_ID: "badIDQuarantine", Input.INTERVAL: 604800, Input.QUARANTINE_STATE: True}
        )
        expect = Util.load_json("expected/quarantine_bad.exp")
        self.assertEqual(expect, actual)
