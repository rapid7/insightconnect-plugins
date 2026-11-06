import os
import sys

sys.path.append(os.path.abspath("../"))

import datetime
from unittest import TestCase

from icon_whoisfreaks.util import constants, feed

THREAT_HEADER = ",".join(constants.THREAT_FEED_COLUMNS)
THREAT_ROW = (
    "Roblox.com.bn,phishing,0.92,2026-06-25 13:45:22.864798+00,2026-10-12 00:16:50.02713+00,t,t,f,,,"
    '"email:a@example.com | phone:14692355437"'
)


class TestFeedDefinitions(TestCase):
    def test_nrd(self):
        plain = feed.nrd_feed("gtld", False)
        self.assertEqual("/v3.3/stream/domainer/gtld", plain.path)
        self.assertEqual(("newly", "gtld"), plain.status_path)
        self.assertEqual("newly.gtld[whois=false]", plain.identity)
        self.assertFalse(plain.is_csv)
        whois = feed.nrd_feed("cctld", True)
        self.assertTrue(whois.is_csv)
        self.assertEqual(83, len(whois.columns))
        self.assertEqual("newly.cctld[whois=true]", whois.identity)

    def test_threat(self):
        threat = feed.threat_feed("malware")
        self.assertEqual("/v3.4/stream/threat-feed/malware", threat.path)
        self.assertEqual("threat_feed.malware", threat.identity)
        self.assertEqual("Malware threat feed", threat.label)


class TestWindow(TestCase):
    def test_resolve(self):
        status = {"threat_feed": {"spam": {"last_update": "2026-10-30", "available_from": "2026-07-29"}}}
        window = feed.resolve_window(status, ("threat_feed", "spam"))
        self.assertEqual(datetime.date(2026, 7, 29), window.available_from)
        self.assertTrue(window.contains(datetime.date(2026, 10, 30)))
        self.assertFalse(window.contains(datetime.date(2026, 10, 31)))

    def test_unavailable(self):
        cases = [
            {},
            {"newly": "x"},
            {"newly": {"gtld": {"last_update": "Not Available", "available_from": "Not Available"}}},
            {"newly": {"gtld": {"last_update": "2026-01-01", "available_from": "2026-02-01"}}},
            {"newly": {"gtld": ["2026-01-01"]}},
        ]
        for status in cases:
            with self.subTest(status=status):
                self.assertIsNone(feed.resolve_window(status, ("newly", "gtld")))


class TestParsing(TestCase):
    def test_threat_page(self):
        page = feed.parse_page(f"{THREAT_HEADER}\n{THREAT_ROW}\n", feed.threat_feed("phishing"))
        self.assertEqual(1, page.raw_count)
        self.assertFalse(page.header_missing)
        self.assertEqual(
            {
                "domain": "roblox.com.bn",
                "threat_type": "phishing",
                "confidence": 0.92,
                "first_seen": "2026-06-25T13:45:22.864798+00:00",
                "last_seen": "2026-10-12T00:16:50.027130+00:00",
                "is_seed": True,
                "is_extrapolated": True,
                "is_dropped": False,
                "matched_pivots": ["email:a@example.com", "phone:14692355437"],
            },
            page.rows[0],
        )

    def test_header_only_page_is_end(self):
        self.assertEqual(0, feed.parse_page(f"{THREAT_HEADER}\n", feed.threat_feed("spam")).raw_count)

    def test_missing_header_uses_documented_columns(self):
        page = feed.parse_page(f"{THREAT_ROW}\n", feed.threat_feed("phishing"))
        self.assertTrue(page.header_missing)
        self.assertEqual("roblox.com.bn", page.rows[0]["domain"])

    def test_short_and_long_rows(self):
        text = f"{THREAT_HEADER}\nshort.com,phishing\nlong.com,spam,1,,,,,,,,,extra,columns\n"
        rows = feed.parse_page(text, feed.threat_feed("spam")).rows
        self.assertEqual({"domain": "short.com", "threat_type": "phishing"}, rows[0])
        self.assertEqual(1.0, rows[1]["confidence"])
        self.assertNotIn("extra", str(rows[1]))

    def test_unknown_values_are_preserved_as_text(self):
        text = f"{THREAT_HEADER}\nx.com,phishing,high,yesterday,,maybe,,,,,\n"
        row = feed.parse_page(text, feed.threat_feed("phishing")).rows[0]
        self.assertEqual("yesterday", row["first_seen"])
        self.assertNotIn("confidence", row)
        self.assertNotIn("is_seed", row)

    def test_whois_page_with_quoted_commas_and_newlines(self):
        header = ",".join(constants.NRD_WHOIS_COLUMNS)
        row = '1,"Example.com","2026-09-14 15:01:20","2026-09-09","","2027-09-09","","Registrar, Inc.","","","","","","","","","Name\nSecond line"'
        page = feed.parse_page(f"{header}\n{row}\n", feed.nrd_feed("gtld", True))
        record = page.rows[0]
        self.assertEqual(1, record["num"])
        self.assertEqual("example.com", record["domain_name"])
        self.assertEqual("2026-09-14T15:01:20", record["query_time"])
        self.assertEqual("Registrar, Inc.", record["domain_registrar_name"])
        self.assertEqual("Name\nSecond line", record["registrant_name"])
        self.assertNotIn("update_date", record)

    def test_plain_page(self):
        page = feed.parse_page("Zuqujl26.com.cn\n\nsurreyasphaltpaving.ca\n", feed.nrd_feed("cctld", False))
        self.assertEqual([{"domain_name": "zuqujl26.com.cn"}, {"domain_name": "surreyasphaltpaving.ca"}], page.rows)
        self.assertEqual(2, page.raw_count)
        self.assertEqual("surreyasphaltpaving.ca", page.last_line)

    def test_plain_page_past_the_end_repeats_last_line(self):
        page = feed.parse_page("last.com\n", feed.nrd_feed("gtld", False), previous_last_line="last.com")
        self.assertEqual(0, page.raw_count)
        self.assertEqual([], page.rows)
        self.assertEqual("last.com", page.last_line)

    def test_plain_page_skips_non_domain_lines(self):
        page = feed.parse_page('ok.com\n{"timestamp":1,"status":401}\nnot a domain\n', feed.nrd_feed("gtld", False))
        self.assertEqual([{"domain_name": "ok.com"}], page.rows)
        self.assertEqual(3, page.raw_count)
        self.assertEqual(2, page.invalid_lines)

    def test_empty_page(self):
        for text in (None, "", "  \n"):
            with self.subTest(text=text):
                self.assertEqual(0, feed.parse_page(text, feed.nrd_feed("gtld", False), "x.com").raw_count)


class TestRowFilter(TestCase):
    def test_filters(self):
        threat = feed.threat_feed("phishing")
        accept = feed.build_row_filter(threat, ["brand"], ["com", "co.uk"], 0.8)
        self.assertTrue(accept({"domain": "my-brand.co.uk", "confidence": 0.9}))
        self.assertFalse(accept({"domain": "my-brand.net", "confidence": 0.9}))
        self.assertFalse(accept({"domain": "other.com", "confidence": 0.9}))
        self.assertFalse(accept({"domain": "brand.com", "confidence": 0.5}))
        self.assertFalse(accept({"domain": "brand.com"}))
        self.assertTrue(feed.build_row_filter(threat, [], [], None)({"domain": "anything.org"}))
