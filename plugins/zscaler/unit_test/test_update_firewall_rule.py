import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.update_firewall_rule import UpdateFirewallRule


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateFirewallRule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateFirewallRule())

    def test_update_firewall_rule(self, _mock_request):
        rule_data = {"name": "Block SSH Updated", "state": "DISABLED"}
        mock_response = {"id": 101, "name": "Block SSH Updated", "state": "DISABLED"}
        self.action.connection.zia_client.update_firewall_rule = MagicMock(return_value=mock_response)
        result = self.action.run({"rule_id": 101, "rule_data": rule_data})
        self.assertEqual(result, {"rule": mock_response})
