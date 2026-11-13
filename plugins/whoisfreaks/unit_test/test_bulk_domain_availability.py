import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.bulk_domain_availability import BulkDomainAvailability
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestBulkDomainAvailability(ActionTestCase):
    action_class = BulkDomainAvailability

    def test_domains(self):
        body = {
            "bulk_domain_availability_response": [
                {"domain": "example.com", "availability": "UNAVAILABLE", "status": True}
            ]
        }
        output, session = self.run_action({"domains": ["example.com"]}, MockResponse(206, body))
        self.assert_request(session, "POST", "/v2.0/domain/availability", None, {"domainNames": ["example.com"]})
        self.assertEqual(206, output["status_code"])
        self.assertEqual(1, len(output["results"]))

    def test_domain_with_tlds(self):
        params = {"domain": "example.com", "tlds": [".NET", "org", "bad tld"]}
        output, session = self.run_action(params, MockResponse(200, {"bulk_domain_availability_response": []}))
        self.assert_request(
            session, "POST", "/v2.0/domain/availability", {"domain": "example.com"}, {"tld": ["net", "org"]}
        )
        self.assertEqual([{"value": "bad tld", "reason": "Not a valid TLD"}], output["skipped"])

    def test_both_modes_rejected(self):
        with self.assertRaises(PluginException):
            self.run_action({"domains": ["a.com"], "domain": "b.com", "tlds": ["net"]})

    def test_nothing_to_check(self):
        with self.assertRaises(PluginException):
            self.run_action({"domain": "b.com"})

    def test_all_skipped(self):
        output, session = self.run_action({"domains": ["not valid"]})
        self.assertEqual([], session.calls)
        self.assertEqual([], output["results"])
