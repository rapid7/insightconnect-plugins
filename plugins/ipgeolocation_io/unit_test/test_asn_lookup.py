from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.asn_lookup import AsnLookup
from icon_ipgeolocation_io.actions.asn_lookup.schema import Input, Output
from unit_test.mock import IP_HETZNER, make_action, mock_request, sent_params
import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestAsnLookup(TestCase):
    def setUp(self):
        self.action = make_action(AsnLookup)

    def test_lookup_by_asn(self, mocked):
        actual = self.action.run({Input.ASN: "24940"})

        self.assertEqual(sent_params(mocked)["asn"], "24940")
        self.assertEqual(actual[Output.ASN]["organization"], "Hetzner Online GmbH")
        self.assertEqual(actual[Output.ASN]["allocation_status"], "ASSIGNED")
        # The ip key is absent when the lookup was made by ASN.
        self.assertNotIn(Output.IP, actual)

    def test_as_prefix_is_stripped(self, mocked):
        self.action.run({Input.ASN: "AS24940"})

        self.assertEqual(sent_params(mocked)["asn"], "24940")

    def test_lookup_by_ip_returns_the_queried_ip(self, mocked):
        actual = self.action.run({Input.IP: IP_HETZNER})

        self.assertEqual(sent_params(mocked)["ip"], IP_HETZNER)
        self.assertEqual(actual[Output.IP], IP_HETZNER)
        self.assertEqual(actual[Output.ASN]["as_number"], "AS24940")

    def test_ip_wins_when_both_are_supplied(self, mocked):
        self.action.run({Input.IP: IP_HETZNER, Input.ASN: "AS1257"})

        params = sent_params(mocked)
        self.assertEqual(params["ip"], IP_HETZNER)
        self.assertNotIn("asn", params)

    def test_neither_input_falls_back_to_the_orchestrator_ip(self, mocked):
        self.action.run({})

        params = sent_params(mocked)
        self.assertNotIn("ip", params)
        self.assertNotIn("asn", params)

    def test_include_adds_routing_intelligence(self, mocked):
        actual = self.action.run({Input.ASN: "24940", Input.INCLUDE: ["peers", "routes", "whois_response"]})

        self.assertEqual(sent_params(mocked)["include"], "peers,routes,whois_response")
        asn = actual[Output.ASN]
        self.assertEqual(asn["peers"][0]["as_number"], "AS3356")
        self.assertEqual(asn["routes"], ["49.12.0.0/16", "2a01:4f8::/29"])
        self.assertIn("HETZNER-AS", asn["whois_response"])

    def test_invalid_asn_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.ASN: "HETZNER"})

        self.assertIn("not a valid Autonomous System Number", context.exception.cause)
        mocked.assert_not_called()

    def test_invalid_ip_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IP: "not-an-ip"})
        mocked.assert_not_called()
