import os
import sys
from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.actions.quarantine_multiple.action import QuarantineMultiple
from icon_rapid7_insight_agent.actions.quarantine_multiple.schema import Input
from unit_test.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.post", side_effect=Util.mocked_request)
class TestQuarantineMultiple(TestCase):
    @parameterized.expand(Util.load_json("parameters/quarantine_multiple_success.json.resp").get("parameters"))
    def test_quarantine_multiple_success(self, mock_post, agent_id_array, interval, quarantine_state, expected):

        action = Util.default_connector(QuarantineMultiple())
        actual = action.run(
            {Input.AGENT_ARRAY: agent_id_array, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_json("parameters/quarantine_multiple_failure.json.resp").get("parameters"))
    def test_quarantine_multiple_failure(self, mock_post, agent_id_array, interval, quarantine_state, expected):

        action = Util.default_connector(QuarantineMultiple())
        actual = action.run(
            {Input.AGENT_ARRAY: agent_id_array, Input.INTERVAL: interval, Input.QUARANTINE_STATE: quarantine_state}
        )
        self.assertEqual(actual, expected)

    def test_empty_array(self, mock_post):
        action = Util.default_connector(QuarantineMultiple())
        with self.assertRaises(PluginException) as context:
            action.run({Input.AGENT_ARRAY: [], Input.INTERVAL: 1000, Input.QUARANTINE_STATE: True})
        self.assertEqual(context.exception.cause, "Empty list provided.")
