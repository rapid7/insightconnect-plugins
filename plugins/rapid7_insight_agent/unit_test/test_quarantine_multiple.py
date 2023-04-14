import os
import sys
from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.actions.quarantine_multiple.action import QuarantineMultiple
from icon_rapid7_insight_agent.actions.quarantine_multiple.schema import Input
from unit_test.util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestQuarantineMultiple(TestCase):
    @parameterized.expand(Util.load_json("parameters/quarantine_multiple.json.resp").get("parameters"))
    @patch(
        "icon_rapid7_insight_agent.util.graphql_api.api_connection.ApiConnection._get_agent_id",
        return_value="goodIDMultiple",
    )
    def test_quarantine_multiple(self, agent_id_array, interval, quarantine_state, expected, mock_agent_id, mock_post):
        action = Util.default_connector(QuarantineMultiple())
        actual = action.run(
            {Input.AGENT_ARRAY: agent_id_array, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        self.assertEqual(actual, expected)
