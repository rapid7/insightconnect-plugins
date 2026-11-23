from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.ip_geolocation import IpGeolocation
from icon_ipgeolocation_io.actions.ip_geolocation.schema import Input, Output
from unit_test.mock import DOMAIN, IP_BOGON, IP_SWEDEN, make_action, mock_request, sent_params
import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestIpGeolocation(TestCase):
    def setUp(self):
        self.action = make_action(IpGeolocation)

    def test_enriches_an_ip(self, _):
        actual = self.action.run({Input.IP: IP_SWEDEN})

        result = actual[Output.RESULT]
        self.assertEqual(result["ip"], IP_SWEDEN)
        self.assertEqual(result["location"]["city"], "Stockholm")
        self.assertEqual(result["asn"]["as_number"], "AS1257")
        self.assertEqual(result["currency"]["code"], "SEK")
        self.assertEqual(result["country_metadata"]["calling_code"], "+46")
        self.assertEqual(result["time_zone"]["name"], "Europe/Stockholm")

    def test_omits_ip_to_geolocate_the_orchestrator(self, mocked):
        self.action.run({})

        self.assertNotIn("ip", sent_params(mocked))

    def test_list_inputs_are_sent_as_comma_separated_values(self, mocked):
        self.action.run(
            {
                Input.IP: IP_SWEDEN,
                Input.INCLUDE: ["security", "abuse", "security"],
                Input.FIELDS: ["location.city", "security.threat_score"],
                Input.EXCLUDES: ["currency"],
            }
        )

        params = sent_params(mocked)
        self.assertEqual(params["include"], "security,abuse")
        self.assertEqual(params["fields"], "location.city,security.threat_score")
        self.assertEqual(params["excludes"], "currency")

    def test_default_language_is_not_sent(self, mocked):
        self.action.run({Input.IP: IP_SWEDEN, Input.LANG: "en"})

        self.assertNotIn("lang", sent_params(mocked))

    def test_non_default_language_is_sent(self, mocked):
        self.action.run({Input.IP: IP_SWEDEN, Input.LANG: "cn"})

        self.assertEqual(sent_params(mocked)["lang"], "cn")

    def test_unsupported_language_is_rejected(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IP: IP_SWEDEN, Input.LANG: "xx"})
        mocked.assert_not_called()

    def test_user_agent_is_sent_as_a_header_not_a_query_parameter(self, mocked):
        self.action.run(
            {
                Input.IP: IP_SWEDEN,
                Input.INCLUDE: ["user_agent"],
                Input.USER_AGENT: "python-requests/2.32.4",
            }
        )

        self.assertEqual(mocked.call_args.kwargs["headers"], {"User-Agent": "python-requests/2.32.4"})
        self.assertNotIn("user_agent", sent_params(mocked))

    def test_no_user_agent_header_when_input_is_blank(self, mocked):
        self.action.run({Input.IP: IP_SWEDEN, Input.USER_AGENT: "   "})

        self.assertIsNone(mocked.call_args.kwargs["headers"])

    def test_domain_lookup_returns_the_domain_and_resolved_ip(self, _):
        actual = self.action.run({Input.IP: DOMAIN})

        result = actual[Output.RESULT]
        self.assertEqual(result["domain"], DOMAIN)
        self.assertEqual(result["ip"], "104.26.5.14")

    def test_empty_strings_are_stripped_but_false_and_zero_survive(self, _):
        result = self.action.run({Input.IP: IP_SWEDEN})[Output.RESULT]

        # dma_code comes back as "" for non-US addresses and should not be emitted.
        self.assertNotIn("dma_code", result["location"])
        # A clean IP legitimately scores zero and must not be dropped as falsy.
        self.assertEqual(result["security"]["threat_score"], 0)
        self.assertIs(result["security"]["is_vpn"], False)
        self.assertIs(result["location"]["is_eu"], True)
        self.assertIs(result["network"]["is_anycast"], False)

    def test_bogon_is_rejected_by_the_api(self, _):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IP: IP_BOGON})

        self.assertIn("bogon", context.exception.cause.lower())
