import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.historical_whois import HistoricalWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestHistoricalWhois(ActionTestCase):
    action_class = HistoricalWhois

    def test_records(self):
        body = {"status": True, "total_records": "2", "whois_domains_historical": [{"num": 1}, {"num": 2}]}
        output, session = self.run_action({"domain": "example.com"}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v2.0/whois/history", {"domainName": "example.com"})
        self.assertEqual(2, output["total_records"])
        self.assertEqual([{"num": 1}, {"num": 2}], output["records"])
        self.assertTrue(output["found"])

    def test_not_found(self):
        output, _ = self.run_action(
            {"domain": "example.com"},
            MockResponse(404, {"status": 404, "error": "Not Found", "message": "Record not found."}),
        )
        self.assertFalse(output["found"])
        self.assertEqual([], output["records"])
