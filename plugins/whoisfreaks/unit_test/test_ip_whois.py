import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.ip_whois import IpWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestIpWhois(ActionTestCase):
    action_class = IpWhois

    def test_lookup(self):
        body = {"status": True, "ip_address": "8.8.8.8", "organization": {"name": "Google LLC"}}
        output, session = self.run_action({"ip_address": " 8.8.8.8 "}, MockResponse(206, body))
        self.assert_request(session, "GET", "/v1.0/ip-whois", {"ip": "8.8.8.8"})
        self.assertEqual("Google LLC", output["organization_name"])
        self.assertIn("Partial record", output["message"])

    def test_special_use_addresses(self):
        for address in (
            "10.0.0.1",
            "127.0.0.1",
            "169.254.1.1",
            "224.0.0.1",
            "::1",
            "fe80::1",
            "::ffff:192.168.0.1",
            "100.64.0.1",
        ):
            with self.subTest(address=address):
                output, session = self.run_action({"ip_address": address})
                self.assertEqual([], session.calls)
                self.assertFalse(output["found"])

    def test_invalid_address(self):
        with self.assertRaises(PluginException):
            self.run_action({"ip_address": "999.1.1.1"})

    def test_reserved_ip_error_from_api(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action({"ip_address": "8.8.8.8"}, MockResponse(423, {"message": "Bogon IP"}))
        self.assertEqual("reserved_ip", context.exception.kind)
