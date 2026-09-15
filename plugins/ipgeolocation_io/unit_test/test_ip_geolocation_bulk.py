from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.actions.ip_geolocation_bulk import IpGeolocationBulk
from icon_ipgeolocation_io.actions.ip_geolocation_bulk.schema import Input, Output
from unit_test.mock import DOMAIN, IP_BOGON, IP_SWEDEN, make_action, mock_request, sent_body, sent_params
import os
import sys

sys.path.append(os.path.abspath("../"))



@patch("requests.Session.request", side_effect=mock_request)
class TestIpGeolocationBulk(TestCase):
    def setUp(self):
        self.action = make_action(IpGeolocationBulk)

    def test_posts_entries_in_the_request_body(self, mocked):
        self.action.run({Input.IPS: ["8.8.8.8", "1.1.1.1"]})

        self.assertEqual(mocked.call_args.args[0], "POST")
        self.assertEqual(sent_body(mocked), {"ips": ["8.8.8.8", "1.1.1.1"]})

    def test_preserves_submitted_order_and_duplicates(self, mocked):
        actual = self.action.run({Input.IPS: [" 8.8.8.8 ", "1.1.1.1", "8.8.8.8"]})

        self.assertEqual(sent_body(mocked)["ips"], ["8.8.8.8", "1.1.1.1", "8.8.8.8"])
        self.assertEqual([entry["ip"] for entry in actual[Output.RESULTS]], ["8.8.8.8", "1.1.1.1", "8.8.8.8"])

    def test_invalid_entries_come_back_as_messages(self, _):
        actual = self.action.run({Input.IPS: [IP_BOGON, IP_SWEDEN]})

        results = actual[Output.RESULTS]
        self.assertEqual(len(results), 2)
        self.assertIn("bogon", results[0]["message"])
        self.assertNotIn("ip", results[0])
        self.assertEqual(results[1]["ip"], IP_SWEDEN)

    def test_domains_are_accepted_alongside_addresses(self, _):
        actual = self.action.run({Input.IPS: [DOMAIN, "8.8.8.8"]})

        self.assertEqual(actual[Output.RESULTS][0]["domain"], DOMAIN)

    def test_query_parameters_travel_in_the_url(self, mocked):
        self.action.run({Input.IPS: ["8.8.8.8"], Input.INCLUDE: ["security"], Input.EXCLUDES: ["currency"]})

        params = sent_params(mocked)
        self.assertEqual(params["include"], "security")
        self.assertEqual(params["excludes"], "currency")

    def test_empty_list_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException):
            self.action.run({Input.IPS: []})
        mocked.assert_not_called()

    def test_oversized_batch_is_rejected_before_any_request(self, mocked):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.IPS: [f"1.1.1.{index}" for index in range(50001)]})

        self.assertIn("50,000", context.exception.assistance)
        mocked.assert_not_called()
