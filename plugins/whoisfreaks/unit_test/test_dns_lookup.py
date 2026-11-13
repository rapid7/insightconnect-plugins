import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.dns_lookup import DnsLookup
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestDnsLookup(ActionTestCase):
    action_class = DnsLookup

    def test_domain_lookup(self):
        body = {"domainName": "example.com", "dnsRecords": [{"dnsType": "A", "address": "93.184.215.14"}, "junk"]}
        params = {"domain": "example.com", "record_types": "a, mx,A", "cname_depth": 2, "relative_records": False}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session,
            "GET",
            "/v2.0/dns/live",
            {"type": "A,MX", "cnameDepth": 2, "relativeRecords": "false", "domainName": "example.com"},
        )
        self.assertEqual([{"dnsType": "A", "address": "93.184.215.14"}], output["records"])

    def test_ptr_lookup(self):
        _, session = self.run_action({"ip_address": "8.8.8.8", "record_types": "PTR"}, MockResponse(200, {"a": 1}))
        self.assertEqual({"type": "PTR", "ipAddress": "8.8.8.8"}, session.calls[-1]["params"])

    def test_private_ip_is_not_sent(self):
        output, session = self.run_action({"ip_address": "192.168.1.10", "record_types": "all"})
        self.assertEqual([], session.calls)
        self.assertFalse(output["found"])

    def test_requires_domain_or_ip(self):
        with self.assertRaises(PluginException):
            self.run_action({"record_types": "all"})

    def test_invalid_record_type(self):
        with self.assertRaises(PluginException) as context:
            self.run_action({"domain": "example.com", "record_types": "A,BOGUS"})
        self.assertIn("BOGUS", context.exception.cause)

    def test_invalid_cname_depth(self):
        with self.assertRaises(PluginException):
            self.run_action({"domain": "example.com", "cname_depth": 9})

    def test_not_found(self):
        output, _ = self.run_action(
            {"domain": "example.com"},
            MockResponse(404, {"status": 404, "error": "Not Found", "message": "Record not found."}),
        )
        self.assertFalse(output["found"])
