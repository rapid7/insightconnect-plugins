import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.reverse_whois import ReverseWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestReverseWhois(ActionTestCase):
    action_class = ReverseWhois

    def test_search(self):
        body = {
            "total_Result": 120,
            "total_Pages": 3,
            "current_Page": 2,
            "whois_domains_historical": [{"domain_name": "a.com"}],
        }
        params = {"email": "user@example.com", "mode": "mini", "exact": True, "page": 2}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session,
            "GET",
            "/v2.0/whois/reverse",
            {"email": "user@example.com", "mode": "mini", "exact": "true", "page": 2},
        )
        self.assertEqual((120, 3, 2), (output["total_records"], output["total_pages"], output["current_page"]))

    def test_capitalised_paging_keys(self):
        body = {"Total_Result": 5, "Total_Pages": 1, "Current_Page": 1, "whois_domains_historical": [{"x": 1}]}
        output, _ = self.run_action({"keyword": "example"}, MockResponse(200, body))
        self.assertEqual(5, output["total_records"])

    def test_requires_criteria(self):
        with self.assertRaises(PluginException) as context:
            self.run_action({"mode": "default", "exact": False, "page": 1, "keyword": "  "})
        self.assertIn("search value", context.exception.cause)

    def test_invalid_page(self):
        with self.assertRaises(PluginException):
            self.run_action({"keyword": "example", "page": 0})
