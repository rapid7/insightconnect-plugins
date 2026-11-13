import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.bulk_whois import BulkWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestBulkWhois(ActionTestCase):
    action_class = BulkWhois

    def test_bulk(self):
        body = {"bulk_whois_response": [{"domain_name": "example.com"}, {"domain_name": "example.org"}]}
        params = {"domains": ["example.com", "EXAMPLE.com", "bad value", "example.org"]}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session, "POST", "/v2.0/bulkwhois/live", None, {"domainNames": ["example.com", "example.org"]}
        )
        self.assertEqual(2, len(output["results"]))
        self.assertEqual(["EXAMPLE.com", "bad value"], [item["value"] for item in output["skipped"]])

    def test_all_skipped_makes_no_request(self):
        output, session = self.run_action({"domains": ["bad value"]})
        self.assertEqual([], session.calls)
        self.assertEqual([], output["results"])

    def test_too_many_domains(self):
        with self.assertRaises(PluginException) as context:
            self.run_action({"domains": [f"d{index}.com" for index in range(101)]})
        self.assertIn("more than the WhoisFreaks limit", context.exception.cause)

    def test_empty_list(self):
        with self.assertRaises(PluginException):
            self.run_action({"domains": []})

    def test_bulk_post_is_not_retried_after_server_error(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action({"domains": ["example.com"]}, MockResponse(500, {"message": "boom"}), MockResponse(200, {}))
        self.assertEqual("server_error", context.exception.kind)

    def test_bulk_post_is_retried_after_rate_limit(self):
        body = {"bulk_whois_response": [{"domain_name": "example.com"}]}
        output, session = self.run_action(
            {"domains": ["example.com"]},
            MockResponse(429, {"message": "Please slow down."}, {"X-RateLimit-Remaining-Time": "2000000000"}),
            MockResponse(200, body),
        )
        self.assertEqual(2, len(session.calls))
        self.assertEqual(1, len(output["results"]))
