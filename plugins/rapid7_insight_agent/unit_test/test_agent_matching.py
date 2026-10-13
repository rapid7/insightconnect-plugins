import os
import sys
from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from util import Util

from icon_rapid7_insight_agent.actions.get_agent_details import GetAgentDetails
from icon_rapid7_insight_agent.actions.get_agent_details.schema import Input as GetAgentDetailsInput
from icon_rapid7_insight_agent.actions.quarantine.action import Quarantine
from icon_rapid7_insight_agent.actions.quarantine.schema import Input as QuarantineInput
from icon_rapid7_insight_agent.actions.quarantine_multiple.action import QuarantineMultiple
from icon_rapid7_insight_agent.actions.quarantine_multiple.schema import Input as QuarantineMultipleInput

POST_PAYLOAD = "icon_rapid7_insight_agent.util.graphql_api.api_connection.ApiConnection._post_payload"
TIMEOUT_MINUTES = "icon_rapid7_insight_agent.util.graphql_api.api_connection.TIMEOUT_MINUTES"


def asset(asset_id: str, names: List[str], status: str, last_check_in: Optional[str] = None) -> Dict[str, Any]:
    """Build an asset as returned by the API; last_check_in is an ISO date, or None to leave it out"""
    agent = {"agentStatus": status, "quarantineState": {"currentState": "NOT_QUARANTINED"}}
    if last_check_in:
        agent["timestamp"] = datetime.fromisoformat(last_check_in).replace(tzinfo=timezone.utc).timestamp() * 1000
    return {
        "id": asset_id,
        "platform": "windows",
        "host": {
            "hostNames": [{"name": name} for name in names],
            "primaryAddress": {"ip": "10.0.0.1", "mac": "AA-BB-CC-DD-EE-FF"},
            "uniqueIdentity": [],
            "attributes": [],
        },
        "agent": agent,
    }


class FakeAgentApi:
    """
    Serves pages of assets, ID lookups and quarantine requests. Requests are recognised by what they do rather
    than by their exact text, so these tests also run against earlier versions of the plugin.
    """

    def __init__(self, pages: List[List[dict]], assets_by_id: Optional[Dict[str, dict]] = None) -> None:
        self.pages = pages
        self.assets_by_id = assets_by_id or {asset_["id"]: asset_ for page in pages for asset_ in page}
        self.pages_read: List[int] = []
        self.quarantined: List[str] = []

    def __call__(self, payload: dict) -> dict:
        # Like the real API, every response is a fresh copy; the actions modify what they receive
        return deepcopy(self._respond(payload))

    def _respond(self, payload: dict) -> dict:
        query, variables = payload["query"], payload.get("variables", {})
        if query.startswith("{ organizations"):
            return {"data": {"organizations": {"edges": [{"node": {"id": "org-1", "name": "Example org"}}]}}}
        if "quarantineAssets" in query:  # also matches unquarantineAssets
            self.quarantined.append(variables["agentID"])
            mutation = "unquarantineAssets" if "unquarantineAssets" in query else "quarantineAssets"
            return {"data": {mutation: {"results": [{"assetId": variables["agentID"], "failed": False}]}}}
        if "ids: [$agentID]" in query:
            return {"data": {"assets": [self.assets_by_id.get(variables["agentID"])]}}
        page = int(variables.get("nextCursor") or 0)
        self.pages_read.append(page)
        return {
            "data": {
                "organization": {
                    "assets": {
                        "pageInfo": {"hasNextPage": page + 1 < len(self.pages), "endCursor": str(page + 1)},
                        "edges": [{"node": asset_} for asset_ in self.pages[page]],
                    }
                }
            }
        }


# A device whose agent was reinstalled: the old record stays behind with the same hostname
REINSTALLED_OLD = asset("old", ["LAPTOP-01"], "OFFLINE")
REINSTALLED_NEW = asset("new", ["LAPTOP-01"], "ONLINE")


