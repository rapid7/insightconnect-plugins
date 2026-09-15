from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ipgeolocation_io.util.helpers import (
    normalize_asn,
    normalize_language,
    to_csv,
    validate_bulk_entries,
    validate_bulk_ips,
    validate_ip,
)

import os
import sys

sys.path.append(os.path.abspath("../"))



class TestHelpers(TestCase):
    def test_to_csv_joins_strips_and_deduplicates(self):
        self.assertEqual(to_csv(["security", " abuse ", "security"]), "security,abuse")

    def test_to_csv_returns_none_for_empty_input(self):
        for value in (None, [], ["", "   "]):
            self.assertIsNone(to_csv(value))

    def test_normalize_asn_strips_prefix(self):
        for value in ("24940", "AS24940", "as24940", " AS24940 "):
            self.assertEqual(normalize_asn(value), "24940")

    def test_normalize_asn_rejects_non_numeric(self):
        with self.assertRaises(PluginException):
            normalize_asn("HETZNER-AS")

    def test_normalize_asn_passes_through_blank(self):
        self.assertIsNone(normalize_asn(""))

    def test_validate_ip_accepts_v4_and_v6(self):
        self.assertEqual(validate_ip("8.8.8.8", "IP"), "8.8.8.8")
        self.assertEqual(validate_ip(" 2001:4860:4860::8888 ", "IP"), "2001:4860:4860::8888")

    def test_validate_ip_rejects_domain(self):
        with self.assertRaises(PluginException) as context:
            validate_ip("ipgeolocation.io", "IP")
        self.assertIn("not a valid IPv4 or IPv6 address", context.exception.cause)

    def test_validate_ip_rejects_private_and_bogon(self):
        for value in ("10.0.0.0", "192.168.1.1", "127.0.0.1", "100.64.0.1"):
            with self.assertRaises(PluginException) as context:
                validate_ip(value, "IP")
            self.assertIn("private or bogon", context.exception.cause)

    def test_validate_ip_allows_private_when_not_required_routable(self):
        self.assertEqual(validate_ip("10.0.0.0", "IP", require_routable=False), "10.0.0.0")

    def test_validate_bulk_entries_rejects_empty(self):
        with self.assertRaises(PluginException):
            validate_bulk_entries([" ", ""], "IPs")

    def test_validate_bulk_entries_rejects_oversized_batch(self):
        with self.assertRaises(PluginException) as context:
            validate_bulk_entries([f"1.1.1.{index}" for index in range(50001)], "IPs")
        self.assertIn("50,000", context.exception.assistance)

    def test_validate_bulk_entries_preserves_order_and_duplicates(self):
        self.assertEqual(
            validate_bulk_entries(["8.8.8.8", "1.1.1.1", "8.8.8.8"], "IPs"), ["8.8.8.8", "1.1.1.1", "8.8.8.8"]
        )

    def test_validate_bulk_ips_rejects_domains(self):
        with self.assertRaises(PluginException) as context:
            validate_bulk_ips(["8.8.8.8", "example.com"], "IPs")
        self.assertIn("example.com", context.exception.cause)

    def test_validate_bulk_ips_keeps_bogons_for_the_api_to_report(self):
        self.assertEqual(validate_bulk_ips(["10.0.0.0", "8.8.8.8"], "IPs"), ["10.0.0.0", "8.8.8.8"])

    def test_normalize_language_drops_default(self):
        self.assertIsNone(normalize_language("en"))
        self.assertIsNone(normalize_language(None))

    def test_normalize_language_lowercases_supported_value(self):
        self.assertEqual(normalize_language("CN"), "cn")

    def test_normalize_language_rejects_unsupported(self):
        with self.assertRaises(PluginException):
            normalize_language("xx")
