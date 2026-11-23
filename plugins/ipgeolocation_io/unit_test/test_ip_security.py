from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.ip_security import IpSecurity
from icon_ipgeolocation_io.actions.ip_security.schema import Input, Output
from unit_test.mock import DOMAIN, IP_BOGON, IP_CLEAN, IP_MALICIOUS, make_action, mock_request, sent_params

import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestIpSecurity(TestCase):
    def setUp(self):
        self.action = make_action(IpSecurity)

    def test_assesses_a_risky_ip(self, _):
        actual = self.action.run({Input.IP: IP_MALICIOUS})

        self.assertEqual(actual[Output.IP], IP_MALICIOUS)
        security = actual[Output.SECURITY]
        self.assertEqual(security["threat_score"], 80)
        self.assertIs(security["is_vpn"], True)
        self.assertIs(security["is_residential_proxy"], True)
        self.assertEqual(security["vpn_provider_names"], ["Nord VPN"])
        self.assertEqual(security["cloud_provider_name"], "Packethub S.A.")

    def test_zero_score_and_false_flags_are_preserved(self, _):
        security = self.action.run({Input.IP: IP_CLEAN})[Output.SECURITY]

        # These are the values that a naive falsy filter would silently delete.
        self.assertEqual(security["threat_score"], 0)
        self.assertEqual(security["proxy_confidence_score"], 0)
        self.assertIs(security["is_anonymous"], False)
        self.assertIs(security["is_known_attacker"], False)
        # Empty provider strings carry no information and are dropped.
        self.assertNotIn("relay_provider_name", security)

    def test_omits_ip_to_assess_the_orchestrator(self, mocked):
        self.action.run({})

        self.assertNotIn("ip", sent_params(mocked))

    def test_domain_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IP: DOMAIN})

        self.assertIn("does not accept domain names", context.exception.assistance)
        mocked.assert_not_called()

    def test_private_address_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IP: IP_BOGON})

        self.assertIn("private or bogon", context.exception.cause)
        mocked.assert_not_called()

    def test_field_filters_are_forwarded(self, mocked):
        self.action.run(
            {
                Input.IP: IP_MALICIOUS,
                Input.FIELDS: ["security.threat_score"],
                Input.EXCLUDES: ["security.is_tor"],
            }
        )

        params = sent_params(mocked)
        self.assertEqual(params["fields"], "security.threat_score")
        self.assertEqual(params["excludes"], "security.is_tor")