class TestGetAgentDetailsMatching(TestCase):
    @parameterized.expand(
        [
            (
                "online_record_on_later_page_beats_offline_one",
                [[REINSTALLED_OLD], [REINSTALLED_NEW]],
                "laptop-01",
                "new",
                "2 agents share the hostname 'laptop-01'. Returned agent new because it is online.",
            ),
            (
                "online_record_found_before_the_last_page",
                [[REINSTALLED_OLD, REINSTALLED_NEW], [asset("other", ["LAPTOP-01"], "OFFLINE")]],
                "laptop-01",
                "new",
                "At least 2 agents share the hostname 'laptop-01'. Returned agent new because it is online.",
            ),
            (
                "most_recently_seen_when_none_is_online",
                [
                    [asset("older", ["LAPTOP-01"], "OFFLINE", "2026-03-10")],
                    [asset("newer", ["LAPTOP-01"], "OFFLINE", "2026-03-15")],
                ],
                "LAPTOP-01",
                "newer",
                "2 agents share the hostname 'LAPTOP-01'. Returned agent newer because none is online and it checked "
                "in most recently, at 2026-03-15T00:00:00+00:00.",
            ),
            (
                "first_found_without_check_in_times",
                [[asset("a", ["LAPTOP-01"], "OFFLINE")], [asset("b", ["LAPTOP-01"], "OFFLINE")]],
                "LAPTOP-01",
                "a",
                "2 agents share the hostname 'LAPTOP-01'. Returned agent a because none is online or has a check-in "
                "time, so it is the first one found.",
            ),
            ("single_stale_record_is_returned", [[asset("gone", ["WEB01"], "STALE")]], "web01", "gone", None),
        ]
    )
    def test_chosen_agent(
        self, name: str, pages: List[List[dict]], agent_input: str, expected_id: str, expected_message: Optional[str]
    ) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi(pages)):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({GetAgentDetailsInput.AGENT: agent_input})
        self.assertEqual(expected_id, actual.get("agent", {}).get("id"))
        self.assertEqual(expected_message, actual.get("message"))

    @patch(TIMEOUT_MINUTES, -1)
    def test_time_limit_returns_first_match_with_message(self) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi([[REINSTALLED_OLD], [REINSTALLED_NEW]])):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({GetAgentDetailsInput.AGENT: "laptop-01"})
        self.assertEqual("old", actual["agent"]["id"])
        self.assertNotIn("next_cursor", actual)
        self.assertTrue(actual["message"].startswith("Stopped searching for 'laptop-01' at the"))
        self.assertIn("Returned the first agent found with this hostname", actual["message"])

    @patch(TIMEOUT_MINUTES, -1)
    def test_time_limit_without_match_returns_next_cursor_with_message(self) -> None:
        with patch(POST_PAYLOAD, side_effect=FakeAgentApi([[asset("w1", ["WEB01"], "ONLINE")], [REINSTALLED_NEW]])):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({GetAgentDetailsInput.AGENT: "laptop-01"})
        self.assertNotIn("agent", actual)
        self.assertEqual("1", actual["next_cursor"])
        self.assertIn("Run the action again with the next cursor", actual["message"])

    def test_stops_reading_pages_at_online_match(self) -> None:
        fake_api = FakeAgentApi([[REINSTALLED_NEW], [REINSTALLED_OLD]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({GetAgentDetailsInput.AGENT: "LAPTOP-01"})
        self.assertEqual("new", actual["agent"]["id"])
        self.assertEqual([0], fake_api.pages_read)

    def test_agent_id_is_looked_up_directly(self) -> None:
        agent_id = "0123456789abcdef0123456789abcdef"
        fake_api = FakeAgentApi([[asset(agent_id, ["LAPTOP-01"], "ONLINE")]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(GetAgentDetails())
            actual = action.run({GetAgentDetailsInput.AGENT: agent_id})
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
            actual = action.run({GetAgentDetailsInput.AGENT: agent_input})
        self.assertEqual({"agent": {}}, actual)
        self.assertEqual([0], fake_api.pages_read)


class TestQuarantineAgentState(TestCase):
    @parameterized.expand(
        [
            ("online", "ONLINE", True, {"success": True, "is_asset_online": True}),
            ("offline", "OFFLINE", True, {"success": True, "is_asset_online": False}),
            ("offline_unquarantine", "OFFLINE", False, {"success": True, "is_asset_online": False}),
            # Unchanged behaviour: an ID the lookup does not know is still sent to the platform
            ("unknown_agent_is_still_sent", None, True, {"success": True, "is_asset_online": False}),
        ]
    )
    def test_quarantine(
        self, name: str, status: Optional[str], quarantine_state: bool, expected: Dict[str, Any]
    ) -> None:
        fake_api = FakeAgentApi([[asset("a1", ["WEB01"], status)]] if status else [[]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(Quarantine())
            actual = action.run(
                {
                    QuarantineInput.AGENT_ID: "a1",
                    QuarantineInput.INTERVAL: 300,
                    QuarantineInput.QUARANTINE_STATE: quarantine_state,
                }
            )
        self.assertEqual(expected, actual)
        self.assertEqual(["a1"], fake_api.quarantined)

    @parameterized.expand([("quarantine", True), ("unquarantine", False)])
    def test_stale_agent_raises(self, name: str, quarantine_state: bool) -> None:
        fake_api = FakeAgentApi([[asset("a1", ["WEB01"], "STALE")]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(Quarantine())
            with self.assertRaises(PluginException) as context:
                action.run(
                    {
                        QuarantineInput.AGENT_ID: "a1",
                        QuarantineInput.INTERVAL: 300,
                        QuarantineInput.QUARANTINE_STATE: quarantine_state,
                    }
                )
        self.assertEqual("Agent a1 is stale.", context.exception.cause)
        self.assertEqual([], fake_api.quarantined)


class TestQuarantineMultipleMatching(TestCase):
    def test_every_host_is_processed(self) -> None:
        hosts = ["web01", "web02", "web03"]
        fake_api = FakeAgentApi(
            [[asset("1", ["WEB01"], "ONLINE"), asset("2", ["WEB02"], "ONLINE")], [asset("3", ["WEB03"], "ONLINE")]]
        )
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(QuarantineMultiple())
            actual = action.run(
                {
                    QuarantineMultipleInput.AGENT_ARRAY: hosts,
                    QuarantineMultipleInput.INTERVAL: 300,
                    QuarantineMultipleInput.QUARANTINE_STATE: True,
                }
            )
        self.assertEqual({"completed": ["web01", "web02", "web03"], "failed": []}, actual)
        self.assertEqual(["web01", "web02", "web03"], hosts)

    def test_agents_are_chosen_like_get_agent_details(self) -> None:
        fake_api = FakeAgentApi(
            [
                [REINSTALLED_OLD, asset("s1", ["OLDBOX"], "STALE"), asset("w-old", ["WEB01"], "OFFLINE", "2026-03-10")],
                [REINSTALLED_NEW, asset("w-new", ["WEB01"], "OFFLINE", "2026-03-15")],
            ]
        )
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(QuarantineMultiple())
            actual = action.run(
                {
                    QuarantineMultipleInput.AGENT_ARRAY: ["laptop-01", "oldbox", "web01"],
                    QuarantineMultipleInput.INTERVAL: 300,
                    QuarantineMultipleInput.QUARANTINE_STATE: True,
                }
            )
        # laptop-01: the online agent; web01: none online, so the one that checked in most recently
        self.assertEqual(["laptop-01", "web01"], actual["completed"])
        self.assertEqual(["new", "w-new"], fake_api.quarantined)
        self.assertEqual(
            [{"hostname": "oldbox", "error": "Agent ID s1 is stale and will not receive the request"}], actual["failed"]
        )
