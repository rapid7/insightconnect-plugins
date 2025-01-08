import os
import sys
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from util import Util

from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
from icon_rapid7_insight_agent.actions.get_agent_details.schema import Input


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestGetAgentDetails(TestCase):
    @parameterized.expand(Util.load_json("parameters/get_agents_details.json.resp").get("parameters"))
    def test_get_agent_details(self, mock_request: MagicMock, name: str, agent: str, expect: Dict[str, Any]) -> None:
        action = Util.default_connector(GetAgentDetails())
        actual = action.run({Input.AGENT: agent})
        validate(actual, action.output.schema)
        self.assertEqual(expect, actual)

    def test_get_agent_by_hostname_bad(self, mock_request: MagicMock) -> None:
        action = Util.default_connector(GetAgentDetails())
        actual = action.run({Input.AGENT: "badID"})
        expected = {"agent": {}}
        self.assertEqual(actual, expected)
