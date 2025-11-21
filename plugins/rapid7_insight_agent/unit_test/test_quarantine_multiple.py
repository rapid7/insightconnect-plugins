import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict, List

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from util import Util

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
