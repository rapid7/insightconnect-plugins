import os
import sys
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List, Optional
from unittest import TestCase

from util import (
    CONNECTION_LOGGER,
    POST_PAYLOAD,
    REINSTALLED_NEW,
    REINSTALLED_OLD,
    TIMEOUT_MINUTES,
    FakeAgentApi,
    Util,
    asset,
)

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


class TestGetAgentDetailsHostnameMatching(TestCase):
    @parameterized.expand(
        [
            (
                "online_record_on_later_page_beats_offline_one",
                [[REINSTALLED_OLD], [REINSTALLED_NEW]],
                "laptop-01",
                "new",
                "2 agents share the hostname 'laptop-01'. Using agent new because it is online.",
            ),
            (
                "online_record_found_before_the_last_page",
                [[REINSTALLED_OLD, REINSTALLED_NEW], [asset("other", ["LAPTOP-01"], "OFFLINE")]],
                "laptop-01",
                "new",
                "At least 2 agents share the hostname 'laptop-01'. Using agent new because it is online.",
            ),
            (
                "most_recently_seen_when_none_is_online",
                [
                    [asset("older", ["LAPTOP-01"], "OFFLINE", "2026-03-10")],
                    [asset("newer", ["LAPTOP-01"], "OFFLINE", "2026-03-15")],
                ],
                "LAPTOP-01",
                "newer",
                "2 agents share the hostname 'LAPTOP-01'. Using agent newer because none is online and it checked "
                "in most recently, at 2026-03-15T00:00:00+00:00.",
            ),
            (
                "first_found_without_check_in_times",
                [[asset("a", ["LAPTOP-01"], "OFFLINE")], [asset("b", ["LAPTOP-01"], "OFFLINE")]],
                "LAPTOP-01",
                "a",
                "2 agents share the hostname 'LAPTOP-01'. Using agent a because none is online or has a check-in "
                "time, so it is the first one found.",
            ),
            ("single_stale_record_is_returned", [[asset("gone", ["WEB01"], "STALE")]], "web01", "gone", None),
        ]
    )
    def test_chosen_agent(
        self, name: str, pages: List[List[dict]], agent_input: str, expected_id: str, expected_log: Optional[str]
    ) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi(pages)):
            action = Util.default_connector(GetAgentDetails())
            if expected_log:
                with self.assertLogs(CONNECTION_LOGGER, level="WARNING") as logs:
                    actual = action.run({Input.AGENT: agent_input})
                self.assertIn(expected_log, "\n".join(logs.output))
            else:
                with self.assertNoLogs(CONNECTION_LOGGER, level="WARNING"):
                    actual = action.run({Input.AGENT: agent_input})
        self.assertEqual(expected_id, actual["agent"]["id"])

    @patch(TIMEOUT_MINUTES, -1)
    def test_time_limit_returns_first_match(self) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi([[REINSTALLED_OLD], [REINSTALLED_NEW]])):
            action = Util.default_connector(GetAgentDetails())
            with self.assertLogs(CONNECTION_LOGGER, level="WARNING") as logs:
                actual = action.run({Input.AGENT: "laptop-01"})
        self.assertEqual("old", actual["agent"]["id"])
        self.assertNotIn("next_cursor", actual)
        log_output = "\n".join(logs.output)
        self.assertIn("Stopped searching for 'laptop-01'", log_output)
        self.assertIn("Returning the first agent found with this hostname", log_output)

    @patch(TIMEOUT_MINUTES, -1)
    def test_time_limit_without_match_returns_next_cursor(self) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi([[asset("w1", ["WEB01"], "ONLINE")], [REINSTALLED_NEW]])):
            action = Util.default_connector(GetAgentDetails())
            with self.assertLogs(CONNECTION_LOGGER, level="INFO") as logs:
                actual = action.run({Input.AGENT: "laptop-01"})
        self.assertNotIn("agent", actual)
        self.assertEqual("1", actual["next_cursor"])
        self.assertIn("Run the action again with the next cursor", "\n".join(logs.output))

    def test_stops_reading_pages_at_online_match(self) -> None:
        fake_api = FakeAgentApi([[REINSTALLED_NEW], [REINSTALLED_OLD]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({Input.AGENT: "LAPTOP-01"})
        self.assertEqual("new", actual["agent"]["id"])
        self.assertEqual([0], fake_api.pages_read)

    def test_agent_id_is_looked_up_directly(self) -> None:
        agent_id = "0123456789abcdef0123456789abcdef"
        fake_api = FakeAgentApi([[asset(agent_id, ["LAPTOP-01"], "ONLINE")]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({Input.AGENT: agent_id})
        self.assertEqual(agent_id, actual["agent"]["id"])
        self.assertEqual([], fake_api.pages_read)

    @parameterized.expand(
        [
            ("unknown_agent_id_falls_back_to_hostname_search", "ffffffffffffffffffffffffffffffff"),
            # Names must match exactly; there is deliberately no short-name fallback
            ("fqdn_does_not_match_short_name_record", "web01.example.com"),
        ]
    )
    def test_no_match(self, name: str, agent_input: str) -> None:
        fake_api = FakeAgentApi([[asset("w1", ["WEB01"], "ONLINE")]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({Input.AGENT: agent_input})
        self.assertEqual({"agent": {}}, actual)
        self.assertEqual([0], fake_api.pages_read)
