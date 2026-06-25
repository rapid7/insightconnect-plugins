import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.list_firewall_rules import ListFirewallRules


@patch("requests.request", side_effect=Util.mock_request)
class TestListFirewallRules(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListFirewallRules())

    def test_list_firewall_rules(self, _mock_request):
        mock_response = {
            "rules": [{"id": 101, "name": "Block SSH"}],
            "next_link": "",
        }
        self.action.connection.zia_client.list_firewall_rules = MagicMock(return_value=mock_response)
        result = self.action.run({})
        self.assertEqual(result["rules"], [{"id": 101, "name": "Block SSH"}])
