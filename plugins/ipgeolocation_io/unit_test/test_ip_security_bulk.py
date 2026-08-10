from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.ip_security_bulk import IpSecurityBulk
from icon_ipgeolocation_io.actions.ip_security_bulk.schema import Input, Output
from unit_test.mock import DOMAIN, IP_BOGON, IP_CLEAN, IP_MALICIOUS, make_action, mock_request, sent_body

import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestIpSecurityBulk(TestCase):
    def setUp(self):
        self.action = make_action(IpSecurityBulk)

    def test_assesses_a_batch(self, mocked):
        actual = self.action.run({Input.IPS: [IP_MALICIOUS, IP_CLEAN]})

        results = actual[Output.RESULTS]
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["security"]["threat_score"], 80)
        self.assertEqual(results[1]["security"]["threat_score"], 0)
        self.assertEqual(sent_body(mocked), {"ips": [IP_MALICIOUS, IP_CLEAN]})

    def test_bogon_entries_are_reported_per_entry_not_rejected(self, mocked):
        actual = self.action.run({Input.IPS: [IP_BOGON, IP_CLEAN]})

        results = actual[Output.RESULTS]
        self.assertIn("bogon", results[0]["message"])
        self.assertEqual(results[1]["ip"], IP_CLEAN)
        # The bogon must still be sent so the results stay aligned with the input.
        self.assertEqual(sent_body(mocked)["ips"], [IP_BOGON, IP_CLEAN])

    def test_domains_are_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IPS: ["8.8.8.8", DOMAIN]})

        self.assertIn("Domain names are not supported", context.exception.assistance)
        mocked.assert_not_called()

    def test_empty_list_is_rejected(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IPS: []})
        mocked.assert_not_called()
