import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.ssl_lookup import SslLookup
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestSslLookup(ActionTestCase):
    action_class = SslLookup

    def test_certificate(self):
        body = {
            "domainName": "example.com",
            "sslCertificates": [
                {"chainOrder": "end-user", "validityStartDate": "2026-01-15", "validityEndDate": "2027-01-15"}
            ],
        }
        params = {"domain": "example.com", "include_chain": True, "include_raw": False}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session, "GET", "/v1.0/ssl/live", {"domainName": "example.com", "chain": "true", "sslRaw": "false"}
        )
        self.assertEqual("2026-01-15", output["valid_from"])
        self.assertEqual("2027-01-15", output["valid_to"])

    def test_no_certificate(self):
        output, _ = self.run_action(
            {"domain": "example.com"}, MockResponse(404, {"message": "No Ssl Certificate exists for this Domain."})
        )
        self.assertFalse(output["found"])
        self.assertIn("No Ssl Certificate", output["message"])
