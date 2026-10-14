import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict, List

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from util import (
    CONNECTION_LOGGER,
    POST_PAYLOAD,
    REINSTALLED_NEW,
    REINSTALLED_OLD,
    FakeAgentApi,
    Util,
    asset,
)

from icon_rapid7_insight_agent.actions.quarantine_multiple.action import QuarantineMultiple
from icon_rapid7_insight_agent.actions.quarantine_multiple.schema import Input


@patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
class TestQuarantineMultiple(TestCase):
    @parameterized.expand(Util.load_json("parameters/quarantine_multiple_success.json.resp").get("parameters"))
    def test_quarantine_multiple_success(
        self,
        mock_post: MagicMock,
        agent_id_array: List[str],
        interval: int,
        quarantine_state: str,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(QuarantineMultiple())
        actual = action.run(
            {Input.AGENT_ARRAY: agent_id_array, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_json("parameters/quarantine_multiple_failure.json.resp").get("parameters"))
    def test_quarantine_multiple_failure(
        self,
        mock_post: MagicMock,
        name: str,
        agent_id_array: List[str],
        interval: int,
        quarantine_state: str,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(QuarantineMultiple())
        actual = action.run(
            {Input.AGENT_ARRAY: agent_id_array, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)

    def test_empty_array(self, mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            action = Util.default_connector(QuarantineMultiple())
            action.run({Input.AGENT_ARRAY: [], Input.INTERVAL: 1000, Input.QUARANTINE_STATE: True})
        self.assertEqual(context.exception.cause, "Empty list provided.")


class TestQuarantineMultipleAgentChoice(TestCase):
    def test_every_host_is_processed(self) -> None:
        hosts = ["web01", "web02", "web03"]
        fake_api = FakeAgentApi(
            [[asset("1", ["WEB01"], "ONLINE"), asset("2", ["WEB02"], "ONLINE")], [asset("3", ["WEB03"], "ONLINE")]]
        )
        with patch(POST_PAYLOAD, side_effect=fake_api):
            action = Util.default_connector(QuarantineMultiple())
            actual = action.run({Input.AGENT_ARRAY: hosts, Input.INTERVAL: 300, Input.QUARANTINE_STATE: True})
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
            with self.assertLogs(CONNECTION_LOGGER, level="WARNING") as logs:
                actual = action.run(
                    {
                        Input.AGENT_ARRAY: ["laptop-01", "oldbox", "web01"],
                        Input.INTERVAL: 300,
                        Input.QUARANTINE_STATE: True,
                    }
                )
        # laptop-01: the online agent; web01: none online, so the one that checked in most recently
        self.assertEqual(["laptop-01", "web01"], actual["completed"])
        self.assertEqual(["new", "w-new"], fake_api.quarantined)
        self.assertEqual(
            [{"hostname": "oldbox", "error": "Agent ID s1 is stale and will not receive the request"}], actual["failed"]
        )
        self.assertIn("Using agent new because it is online", "\n".join(logs.output))
        self.assertIn(
            "Using agent w-new because none is online and it checked in most recently", "\n".join(logs.output)
        )
