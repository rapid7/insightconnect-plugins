import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_firewall_rule import GetFirewallRule


@patch("requests.request", side_effect=Util.mock_request)
class TestGetFirewallRule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFirewallRule())

    def test_get_firewall_rule(self, _mock_request):
        mock_rule = {"id": 101, "name": "Block SSH", "state": "ENABLED"}
        self.action.connection.zia_client.get_firewall_rule = MagicMock(return_value=mock_rule)
        result = self.action.run({"rule_id": 101})
        self.assertEqual(result, {"rule": mock_rule})
