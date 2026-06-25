import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.create_firewall_rule import CreateFirewallRule


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateFirewallRule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateFirewallRule())

    def test_create_firewall_rule(self, _mock_request):
        rule_data = {"name": "Block SSH", "state": "ENABLED", "action": "BLOCK_DROP"}
        mock_response = {"id": 201, "name": "Block SSH", "state": "ENABLED", "action": "BLOCK_DROP"}
        self.action.connection.zia_client.create_firewall_rule = MagicMock(return_value=mock_response)
        result = self.action.run({"rule_data": rule_data})
        self.assertEqual(result, {"rule": mock_response})
