import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.util import outputs, validators
from icon_whoisfreaks.util.client import LookupResult
from icon_whoisfreaks.util.errors import (
    SERVICE_FEED,
    SERVICE_LOOKUP,
    SERVICE_STATUS,
    Kind,
    WhoisFreaksError,
    classify,
    redact,
)


class TestClassify(TestCase):
    def test_documented_errors(self):
        cases = [
            (400, "Please pass apiKey param value.", SERVICE_LOOKUP, Kind.INVALID_CREDENTIALS),
            (400, "Please pass valid apiKey param value", SERVICE_FEED, Kind.INVALID_CREDENTIALS),
            (400, "Request-param 'format' (x) is not valid.", SERVICE_LOOKUP, Kind.BAD_REQUEST),
            (400, "Date is not available", SERVICE_FEED, Kind.DATE_NOT_AVAILABLE),
            (401, "Provided API key is invalid.", SERVICE_LOOKUP, Kind.INVALID_CREDENTIALS),
            (401, "Provided API key is inactive.", SERVICE_LOOKUP, Kind.INVALID_CREDENTIALS),
            (401, "Please buy a subscription plan or add api credits", SERVICE_LOOKUP, Kind.NO_CREDITS),
            (401, "You are blocked due to suspicious activity.", SERVICE_LOOKUP, Kind.ACCOUNT_BLOCKED),
            (401, "Api record not found.", SERVICE_FEED, Kind.END_OF_DATA),
            (401, "Api record not found.", SERVICE_LOOKUP, Kind.INVALID_CREDENTIALS),
            (401, "Please buy domainer package.", SERVICE_FEED, Kind.NOT_ENTITLED),
            (401, "Your domainer package plan is inactive.", SERVICE_FEED, Kind.NOT_ENTITLED),
            (401, "Please buy database subscription.", SERVICE_FEED, Kind.NOT_ENTITLED),
            (401, "You have exceeded the download limit of 20000.", SERVICE_FEED, Kind.PLAN_LIMIT),
            (402, "", SERVICE_LOOKUP, Kind.NO_CREDITS),
            (403, "WHOIS is not offered for this TLD", SERVICE_LOOKUP, Kind.FORBIDDEN),
            (403, "access denied for this key", SERVICE_LOOKUP, Kind.NOT_ENTITLED),
            (403, "", SERVICE_FEED, Kind.NOT_ENTITLED),
            (404, "Record not found.", SERVICE_LOOKUP, Kind.NOT_FOUND),
            (404, "Internal Server Error occurred", SERVICE_LOOKUP, Kind.SERVER_ERROR),
            (404, "File is not available of this date.", SERVICE_FEED, Kind.DATE_NOT_AVAILABLE),
            (404, "", SERVICE_STATUS, Kind.SERVER_ERROR),
            (405, "", SERVICE_LOOKUP, Kind.METHOD_NOT_ALLOWED),
            (408, "", SERVICE_LOOKUP, Kind.UPSTREAM_TIMEOUT),
            (412, "", SERVICE_LOOKUP, Kind.PLAN_LIMIT),
            (413, "API credit limit exceeded. Please upgrade your plan.", SERVICE_LOOKUP, Kind.NO_CREDITS),
            (413, "Surcharge limit exceeded. Please upgrade your plan.", SERVICE_LOOKUP, Kind.NO_CREDITS),
            (
                413,
                "The requested list size is [101] which exceeds the maximum list size of 100.",
                SERVICE_LOOKUP,
                Kind.LIST_TOO_LARGE,
            ),
            (413, "Maximum request body size limit exceeded", SERVICE_LOOKUP, Kind.LIST_TOO_LARGE),
            (
                413,
                "Please upgrade your plans.This Plan does not have to access to download file.",
                SERVICE_FEED,
                Kind.NOT_ENTITLED,
            ),
            (415, "", SERVICE_LOOKUP, Kind.BAD_REQUEST),
            (423, "", SERVICE_LOOKUP, Kind.RESERVED_IP),
            (429, "", SERVICE_LOOKUP, Kind.RATE_LIMITED),
            (499, "", SERVICE_LOOKUP, Kind.SERVER_ERROR),
            (500, "", SERVICE_LOOKUP, Kind.SERVER_ERROR),
            (502, "Please provide ips in request body.", SERVICE_LOOKUP, Kind.BAD_REQUEST),
            (502, "Bad gateway", SERVICE_LOOKUP, Kind.SERVER_ERROR),
            (503, "", SERVICE_FEED, Kind.SERVER_ERROR),
            (504, "", SERVICE_LOOKUP, Kind.SERVER_ERROR),
            (505, "", SERVICE_LOOKUP, Kind.UNEXPECTED),
            (301, "", SERVICE_LOOKUP, Kind.REDIRECT),
            (199, "", SERVICE_LOOKUP, Kind.UNEXPECTED),
        ]
        for status, message, service, kind in cases:
            with self.subTest(status=status, message=message, service=service):
                self.assertEqual(kind, classify(status, message, service))

    def test_error_text(self):
        error = WhoisFreaksError(Kind.NO_CREDITS, "IP Security", 413, "Credit limit exceeded", "detail")
        self.assertEqual(
            "IP Security: The WhoisFreaks account has no remaining credits or no active plan (detail). "
            "WhoisFreaks said: Credit limit exceeded",
            error.cause,
        )
        self.assertEqual("HTTP 413", error.data)
        self.assertIsInstance(error, PluginException)

    def test_unknown_kind_text(self):
        self.assertIn("unexpected response", WhoisFreaksError("made-up", "Op").cause)

    def test_redact(self):
        self.assertEqual("x ******** y", redact("x secret-key y", ("secret-key",)))
        self.assertEqual("/p?a=1&apiKey=********&b=2", redact("/p?a=1&apiKey=abc123&b=2"))
        self.assertEqual("api_key=********", redact("api_key=zzz"))
        self.assertEqual("abc", redact("abc", ("", "ab")))


