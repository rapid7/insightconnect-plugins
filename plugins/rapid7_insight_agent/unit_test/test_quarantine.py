import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict

from jsonschema import validate
from util import Util

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
