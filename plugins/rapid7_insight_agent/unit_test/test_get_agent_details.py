import os
import sys
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from util import PAGES_CREDS, Util

from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
from icon_rapid7_insight_agent.actions.get_agent_details.schema import Input


@patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
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

    @parameterized.expand(
        [
            # The stale record comes first on the same page as the online one
            ("online_record_on_the_same_page", "samepage-01", "same-page-live"),
            # The online record is on the second page
            ("online_record_on_later_page", "LAPTOP-01", "new"),
            # None is online, so the first one found is kept even though a second one is on the second page
            ("first_found_when_none_is_online", "RECENT-01", "older"),
        ]
    )
    def test_get_agent_by_hostname_shared(
        self, mock_request: MagicMock, name: str, agent: str, expected_id: str
    ) -> None:
        action = Util.default_connector(GetAgentDetails(), api_key=PAGES_CREDS)
        with self.assertLogs("connection logger", level="INFO") as logs:
            actual = action.run({Input.AGENT: agent})
        validate(actual, action.output.schema)
        self.assertEqual(expected_id, actual.get("agent", {}).get("id"))

        # The log tells which of the agents sharing the hostname was used
        self.assertIn(f"using agent {expected_id}", "\n".join(logs.output))
