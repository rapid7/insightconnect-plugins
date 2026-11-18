import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.ip_security import IpSecurity
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestIpSecurity(ActionTestCase):
    action_class = IpSecurity

    def test_lookup(self):
        body = {
            "ip": "8.8.8.8",
            "security": {
                "threat_score": 5,
                "is_tor": False,
                "is_proxy": False,
                "is_vpn": True,
                "is_cloud_provider": True,
            },
        }
        output, session = self.run_action({"ip_address": "8.8.8.8"}, MockResponse(200, body))
        self.assert_request(session, "GET", "/v2.0/security", {"ip": "8.8.8.8"})
        self.assertEqual(5, output["threat_score"])
        self.assertTrue(output["is_vpn"])
        self.assertFalse(output["is_tor"])
        self.assertNotIn("is_bot", output)

    def test_private_ip(self):
        output, session = self.run_action({"ip_address": "172.16.0.5"})
        self.assertEqual([], session.calls)
        self.assertEqual("Private, reserved or special-use IP address", output["message"])

    def test_credits_exhausted(self):
        with self.assertRaises(WhoisFreaksError) as context:
            self.run_action(
                {"ip_address": "8.8.8.8"},
                MockResponse(413, {"message": "API credit limit exceeded. Please upgrade your plan."}),
            )
        self.assertEqual("no_credits", context.exception.kind)
        self.assertIn("Get Account Usage", context.exception.assistance)
