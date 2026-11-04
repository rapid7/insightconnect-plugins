import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.asn_whois import AsnWhois
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestAsnWhois(ActionTestCase):
    action_class = AsnWhois

    def test_lookup(self):
        body = {"asNumber": "15169", "asName": "GOOGLE", "orgName": "Google LLC", "country": "US"}
        output, session = self.run_action({"asn": "as15169"}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v2.0/asn-whois", {"asn": "15169"})
        self.assertEqual(
            ("GOOGLE", "Google LLC", "US"), (output["as_name"], output["organization_name"], output["country"])
        )

    def test_invalid_asn(self):
        with self.assertRaises(PluginException):
            self.run_action({"asn": "ASX"})
