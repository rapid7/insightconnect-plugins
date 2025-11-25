import os
import sys
from typing import Any, Dict, List

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized
from util import Util

from icon_rapid7_insight_agent.actions.get_all_agents_by_ip import GetAllAgentsByIp
from icon_rapid7_insight_agent.actions.get_all_agents_by_ip.schema import Input, Output


class TestGetAllAgentsByIp(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetAllAgentsByIp())

    @parameterized.expand(Util.load_json("parameters/get_all_agents_by_ip.json.resp").get("parameters"))
    @patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
    def test_get_all_agents_by_ip(
        self, input_parameters: Dict[str, Any], expected: List[Dict[str, Any]], mock_request: MagicMock
    ) -> None:
        response = self.action.run({Input.IP_ADDRESS: input_parameters})
        validate(response, self.action.output.schema)
        self.assertEqual(response, {Output.AGENTS: expected})
        mock_request.assert_called()

    @patch("requests.sessions.Session.send", side_effect=Util.mocked_request)
    def test_get_all_agents_by_ip_exception(self, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IP_ADDRESS: "BadIP"})
        self.assertEqual(context.exception.cause, "Invalid input IP address: 'BadIP'")
        self.assertEqual(
            context.exception.assistance,
            "Please ensure that the input is a valid IPv4 or IPv6 address.",
        )
