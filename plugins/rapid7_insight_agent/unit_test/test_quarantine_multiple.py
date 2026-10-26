import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict, List

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from util import PAGES_CREDS, Util

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

    @parameterized.expand(
        [
            # Quarantine
            ("quarantine", True),
            # Unquarantine uses the agent from the listing, so it must work without another lookup
            ("unquarantine", False),
        ]
    )
    def test_quarantine_multiple_shared_hostnames(
        self, mock_post: MagicMock, name: str, quarantine_state: bool
    ) -> None:
        action = Util.default_connector(QuarantineMultiple(), api_key=PAGES_CREDS)
        hostnames = ["web01", "laptop-01", "web03"]
        actual = action.run(
            {Input.AGENT_ARRAY: hostnames, Input.INTERVAL: 300, Input.QUARANTINE_STATE: quarantine_state}
        )

        # WEB03 is on the second page and used to crash, and hosts after a match used to be skipped
        self.assertEqual({"completed": hostnames, "failed": []}, actual)

        # LAPTOP-01 has an offline record on the first page, the online one on the second must be used
        sent = [call.args[0].body.decode() for call in mock_post.call_args_list]
        self.assertTrue(any('"agentID": "new"' in body for body in sent))
