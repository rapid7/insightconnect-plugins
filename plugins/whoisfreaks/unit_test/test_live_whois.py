import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.live_whois import LiveWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestLiveWhois(ActionTestCase):
    action_class = LiveWhois

    def test_registered_domain(self):
        record = {
            "status": True,
            "domain_name": "example.com",
            "domain_registered": "yes",
            "create_date": "1995-08-14",
            "update_date": "2026-08-14",
            "expiry_date": "2027-08-13",
            "domain_registrar": {"registrar_name": "RESERVED-Internet Assigned Numbers Authority"},
            "name_servers": ["a.iana-servers.net", "b.iana-servers.net"],
            "domain_status": ["clientDeleteProhibited"],
        }
        output, session = self.run_action({"domain": " Example.COM. "}, MockResponse(200, record))
        self.assert_request(session, "GET", "/v2.0/whois/live", {"domainName": "example.com"})
        self.assertTrue(output["found"])
        self.assertTrue(output["registered"])
        self.assertEqual("RESERVED-Internet Assigned Numbers Authority", output["registrar_name"])
        self.assertEqual(["a.iana-servers.net", "b.iana-servers.net"], output["name_servers"])
        self.assertEqual(record, output["response"])

    def test_unregistered_and_cached(self):
        output, _ = self.run_action({"domain": "free-name.com"}, MockResponse(210, {"domain_registered": "no"}))
        self.assertFalse(output["registered"])
        self.assertEqual(210, output["status_code"])
        self.assertIn("Cached record", output["message"])

    def test_url_input_is_reduced_to_host(self):
        _, session = self.run_action({"domain": "https://www.Example.com/login?x=1"}, MockResponse(200, {"a": 1}))
        self.assertEqual({"domainName": "www.example.com"}, session.calls[-1]["params"])

    def test_not_found(self):
        output, _ = self.run_action(
            {"domain": "example.com"},
            MockResponse(404, {"status": 404, "error": "Not Found", "message": "Record not found."}),
        )
        self.assertEqual({"found": False, "status_code": 404, "message": "Record not found."}, output)

    def test_invalid_domain(self):
        with self.assertRaises(PluginException) as context:
            self.run_action({"domain": "not a domain"})
        self.assertIn("not valid", context.exception.cause)

    def test_unsupported_tld(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action({"domain": "example.zz"}, MockResponse(403, {"message": "WHOIS not offered for this TLD"}))
        self.assertEqual("forbidden", context.exception.kind)

    def test_thin_registry_fields_come_from_registry_data(self):
        # Shape of a live .com response: registrar and status codes are only present in registry_data
        record = {
            "status": True,
            "domain_name": "example.com",
            "domain_registered": "yes",
            "create_date": "1992-01-01",
            "name_servers": ["elliott.ns.cloudflare.com", "hera.ns.cloudflare.com"],
            "registry_data": {
                "create_date": "1995-08-14",
                "update_date": "2026-08-14",
                "expiry_date": "2027-08-13",
                "domain_registrar": {"registrar_name": "RESERVED-Internet Assigned Numbers Authority"},
                "name_servers": ["ignored.example"],
                "domain_status": ["clientupdateprohibited", "clientdeleteprohibited"],
            },
        }
        output, _ = self.run_action({"domain": "example.com"}, MockResponse(200, record))
        self.assertEqual("1992-01-01", output["create_date"])
        self.assertEqual("2026-08-14", output["update_date"])
        self.assertEqual("RESERVED-Internet Assigned Numbers Authority", output["registrar_name"])
        self.assertEqual(["clientupdateprohibited", "clientdeleteprohibited"], output["domain_status"])
        self.assertEqual(["elliott.ns.cloudflare.com", "hera.ns.cloudflare.com"], output["name_servers"])
