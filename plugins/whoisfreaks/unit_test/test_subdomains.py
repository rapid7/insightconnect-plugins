import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.subdomains import Subdomains
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestSubdomains(ActionTestCase):
    action_class = Subdomains

    def test_subdomains(self):
        body = {
            "domain": "example.com",
            "current_page": 1,
            "total_pages": 1,
            "total_records": 1,
            "subdomains": [{"subdomain": "www.example.com"}],
        }
        params = {"domain": "example.com", "after": "2026-01-01", "before": "2026-12-31", "status": "active", "page": 1}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session,
            "GET",
            "/v1.0/subdomains",
            {"domain": "example.com", "after": "2026-01-01", "before": "2026-12-31", "status": "active", "page": 1},
        )
        self.assertEqual([{"subdomain": "www.example.com"}], output["records"])

    def test_bad_dates(self):
        for params in (
            {"domain": "a.com", "after": "01/01/2026"},
            {"domain": "a.com", "after": "2026-02-01", "before": "2026-01-01"},
        ):
            with self.subTest(params=params), self.assertRaises(PluginException):
                self.run_action(params)

    def test_found_but_empty(self):
        output, _ = self.run_action({"domain": "example.com"}, MockResponse(200, {"subdomains": []}))
        self.assertFalse(output["found"])
        self.assertEqual("No records found", output["message"])