class TestValidators(TestCase):
    def test_domains(self):
        cases = {
            " Example.COM. ": "example.com",
            "https://Sub.Example.co.uk:8443/path": "sub.example.co.uk",
            "bücher.de": "xn--bcher-kva.de",
            "_dmarc.example.com": "_dmarc.example.com",
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(expected, validators.domain(value))
        for value in (
            "",
            None,
            "localhost",
            "a b.com",
            "-bad.com",
            "example.123",
            "x" * 64 + ".com",
            "a..com",
            "\udcff.com",
        ):
            with self.subTest(value=value), self.assertRaises(PluginException):
                validators.domain(value)

    def test_ip(self):
        self.assertEqual(("8.8.8.8", None), validators.ip(" 8.8.8.8 "))
        self.assertEqual((None, validators.REASON_SPECIAL_IP), validators.ip("10.0.0.1"))
        self.assertEqual((None, validators.REASON_SPECIAL_IP), validators.ip("240.0.0.1"))
        with self.assertRaises(PluginException):
            validators.ip("8.8.8")

    def test_asn(self):
        for value in ("AS15169", "as15169", " 15169 "):
            with self.subTest(value=value):
                self.assertEqual("15169", validators.asn(value))
        with self.assertRaises(PluginException):
            validators.asn("AS")

    def test_integer(self):
        self.assertEqual(5, validators.integer(None, "N", 1, default=5))
        self.assertEqual(3, validators.integer(3, "N", 1, 4))
        for value in (0, 5, True, "3", 2.5):
            with self.subTest(value=value), self.assertRaises(PluginException):
                validators.integer(value, "N", 1, 4)
        with self.assertRaises(PluginException) as context:
            validators.integer(0, "N", 1)
        self.assertIn("at least 1", context.exception.assistance)

    def test_dates_and_record_types(self):
        self.assertIsNone(validators.date("  ", "After"))
        self.assertEqual("2026-01-31", validators.date("2026-01-31", "After"))
        with self.assertRaises(PluginException):
            validators.date("2026-02-30", "After")
        self.assertEqual("all", validators.record_types(None))
        self.assertEqual("all", validators.record_types(" ALL "))
        self.assertEqual("A,MX", validators.record_types("a, mx, a"))
        for value in (",", "PTR"):
            with self.subTest(value=value), self.assertRaises(PluginException):
                validators.record_types(value, allow_ptr=False)

    def test_lists(self):
        self.assertEqual(["brand", "acme"], validators.keywords([" Brand ", "", None, "acme", "brand"]))
        self.assertEqual(["co.uk", "com"], validators.tlds([".CO.UK", "com", "."]))
        self.assertEqual((None, "Not a valid TLD"), validators.try_tld("bad tld"))
        self.assertEqual((None, "Not a valid TLD"), validators.try_tld("\udcff"))
        self.assertEqual(([], []), validators.bulk(None, validators.try_ip, "IPs", required=False))


class TestOutputs(TestCase):
    def test_coercion(self):
        self.assertEqual(3, outputs.to_int("3.0"))
        self.assertIsNone(outputs.to_int("3.5"))
        self.assertIsNone(outputs.to_int(True))
        self.assertIsNone(outputs.to_int("x"))
        self.assertEqual(0.5, outputs.to_float("0.5"))
        self.assertIsNone(outputs.to_float("x"))
        self.assertIsNone(outputs.to_float(None))
        self.assertTrue(outputs.to_bool("Yes"))
        self.assertFalse(outputs.to_bool("f"))
        self.assertIsNone(outputs.to_bool("maybe"))
        self.assertIsNone(outputs.to_str({"a": 1}))
        self.assertIsNone(outputs.to_str("  "))
        self.assertEqual(["a", "1"], outputs.to_str_list(["a", None, 1, " "]))
        self.assertIsNone(outputs.to_str_list("a"))
        self.assertEqual([], outputs.to_object_list("a"))
        self.assertIsNone(outputs.get_path({"a": "x"}, "a", "b"))
        self.assertEqual(2, outputs.first_of({"a": None, "b": 2}, "a", "b"))
        self.assertEqual([{"b": 1}], outputs.without_keys([{"a": 1, "b": 1}], ["a"]))

    def test_builders(self):
        found = LookupResult(200, {"x": 1})
        self.assertEqual(
            {"found": True, "status_code": 200, "response": {"x": 1}, "y": 2}, outputs.single(found, {"y": 2})
        )
        missing = LookupResult(404, None, False, "Record not found")
        self.assertEqual(
            {"found": False, "status_code": 404, "message": "Record not found"}, outputs.single(missing, {"y": 2})
        )
        self.assertEqual({"results": [], "skipped": []}, outputs.bulk(None, None, []))
        self.assertEqual([], outputs.bulk(missing, "key", [])["results"])
