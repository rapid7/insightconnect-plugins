import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict, Optional

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from util import POST_PAYLOAD, FakeAgentApi, Util, asset

from icon_rapid7_insight_agent.actions.quarantine.action import Quarantine
from icon_rapid7_insight_agent.actions.quarantine.schema import Input


@patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
class TestQuarantine(TestCase):
    @parameterized.expand(Util.load_json("parameters/quarantine.json.resp").get("parameters"))
    def test_add_address_to_group(
        self,
        mock_post: MagicMock,
        name: str,
        agent_id: str,
        interval: int,
        quarantine_state: str,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(Quarantine())
        actual = action.run(
            {Input.AGENT_ID: agent_id, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)


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
            actual = action.run({Input.AGENT_ID: "a1", Input.INTERVAL: 300, Input.QUARANTINE_STATE: quarantine_state})
        self.assertEqual(expected, actual)
        self.assertEqual(["a1"], fake_api.quarantined)

    @parameterized.expand([("quarantine", True), ("unquarantine", False)])
    def test_stale_agent_raises(self, name: str, quarantine_state: bool) -> None:
        fake_api = FakeAgentApi([[asset("a1", ["WEB01"], "STALE")]])
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(Quarantine())
            with self.assertRaises(PluginException) as context:
                action.run({Input.AGENT_ID: "a1", Input.INTERVAL: 300, Input.QUARANTINE_STATE: quarantine_state})
        self.assertEqual("Agent a1 is stale.", context.exception.cause)
        self.assertEqual([], fake_api.quarantined)
