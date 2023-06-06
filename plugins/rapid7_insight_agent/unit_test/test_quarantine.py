import os
import sys
from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.actions.quarantine.action import Quarantine
from icon_rapid7_insight_agent.actions.quarantine.schema import Input
from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestQuarantine(TestCase):
    @parameterized.expand(Util.load_json("parameters/quarantine.json.resp").get("parameters"))
    def test_add_address_to_group(self, mock_post, name, agent_id, interval, quarantine_state, expected):
        action = Util.default_connector(Quarantine())
        actual = action.run(
            {Input.AGENT_ID: agent_id, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        self.assertEqual(actual, expected)
