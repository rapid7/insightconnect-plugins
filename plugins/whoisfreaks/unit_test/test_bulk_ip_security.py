import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.bulk_ip_security import BulkIpSecurity
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestBulkIpSecurity(ActionTestCase):
    action_class = BulkIpSecurity

    def test_bulk(self):
        output, session = self.run_action({"ip_addresses": ["8.8.8.8"]}, MockResponse(200, [{"ip": "8.8.8.8"}, "junk"]))
        self.assert_request(session, "POST", "/v1.0/security", None, {"ips": ["8.8.8.8"]})
        self.assertEqual([{"ip": "8.8.8.8"}], output["results"])

    def test_all_private(self):
        output, session = self.run_action({"ip_addresses": ["10.0.0.1", "192.168.0.1"]})
        self.assertEqual([], session.calls)
        self.assertEqual(2, len(output["skipped"]))
