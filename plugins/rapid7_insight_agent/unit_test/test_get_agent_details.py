import sys
import os
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unit_test.util import Util
from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
from icon_rapid7_insight_agent.actions.get_agent_details.schema import Input


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestGetAgentDetails(TestCase):
    @classmethod
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_request_for_api_key)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    def test_get_agent_by_hostname(self, mock_request):
        actual = self.action.run({Input.AGENT: "ivm-agent-ub18"})
        expect = Util.load_json("expected/get_agent_details.exp")
        self.assertEqual(expect, actual)

    def test_get_agent_by_hostname_with_none_in_response(self, mock_request):
        actual = self.action.run({Input.AGENT: "ivm-agent-win"})
        expect = Util.load_json("expected/get_agent_details_with_none.exp")
        self.assertEqual(expect, actual)

    def test_get_agent_by_ip(self, mock_request):
        actual = self.action.run({Input.AGENT: "11.44.23.53"})
        expect = Util.load_json("expected/get_agent_details.exp")
        self.assertEqual(expect, actual)

    def test_get_agent_by_ip_with_none_in_response(self, mock_request):
        actual = self.action.run({Input.AGENT: "12.43.13.43"})
        expect = Util.load_json("expected/get_agent_details_with_none.exp")
        self.assertEqual(expect, actual)

    def test_get_agent_by_mac(self, mock_request):
        actual = self.action.run({Input.AGENT: "01-51-53-44-A8-D1"})
        expect = Util.load_json("expected/get_agent_details.exp")
        self.assertEqual(expect, actual)

    def test_get_agent_by_hostname_bad(self, mock_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run({Input.AGENT: "badID"})
        self.assertEqual(exception.exception.cause, "Could not find agent matching badID of type Host Name.")
        self.assertEqual(
            exception.exception.assistance,
            "Check the agent input value and try again.",
        )
