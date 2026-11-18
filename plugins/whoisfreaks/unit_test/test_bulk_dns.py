import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.bulk_dns import BulkDns
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestBulkDns(ActionTestCase):
    action_class = BulkDns

    def test_domains_and_ips(self):
        body = {"bulk_dns_info": [{"domainName": "example.com"}, {"ipAddress": "8.8.8.8"}]}
        params = {
            "domains": ["example.com"],
            "ip_addresses": ["8.8.8.8", "10.0.0.1"],
            "record_types": "A",
            "cname_depth": 1,
        }
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session,
            "POST",
            "/v2.0/dns/bulk/live",
            {"type": "A", "cname_depth": 1},
            {"domainNames": ["example.com"], "ipAddresses": ["8.8.8.8"]},
        )
        self.assertEqual(2, len(output["results"]))
        self.assertEqual(
            [{"value": "10.0.0.1", "reason": "Private, reserved or special-use IP address"}], output["skipped"]
        )

    def test_only_skipped_values(self):
        output, session = self.run_action({"ip_addresses": ["127.0.0.1"]})
        self.assertEqual([], session.calls)
        self.assertEqual(1, len(output["skipped"]))

    def test_requires_values(self):
        with self.assertRaises(PluginException):
            self.run_action({"record_types": "all"})
