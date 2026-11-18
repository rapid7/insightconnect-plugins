import os
import sys

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.actions.reverse_dns import ReverseDns
from icon_whoisfreaks.util.errors import WhoisFreaksError
from util import ActionTestCase, MockResponse


class TestReverseDns(ActionTestCase):
    action_class = ReverseDns

    def test_reverse_a(self):
        body = {
            "totalRecords": 1500,
            "totalPages": 15,
            "currentPage": 1,
            "reverseDnsRecords": [{"domainName": "a.com"}],
        }
        params = {"value": "8.8.8.8", "record_type": "a", "exact": True, "sort": "desc", "page": 1}
        output, session = self.run_action(params, MockResponse(200, body))
        self.assert_request(
            session,
            "GET",
            "/v2.1/dns/reverse",
            {"value": "8.8.8.8", "type": "a", "exact": "true", "sort": "desc", "page": 1},
        )
        self.assertEqual(15, output["total_pages"])

    def test_reverse_mx(self):
        _, session = self.run_action({"value": "mx.example.com", "record_type": "mx"}, MockResponse(200, {}))
        self.assertEqual(
            {"value": "mx.example.com", "type": "mx", "exact": "true", "page": 1}, session.calls[-1]["params"]
        )

    def test_private_ip_for_a_record(self):
        output, session = self.run_action({"value": "10.1.1.1", "record_type": "a"})
        self.assertEqual([], session.calls)
        self.assertFalse(output["found"])

    def test_invalid_ip_for_a_record(self):
        with self.assertRaises(PluginException):
            self.run_action({"value": "mail.example.com", "record_type": "a"})

    def test_empty_value(self):
        with self.assertRaises(PluginException):
            self.run_action({"value": " ", "record_type": "ns"})
