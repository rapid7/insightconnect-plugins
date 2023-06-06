import sys
import os
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from util import Util
from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
from icon_rapid7_insight_agent.actions.get_agent_details.schema import Input


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestGetAgentDetails(TestCase):
    @parameterized.expand(Util.load_json("parameters/get_agents_details.json.resp").get("parameters"))
    def test_get_agent_details(self, mock_request, name, agent, expect):
        action = Util.default_connector(GetAgentDetails())
        actual = action.run({Input.AGENT: agent})
        self.assertEqual(expect, actual)

    def test_get_agent_by_hostname_bad(self, mock_request):
        with self.assertRaises(PluginException) as exception:
            action = Util.default_connector(GetAgentDetails())
            action.run({Input.AGENT: "badID"})
        self.assertEqual(exception.exception.cause, "Could not find agent matching badID of type Host Name.")
        self.assertEqual(
            exception.exception.assistance,
            "Check the agent input value and try again.",
        )
