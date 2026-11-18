import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.ip_geolocation import IpGeolocation
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestIpGeolocation(ActionTestCase):
    action_class = IpGeolocation

    def test_lookup(self):
        body = {
            "ip": "8.8.8.8",
            "location": {"country_code2": "US", "country_name": "United States", "city": "Mountain View"},
        }
        output, session = self.run_action({"ip_address": "8.8.8.8"}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v1.0/geolocation", {"ip": "8.8.8.8"})
        self.assertEqual("US", output["country_code"])
        self.assertEqual("Mountain View", output["city"])

    def test_ipv6(self):
        _, session = self.run_action({"ip_address": "2001:4860:4860:0:0:0:0:8888"}, MockResponse(200, {"ip": "x"}))
        self.assertEqual({"ip": "2001:4860:4860::8888"}, session.calls[-1]["params"])
